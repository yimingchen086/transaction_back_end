from flask_smorest import Blueprint, abort
from exts import db
from sqlalchemy.exc import IntegrityError
from models.schemas import TransactionMethodSchema
from models.transaction_method_db import TransactionMethod

# 創建 Blueprint
transaction_method_bp = Blueprint("transaction_method", __name__, url_prefix="/api/transaction_method", description="交易方式相關操作")

@transaction_method_bp.route("", methods=['POST'])
@transaction_method_bp.arguments(TransactionMethodSchema, description="創建一個新的交易方式")
@transaction_method_bp.response(201, TransactionMethodSchema, description="成功創建交易方式")
def create_transaction_method(transaction_method_data):
    """創建一個新的交易方式"""
    try:
        # 創建新的交易方式
        new_method = TransactionMethod(**transaction_method_data)

        # 添加到數據庫
        db.session.add(new_method)
        db.session.commit()

        return new_method
    except IntegrityError:
        db.session.rollback()
        abort(409, message="交易方式名稱已存在")
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")


@transaction_method_bp.route("/<int:method_id>", methods=['GET'])
@transaction_method_bp.response(200, TransactionMethodSchema, description="成功獲取交易方式")
def get_transaction_method(method_id):
    """根據 ID 獲取單個交易方式"""
    try:
        method = TransactionMethod.query.get_or_404(method_id, description="交易方式不存在")
        return method
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")

@transaction_method_bp.route("", methods=['GET'])
@transaction_method_bp.response(200, TransactionMethodSchema(many=True), description="成功獲取所有交易方式")
def get_all_transaction_methods():
    """獲取所有交易方式"""
    methods = TransactionMethod.query.all()
    return methods


@transaction_method_bp.route("/<int:method_id>", methods=['PUT'])
@transaction_method_bp.arguments(TransactionMethodSchema(partial=True), description="更新交易方式的數據")
@transaction_method_bp.response(200, TransactionMethodSchema, description="成功更新交易方式")
def update_transaction_method(transaction_method_data, method_id):
    """更新一個交易方式"""
    method = TransactionMethod.query.get_or_404(method_id, description="交易方式不存在")

    try:
        # 更新數據
        if "name" in transaction_method_data:
            method.name = transaction_method_data["name"]

        # 提交到數據庫
        db.session.commit()

        # 返回更新後的交易方式
        return method
    except IntegrityError:
        abort(409, message="交易方式名稱已存在")
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")


@transaction_method_bp.route("/<int:method_id>", methods=['DELETE'])
@transaction_method_bp.response(204, description="成功刪除交易方式")
def delete_transaction_method(method_id):
    """刪除一個交易方式"""
    method = TransactionMethod.query.get_or_404(method_id, description="交易方式不存在")

    try:
        # 從數據庫中刪除
        db.session.delete(method)
        db.session.commit()

        # 返回空響應
        return ""
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")

@transaction_method_bp.route("", methods=['GET'])
@transaction_method_bp.response(200, TransactionMethodSchema(many=True), description="成功獲取所有交易方式")
def get_all_transaction_methods():
    """獲取所有交易方式"""
    try:
        # 查詢所有交易方式
        methods = TransactionMethod.query.all()

        # 返回序列化後的數據
        return methods
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")