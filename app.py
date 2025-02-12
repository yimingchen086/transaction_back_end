import config
from exts import db
from flask_migrate import Migrate
from models import CardInfo
from flask import Flask, request, jsonify
from flask_cors import CORS
from routes import register_blueprints

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

app.config['DEBUG'] = True

app.config.from_object(config)

db.init_app(app)
migrate = Migrate(app, db)

# 模組化後用不到
# @app.route("/")
# def hello_world():
#     return "Hello World!"

register_blueprints(app)


# 紀錄消費
@app.route('/api/consumption', methods=['POST'])
def add_consumption_amount():
    data = request.json

    required_fields = ["card_id", "amount"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    card = CardInfo.query.get(data['card_id'])
    if not card:
        return jsonify({"error": "Card not found"}), 404

    card.curramount = card.curramount + data['amount']

    db.session.commit()

    return jsonify(card.to_dict()), 201  # 201 Created


if __name__ == "__main__":
    app.run()
