import config
from exts import db
from flask_migrate import Migrate
from flask import Flask
from flask_cors import CORS
from routes import register_blueprints
from flask_smorest import Api


app = Flask(__name__)
# CORS(app, origins=["http://localhost:5173"])
CORS(app, origins=["http://localhost:5173", "*"], supports_credentials=True)
# CORS(app)

app.config['DEBUG'] = True
app.config.from_object(config)

# 設定 OpenAPI 3 相關資訊
app.config["API_TITLE"] = "Budgeting API"
app.config["API_VERSION"] = "1.0"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


db.init_app(app)
migrate = Migrate(app, db)


api = Api(app)
register_blueprints(api)


if __name__ == "__main__":
    app.run()
    # app.run(host="127.0.0.1", port=5000, debug=True)


# # 紀錄消費
# @app.route('/api/consumption', methods=['POST'])
# def add_consumption_amount():
#     data = request.json
#
#     required_fields = ["card_id", "amount"]
#     if not all(field in data for field in required_fields):
#         return jsonify({"error": "Missing required fields"}), 400
#
#     card = CardInfo.query.get(data['card_id'])
#     if not card:
#         return jsonify({"error": "Card not found"}), 404
#
#     card.curramount = card.curramount + data['amount']
#
#     db.session.commit()
#
#     return jsonify(card.to_dict()), 201  # 201 Created