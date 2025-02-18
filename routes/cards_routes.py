from flask_smorest import Blueprint, abort
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


@cards_bp.route("", methods=["POST"])
@cards_bp.arguments(CardInfoCreateSchema)
@cards_bp.response(201, CardInfoSchema)
def create_card(card_data):
    """新增信用卡"""
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


@cards_bp.route("/<int:card_id>", methods=["PUT"])
@cards_bp.arguments(CardInfoUpdateSchema)
def update_card(updated_data, card_id):
    """更新信用卡資訊"""
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


@cards_bp.route("/<int:card_id>", methods=["DELETE"])
def delete_card(card_id):
    """刪除信用卡"""
    try:
        card = CardInfo.query.get(card_id)

        if not card:
            abort(404, description="Card not found")

        db.session.delete(card)
        db.session.commit()

        return "", 204

    except IntegrityError:
        db.session.rollback()
        abort(409, description="Cannot delete card due to database constraints")  # 409 Conflict

    except Exception as e:
        abort(500, description=f"Internal server error: {str(e)}")  # 500 Internal Server Error


@cards_bp.route("/<int:card_id>", methods=["GET"])
@cards_bp.response(200, CardInfoSchema)
def get_card(card_id):
    """取得單一信用卡資料"""
    card = CardInfo.query.get(card_id)

    if not card:
        abort(404, description="Card not found")

    return card
