from .category_routes import category_bp
from .cards_routes import cards_bp
from .transaction_routes import transaction_bp
from flask_smorest import Api


def register_blueprints(api: Api):
    """
    統一註冊所有的 Blueprint
    """
    api.register_blueprint(cards_bp)
    api.register_blueprint(category_bp)
    api.register_blueprint(transaction_bp)