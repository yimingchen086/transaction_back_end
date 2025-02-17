from flask import Blueprint, request, jsonify

# from models.schemas import ConsumptionCreateSchema

consumption_bp = Blueprint('consumption', __name__)

# 新增一筆金額
# @consumption_bp.route('/consumption', method=['POST'])
# def create_consummption():
#     try:
#         consumption_data = ConsumptionCreateSchema.model_validate(request.json)
#
#         return jsonify(consumption_data.to_dict()), 201  # 201 Created
