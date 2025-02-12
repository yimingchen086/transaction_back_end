from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from exts import db
from models.cardInfo import CardInfo
from models.schemas import CardInfoSchema, CardInfoUpdateSchema, CardInfoCreateSchema  # 匯入 Pydantic Schema

# 建立 Blueprint（名稱為 'cards'，該 Blueprint 對應的 URL 前綴為 '/cards'）
cards_bp = Blueprint('cards', __name__)

# 取得所有卡片
@cards_bp.route('/', methods=['GET'])
def get_cards():
    cards = CardInfo.query.all()
    cards_data = [CardInfoSchema.model_validate(card).model_dump() for card in cards]
    return jsonify(cards_data), 200

# 新增信用卡 (POST /api/cards)
@cards_bp.route('/cards', methods=['POST'])
def create_card():
    try:
        card_data = CardInfoCreateSchema.model_validate(request.json)
        # 建立新的 CardInfo 物件
        new_card = CardInfo(
            card_name=card_data.card_name,
            bank=card_data.bank,
            maxconsume=card_data.maxconsume,
            curramount=card_data.curramount,
            description=card_data.description,
            store=card_data.store,
            rewardstype=card_data.rewardstype,
            daterange_start=card_data.daterange_start,
            daterange_end=card_data.daterange_end,
            postingdate=card_data.postingdate
        )
        db.session.add(new_card)
        db.session.commit()
        return jsonify(new_card.to_dict()), 201  # 201 Created

    except ValidationError as e:
        return jsonify({"error": "Invalid data", "details": e.errors()}), 400  # 400 Bad Request
    except IntegrityError:
        db.session.rollback()  # 回滾避免影響資料庫
        return jsonify({"error": "Database integrity error"}), 400  # 400 Bad Request
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500  # 500 Internal Server Error


#修改信用卡 (PUT /api/cards/<card_id>)
@cards_bp.route('/<int:card_id>', methods=['PUT'])
def update_card(card_id):
    card = CardInfo.query.get(card_id)

    if not card:
        return jsonify({"error": "Card not found", "message": f"Card with ID {card_id} does not exist"}), 404

    try:
        # 驗證請求數據
        data = request.get_json()
        validated_data = CardInfoUpdateSchema.model_validate(data).model_dump(exclude_unset=True)  # Pydantic v2 驗證
        # 更新欄位（只更新提供的欄位）
        for key, value in validated_data.items():
            setattr(card, key, value)

        db.session.commit()
        return jsonify(CardInfoUpdateSchema.model_validate(card).model_dump()), 200  # 轉換為 JSON 格式返回
    except ValidationError as e:
        return jsonify({"error": "Validation failed", "details": e.errors()}), 400  # 400 Bad Request
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500  # 500 Internal Server Error

@cards_bp.route('/api/cards/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    try:
        card = CardInfo.query.get(card_id)

        if not card:
            return jsonify({"error": "Card not found"}), 404  # 404 Not Found

        db.session.delete(card)
        db.session.commit()

        return jsonify({"message": "Card deleted successfully"}), 200  # 200 OK

    except IntegrityError:
        db.session.rollback()  # 回滾資料庫
        return jsonify({"error": "Cannot delete card due to database constraints"}), 400  # 400 Bad Request

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500  # 500 Internal Server Error



#取得單一卡片 (GET /api/cards/<card_id>)
@cards_bp.route('/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = CardInfo.query.get(card_id)

    if not card:
        return jsonify({"error": "Card not found", "message": f"Card with ID {card_id} does not exist"}), 404

    card_data = CardInfoSchema.model_validate(card).model_dump()  # Pydantic v2 轉換
    return jsonify(card_data), 200  # 200 OK