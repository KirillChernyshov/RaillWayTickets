from marshmallow import Schema, validate, fields

class TestSchema(Schema):
    message = fields.String(dump_only=True)


class UserSchema(Schema):
    name = fields.String(required=True, validate=[
        validate.Length(max=250)])
    surname = fields.String(required = True,
                            validate=[validate.Length(max=250)])
    email = fields.String(required=True, validate=[
        validate.Length(max=250)])
    password = fields.String(required=True, validate=[
        validate.Length(max=100)], load_only=True)

class AuthSchema(Schema):
    access_token = fields.String(dump_only=True)
    message = fields.String(dump_only=True)




class TestClass():
    def __init__(self, str):
        self.message = str


