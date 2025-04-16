from utils.tunnel import create_ssh_tunnel
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config
from sqlalchemy import text


def test_connections():
    print("開始測試連線...")

    # 測試 SSH 通道
    print("\n1. 測試 SSH 通道...")
    tunnel = create_ssh_tunnel()
    if tunnel and tunnel.is_active:
        print("✅ SSH 通道建立成功！")
        print(f"本地端口: {tunnel.local_bind_port}")
    else:
        print("❌ SSH 通道建立失敗！")
        return

    # 動態組出 SQLAlchemy URI，使用 SSH Tunnel 的 port
    db_uri = f"postgresql://{config.DB_USERNAME}:{config.DB_PASSWORD}@127.0.0.1:{tunnel.local_bind_port}/{config.DATABASE}?gssencmode=disable"

    # 建立 Flask app 與 SQLAlchemy
    print("\n2. 測試資料庫連線...")
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db = SQLAlchemy(app)

    try:
        with app.app_context():
            # 測試資料庫查詢
            result = db.session.execute(text("SELECT version();")).scalar()
            print("✅ 資料庫連線成功！")
            print(f"PostgreSQL 版本: {result}")

            # 檢查資料表
            print("\n3. 檢查資料庫表...")
            tables = db.session.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)).fetchall()

            if tables:
                print("發現以下資料表：")
                for table in tables:
                    print(f"- {table[0]}")
            else:
                print("⚠️ 找不到任何資料表")

            # ✅ session.close() 應該放這裡
            db.session.close()

    except Exception as e:
        print(f"❌ 資料庫連線失敗: {str(e)}")

    finally:
        if tunnel:
            tunnel.close()
            print("\nSSH 通道已關閉")


if __name__ == "__main__":
    test_connections()
