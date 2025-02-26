from marshmallow import Schema, fields, validate

class CategorySchema(Schema):
    category_id = fields.Int(dump_only=True)  # 僅用於輸出，不需要輸入
    category_name = fields.Str(required=True, validate=validate.Length(min=1, max=100))  # 類別名稱，必填
    transaction_type = fields.Str(required=True, validate=validate.OneOf(['income', 'expense']))  # 交易類型，必填

    class Meta:
        fields = ('category_id', 'category_name', 'transaction_type')