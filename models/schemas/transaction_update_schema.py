from marshmallow import Schema, fields

class TransactionUpdateSchema(Schema):
    transaction_method_id = fields.Int(required=False)
    transaction_title = fields.Str(required=False)
    amount = fields.Decimal(required=False, places=2, as_string=True)
    category_id = fields.Int(required=False)
    card_id = fields.Int(required=False)
    transaction_time = fields.DateTime(format='%Y-%m-%dT%H:%M:%S%z', required=False)