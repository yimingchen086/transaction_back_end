from flask_smorest import Blueprint, abort
from exts import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from models.schemas import TransactionCreateSchema, TransactionSchema, TransactionUpdateSchema, RecentTransactionsQuerySchema
from models.transaction_db import Transaction
import json
import traceback
from decimal import Decimal


# 確保 url_prefix 正確設定在 Blueprint
transaction_bp = Blueprint("transaction", __name__, url_prefix="/api/transaction", description="交易紀錄 API")



@transaction_bp.route("", methods=['POST'])
@transaction_bp.arguments(TransactionCreateSchema)
@transaction_bp.response(201, TransactionCreateSchema)
def create_transaction(transaction_data):
    """新增一筆交易紀錄"""
    try:
        new_transaction = Transaction(**transaction_data)
        db.session.add(new_transaction)
        db.session.commit()
        return new_transaction
    except IntegrityError:
        db.session.rollback()
        print(traceback.format_exc())  # 顯示完整錯誤
        abort(400, message="資料庫完整性錯誤，請檢查 transaction_method_id、category_id 或 card_id 是否存在")
    except Exception as e:
        print("❌ 交易建立失敗:", str(e))
        print(traceback.format_exc())  # 顯示完整錯誤
        abort(500, message=f"內部伺服器錯誤: {str(e)}")


@transaction_bp.route("/<int:transaction_id>", methods=['GET'])
@transaction_bp.response(200, TransactionSchema)
def get_transaction(transaction_id):
    """根據 transaction_id 獲取一筆交易紀錄"""
    try:
        # 查詢交易
        transaction = Transaction.query.get(transaction_id)

        # 如果交易不存在，返回 404
        if not transaction:
            abort(404, message="交易紀錄不存在")

        # 返回交易數據
        return transaction
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")


@transaction_bp.route("/<int:transaction_id>", methods=['PUT'])
@transaction_bp.arguments(TransactionUpdateSchema)
@transaction_bp.response(200, TransactionSchema)
def update_transaction(transaction_data, transaction_id):
    """根據 transaction_id 更新一筆交易紀錄"""
    try:
        # 查詢交易
        transaction = Transaction.query.get(transaction_id)

        # 如果交易不存在，返回 404
        if not transaction:
            abort(404, message="交易紀錄不存在")

        # 更新交易數據
        for key, value in transaction_data.items():
            setattr(transaction, key, value)

        # 提交到資料庫
        db.session.commit()

        # 返回更新後的交易數據
        return transaction
    except IntegrityError:
        db.session.rollback()
        abort(400, message="資料庫完整性錯誤，請檢查 transaction_method_id、category_id 或 card_id 是否存在")
    except Exception as e:
        db.session.rollback()
        abort(500, message=f"內部伺服器錯誤: {str(e)}")


@transaction_bp.route("/<int:transaction_id>", methods=['DELETE'])
@transaction_bp.response(204)
def delete_transaction(transaction_id):
    """根據 transaction_id 刪除一筆交易紀錄"""
    try:
        # 查詢交易
        transaction = Transaction.query.get(transaction_id)

        # 如果交易不存在，返回 404
        if not transaction:
            abort(404, message="交易紀錄不存在")

        # 刪除交易
        db.session.delete(transaction)
        db.session.commit()

        # 返回空回應，狀態碼為 204
        return '', 204
    except IntegrityError:
        db.session.rollback()
        abort(400, message="資料庫完整性錯誤，無法刪除交易")
    except Exception as e:
        db.session.rollback()
        abort(500, message=f"內部伺服器錯誤: {str(e)}")


@transaction_bp.route("/recent", methods=['GET'])
@transaction_bp.arguments(RecentTransactionsQuerySchema, location="query")
@transaction_bp.response(200, TransactionSchema(many=True))
def get_recent_transactions(args):
    """根據查詢參數 take 獲取最近的交易紀錄"""
    try:
        print(args)
        take = args["take"]

        if take <= 0:
            abort(400, message="參數 take 必須是正整數")

        transactions = Transaction.query.order_by(Transaction.transaction_id.desc()).limit(take).all()

        return transactions
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")