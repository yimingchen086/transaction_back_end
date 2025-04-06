from marshmallow import Schema, fields

class LoginGoogleSchema(Schema):
    token = fields.Str(required=True)

class GoogleUserSchema(Schema):
    sub = fields.String(description="The unique user ID from Google", required=True)
    email = fields.String(description="The user's email", required=True)
    name = fields.String(description="The user's name", required=False)
    picture = fields.String(description="The user's profile picture", required=False)