from marshmallow import Schema, fields, validate


class TransactionUpdateSchema(Schema):
    transaction_method_id = fields.Int(required=False)
    transaction_title = fields.Str(required=False)
    amount = fields.Decimal(required=False, places=2, as_string=True)
    category_id = fields.Int(required=False)
    card_id = fields.Int(required=False)
    transaction_time = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z', required=False)
    actual_amount = fields.Integer(default=0, validate=validate.Range(min=0),)