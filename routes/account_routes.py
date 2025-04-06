import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from flask_smorest import Blueprint, abort
from exts import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from models.schemas import LoginGoogleSchema, GoogleUserSchema

# 讀取 .env 檔案
load_dotenv()

# 從環境變數讀取 Google OAuth Client ID
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

account_bp = Blueprint("account", __name__, url_prefix="/api/account", description="帳號相關 API")

@account_bp.route("/login_google", methods=["POST"])
@account_bp.arguments(LoginGoogleSchema)
@account_bp.response(200, GoogleUserSchema)
def login_google(data):
    """Google帳號登入"""
    token = data["token"]
    print(token)

    try:
        # 驗證 token，並自動從 Google 下載公鑰
        idinfo = id_token.verify_oauth2_token(
            token,
            google_requests.Request(),
            GOOGLE_CLIENT_ID
        )

        # Token 驗證成功，返回使用者資料
        user_data = {
            "sub": idinfo["sub"],
            "email": idinfo["email"],
            "name": idinfo.get("name"),
            "picture": idinfo.get("picture")
        }
        return user_data

    except ValueError as e:
        # Token 無效（過期、被篡改等）
        abort(401, message=f"Invalid token: {str(e)}")

