# from flask import Flask
#
# # 從當前目錄（routes）匯入各個 Blueprint
# from .cards_routes import cards_bp
# # from .consumption_routes import consumption_bp
#
# def register_blueprints(app: Flask):
#     """
#     統一註冊所有的 Blueprint
#     """
#     app.register_blueprint(cards_bp, url_prefix='/api/cards')
#     # app.register_blueprint(consumption_bp, url_prefix="/api/consumption")
from flask import Flask
from .category_routes import category_bp
from .cards_routes import cards_bp
from flask_smorest import Api


def register_blueprints(api: Api):
    """
    統一註冊所有的 Blueprint
    """
    api.register_blueprint(cards_bp)
    api.register_blueprint(category_bp)