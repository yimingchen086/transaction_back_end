import config
from exts import db
from flask_migrate import Migrate
from models import CardInfo
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

app.config.from_object(config)

db.init_app(app)
migrate = Migrate(app, db)

# 模組化後用不到
@app.route("/")
def hello_world():
    return "Hello World!"


# 取得所有卡片
@app.route('/api/cards', methods=['GET'])
def get_cards():
    cards = CardInfo.query.all()
    return jsonify([card.to_dict() for card in cards]), 200


# 新增信用卡 (POST /api/cards)
@app.route('/api/cards', methods=['POST'])
def create_card():
    data = request.json
    required_fields = ["card_name", "bank"]

    # 檢查必填欄位
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    new_card = CardInfo(
        card_name=data["card_name"],
        bank=data["bank"],
        maxconsume=data.get("maxconsume"),
        curramount=data.get("curramount"),
        description=data.get("description"),
        store=data.get("store"),
        rewardstype=data.get("rewardstype"),
        daterange_start=data.get("daterange_start"),
        daterange_end=data.get("daterange_end"),
        postingdate=data.get("postingdate")
    )

    db.session.add(new_card)
    db.session.commit()

    return jsonify(new_card.to_dict()), 201  # 201 Created

#取得單一卡片 (GET /api/cards/<card_id>)
@app.route('/api/cards/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = CardInfo.query.get(card_id)

    if not card:
        return jsonify({"error": "Card not found"}), 404

    return jsonify(card.to_dict()), 200  # 200 OK

#修改信用卡 (PUT /api/cards/<card_id>)
@app.route('/api/cards/<int:card_id>', methods=['PUT'])
def update_card(card_id):
    data = request.json
    card = CardInfo.query.get(card_id)

    if not card:
        return jsonify({"error": "Card not found"}), 404

    # 更新欄位（若沒提供則不變動）
    card.card_name = data.get("card_name", card.card_name)
    card.bank = data.get("bank", card.bank)
    card.maxconsume = data.get("maxconsume", card.maxconsume)
    card.curramount = data.get("curramount", card.curramount)
    card.description = data.get("description", card.description)
    card.store = data.get("store", card.store)
    card.rewardstype = data.get("rewardstype", card.rewardstype)
    card.daterange_start = data.get("daterange_start", card.daterange_start)
    card.daterange_end = data.get("daterange_end", card.daterange_end)
    card.postingdate = data.get("postingdate", card.postingdate)

    db.session.commit()
    return jsonify(card.to_dict()), 200  # 200 OK

@app.route('/api/cards/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    card = CardInfo.query.get(card_id)

    if not card:
        return jsonify({"error": "Card not found"}), 404

    db.session.delete(card)
    db.session.commit()

    return jsonify({"message": "Card deleted successfully"}), 200  # 200 OK


if __name__ == "__main__":
    app.run()

