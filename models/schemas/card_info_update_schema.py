from marshmallow import Schema, fields


class CardInfoUpdateSchema(Schema):
    card_name = fields.String()
    bank = fields.String()
    maxconsume = fields.Integer()
    description = fields.String(allow_none=True)
    store = fields.String(allow_none=True)
    rewardstype = fields.String(allow_none=True)
    daterange_start = fields.Date(allow_none=True)
    daterange_end = fields.Date(allow_none=True)
    postingdate = fields.String(allow_none=True)
