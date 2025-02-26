from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from models.category_db import Category
from models.schemas import CategorySchema
from exts import db

category_bp = Blueprint("category", __name__,url_prefix="/api/category", description="交易類別 API")

@category_bp.route("", methods=["GET"])
@category_bp.response(200, CategorySchema(many=True))
def get_categories():
    """取得所有交易類別"""
    try:
        categories = Category.query.all()
        return categories
    except SQLAlchemyError:
        abort(500, message="無法取得交易類別資料")

@category_bp.route("/<int:category_id>", methods=["GET"])
@category_bp.response(200, CategorySchema)
def get_category(category_id):
    """取得特定交易類別"""
    category = Category.query.get(category_id)
    if not category:
        abort(404, message="找不到該交易類別")
    return category

@category_bp.route("", methods=["POST"])
@category_bp.arguments(CategorySchema)
@category_bp.response(201, CategorySchema)
def create_category(category_data):
    """新增交易類別"""
    category = Category(**category_data)
    try:
        db.session.add(category)
        db.session.commit()
        return category
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, message="無法新增交易類別")

@category_bp.route("/<int:category_id>", methods=["PUT"])
@category_bp.arguments(CategorySchema)
@category_bp.response(200, CategorySchema)
def update_category(category_data, category_id):
    """更新特定交易類別"""
    category = Category.query.get(category_id)
    if not category:
        abort(404, message="找不到該交易類別")
    try:
        for key, value in category_data.items():
            setattr(category, key, value)
        db.session.commit()
        return category
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, message="無法更新交易類別")

@category_bp.route("/<int:category_id>", methods=["DELETE"])
@category_bp.response(204)
def delete_category(category_id):
    """刪除特定交易類別"""
    category = Category.query.get(category_id)
    if not category:
        abort(404, message="找不到該交易類別")
    try:
        db.session.delete(category)
        db.session.commit()
        return "", 204
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, message="無法刪除交易類別")