from flask import request, jsonify
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, ValidationError
from exts import db
from models.cardInfo import CardInfo
from models.schemas import CardInfoSchema, CardInfoCreateSchema, CardInfoUpdateSchema
from sqlalchemy.exc import IntegrityError, SQLAlchemyError



# 確保 url_prefix 正確設定在 Blueprint
cards_bp = Blueprint("cards", __name__, url_prefix="/api/cards", description="卡片相關 API")


@cards_bp.route("", methods=["GET"])
@cards_bp.response(200, CardInfoSchema(many=True))
def get_cards():
    """取得所有卡片資訊"""
    cards = CardInfo.query.all()
    return cards


@cards_bp.route('', methods=['POST'])
@cards_bp.arguments(CardInfoCreateSchema)
@cards_bp.response(201, CardInfoSchema)
def create_card(card_data):
    """新增信用卡 (POST /api/cards)"""
    try:
        new_card = CardInfo(**card_data)
        db.session.add(new_card)
        db.session.commit()
        return new_card
    except IntegrityError:
        db.session.rollback()
        abort(400, message="資料庫完整性錯誤，請確認輸入資料是否唯一")
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")

@cards_bp.route('/<int:card_id>', methods=['PUT'])
@cards_bp.arguments(CardInfoUpdateSchema)
def update_card(updated_data, card_id):
    """更新信用卡資訊 (PUT /api/cards/<card_id>)"""
    card = CardInfo.query.get(card_id)

    if not card:
        abort(404, message=f"Card with ID {card_id} not found")

    try:
        for key, value in updated_data.items():
            setattr(card, key, value)
            db.session.commit()
            return CardInfoUpdateSchema().dump(card), 200

    except SQLAlchemyError:
        db.session.rollback()
        abort(500, message="Database error")  # 500: 資料庫錯誤



#
# @cards_bp.route('/api/cards/<int:card_id>', methods=['DELETE'])
# def delete_card(card_id):
#     try:
#         card = CardInfo.query.get(card_id)
#
#         if not card:
#             return jsonify({"error": "Card not found"}), 404  # 404 Not Found
#
#         db.session.delete(card)
#         db.session.commit()
#
#         return jsonify({"message": "Card deleted successfully"}), 200  # 200 OK
#
#     except IntegrityError:
#         db.session.rollback()  # 回滾資料庫
#         return jsonify({"error": "Cannot delete card due to database constraints"}), 400  # 400 Bad Request
#
#     except Exception as e:
#         return jsonify({"error": "Internal server error", "details": str(e)}), 500  # 500 Internal Server Error
#
#
#
# #取得單一卡片 (GET /api/cards/<card_id>)
# @cards_bp.route('/<int:card_id>', methods=['GET'])
# def get_card(card_id):
#     card = CardInfo.query.get(card_id)
#
#     if not card:
#         return jsonify({"error": "Card not found", "message": f"Card with ID {card_id} does not exist"}), 404
#
#     card_data = CardInfoSchema.model_validate(card).model_dump()  # Pydantic v2 轉換
#     return jsonify(card_data), 200  # 200 OK
