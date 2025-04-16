from sqlalchemy import text

import config
from exts import db
from flask_migrate import Migrate
from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from routes import register_blueprints
from utils.tunnel import create_ssh_tunnel
import threading
import time


app = Flask(__name__)

# 啟動 SSH tunnel 並取得本地 port
print("⏳ 建立 SSH tunnel...")
tunnel = create_ssh_tunnel()
if not tunnel or not tunnel.is_active:
    raise RuntimeError("❌ 無法建立 SSH 通道")

# 等待 tunnel 完全啟動（保守延遲）
time.sleep(1)
# 組合 SQLAlchemy URI，使用 tunnel 的本地 port
SQLALCHEMY_DATABASE_URI = f"postgresql://{config.DB_USERNAME}:{config.DB_PASSWORD}@127.0.0.1:{tunnel.local_bind_port}/{config.DATABASE}"
print(f"🎯 使用資料庫 URI: {SQLALCHEMY_DATABASE_URI}")

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_object(config)

# CORS 設定
# CORS(app, origins=["http://localhost:5173"])
CORS(app, supports_credentials=True, origins="*")

app.config['DEBUG'] = True
app.config.from_object(config)

# OpenAPI 設定
app.config["API_TITLE"] = "Budgeting API"
app.config["API_VERSION"] = "1.0"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# 初始化 DB
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
register_blueprints(api)


with app.app_context():
    try:
        db.session.execute(text("SELECT 1"))  # ✅ 用 text() 包起來
        print("✅ 資料庫連線成功！")
    except Exception as e:
        print(f"❌ 資料庫連線失敗: {e}")




# 啟動 Flask App
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5001, debug=True)
    finally:
        tunnel.close()
        print("🔒 SSH tunnel 已關閉")
