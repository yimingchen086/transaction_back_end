import config
from exts import db
from flask_migrate import Migrate
from flask import Flask, render_template, jsonify, make_response
from flask_cors import CORS
from routes import register_blueprints
from flask_smorest import Api


app = Flask(__name__)
# CORS(app, origins=["http://localhost:5173"])
# CORS(app, origins=["http://localhost:5173", "*"], supports_credentials=True)
# CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
CORS(app)


app.config['DEBUG'] = True
app.config.from_object(config)

# 設定 OpenAPI 3 相關資訊
app.config["API_TITLE"] = "Budgeting API"
app.config["API_VERSION"] = "1.0"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"



#
# @app.route("/swagger-ui")
# def custom_swagger_ui():
#     return render_template("swagger-ui.html", url="/openapi.json")

db.init_app(app)
migrate = Migrate(app, db)


api = Api(app)
register_blueprints(api)


with app.app_context():
    try:
        db.session.execute("SELECT 1")  # 嘗試執行 SQL 查詢
        print("資料庫連線成功！")
    except Exception as e:
        print(f"資料庫連線失敗: {e}")




if __name__ == "__main__":
    app.run()
    # app.run(debug=True, host="0.0.0.0")
    # app.run(host="127.0.0.1", port=5000, debug=True)