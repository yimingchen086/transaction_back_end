from marshmallow import Schema, fields

class RecentTransactionsQuerySchema(Schema):
    take = fields.Int(missing=10, description="要獲取的交易筆數")