from marshmallow import Schema, fields


class CardInfoSchema(Schema):
    card_id = fields.Int(dump_only=True)  # 確保 ID 會被序列化，但不會被當成輸入
    card_name = fields.Str(required=True, validate=lambda x: len(x) <= 50)
    bank = fields.Str(required=True, validate=lambda x: len(x) <= 50)
    maxconsume = fields.Int(allow_none=True)
    description = fields.Str(allow_none=True)
    store = fields.Str(allow_none=True)
    rewardstype = fields.Str(allow_none=True)
    daterange_start = fields.Date(allow_none=True)
    daterange_end = fields.Date(allow_none=True)
    postingdate = fields.Str(allow_none=True)