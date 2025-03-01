from marshmallow import Schema, fields, validate

class TransactionMethodSchema(Schema):
    # 欄位定義
    method_id = fields.Int(dump_only=True)  # 僅用於輸出
    method_name = fields.Str(required=True, validate=validate.Length(min=1, max=100))  # 方法名稱，必填，長度限制

    class Meta:
        fields = ('method_id', 'method_name')  # 指定要處理的欄位
        ordered = True  # 保持欄位順序