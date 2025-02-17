from marshmallow import Schema, fields


class CardInfoCreateSchema(Schema):
    card_name = fields.String(required=True)
    bank = fields.String(required=True)
    maxconsume = fields.Integer(required=False, allow_none=True)
    curramount = fields.Integer(required=False, allow_none=True)
    description = fields.String(required=False, allow_none=True)
    store = fields.String(required=False, allow_none=True)
    rewardstype = fields.String(required=False, allow_none=True)
    daterange_start = fields.Date(required=False, allow_none=True)
    daterange_end = fields.Date(required=False, allow_none=True)
    postingdate = fields.String(required=False, allow_none=True)
