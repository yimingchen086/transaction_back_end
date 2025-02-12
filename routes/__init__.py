from flask import Flask

# 從當前目錄（routes）匯入各個 Blueprint
from .cards_routes import cards_bp

def register_blueprints(app: Flask):
    """
    統一註冊所有的 Blueprint
    """
    app.register_blueprint(cards_bp, url_prefix='/api/cards')
