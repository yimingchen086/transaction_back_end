from marshmallow import Schema, fields
from marshmallow import Schema, fields, validate
from datetime import datetime

class TransactionSchema(Schema):
    transaction_id = fields.Int(
        dump_only=True,
        description="交易記錄的唯一識別碼（自動生成）"
    )
    transaction_method_id = fields.Int(
        required=True,
        description="交易方式的ID"
    )
    transaction_title = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=50),
        description="交易標題（最多50個字符）"
    )
    amount = fields.Decimal(
        required=True,
        places=2,  # 保留兩位小數
        description="交易金額（兩位小數）"
    )
    category_id = fields.Int(
        required=True,
        description="交易類別的ID"
    )
    transaction_time = fields.DateTime(
        format='%Y-%m-%dT%H:%M:%S%z',
        allow_none=True,
        description="交易發生的時間（ISO 8601 格式）"
    )
    create_time = fields.DateTime(
        dump_only=True,  # 僅用於序列化，由資料庫生成
        description="記錄創建的時間（ISO 8601 格式）"
    )
    card_id = fields.Int(
        required=True,
        description="信用卡資料的ID"
    )
    actual_amount = fields.Integer(
        required=False,
        description='實際金額'
    )


    # 外鍵關係的嵌套序列化（可選）
    transaction_method = fields.Nested('TransactionMethodSchema', only=('method_id', 'method_name'), dump_only=True)
    category = fields.Nested('CategorySchema', only=('category_id', 'category_name'), dump_only=True)
    card = fields.Nested('CardInfoSchema', only=('card_id', 'card_name'), dump_only=True)

    class Meta:
        fields = (
            'transaction_id',
            'transaction_method_id',
            'transaction_title',
            'amount',
            'category_id',
            'transaction_time',
            'create_time',
            'card_id',
            'transaction_method',
            'category',
            'card',
            'actual_amount'
        )
        ordered = True  # 保持欄位順序