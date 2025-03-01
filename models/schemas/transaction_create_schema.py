from marshmallow import Schema, fields, validate
from datetime import datetime

class TransactionCreateSchema(Schema):
    transaction_method_id = fields.Integer(
        required=True,
        validate=validate.Range(min=1),
        description="交易方法ID"
    )
    transaction_title = fields.String(
        required=True,
        validate=validate.Length(min=1, max=50),
        description="交易標題"
    )
    amount = fields.Decimal(
        required=True,
        places=2,
        validate=validate.Range(min=0),
        description="交易金額"
    )
    category_id = fields.Integer(
        required=True,
        validate=validate.Range(min=1),
        description="交易類型ID"
    )
    transaction_time = fields.DateTime(
        required=False,
        description="交易時間"
    )
    card_id = fields.Integer(
        required=True,
        validate=validate.Range(min=1),
        description="信用卡資料ID"
    )