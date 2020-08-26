from marshmallow import Schema, validate, fields


class TestSchema(Schema):
    message = fields.String(dump_only=True)


class UserSchema(Schema):
    firstname = fields.String(required=True, validate=[
        validate.Length(max=250)])
    lastname = fields.String(required=True,
                             validate=[validate.Length(max=250)])
    email = fields.Email(required=True, validate=[
        validate.Length(max=250)])
    password = fields.String(required=True, validate=[
        validate.Length(max=100)], load_only=True)


class AuthSchema(Schema):
    firstname = fields.String(required=True, validate=[
        validate.Length(max=250)])
    lastname = fields.String(required=True,
                             validate=[validate.Length(max=250)])
    access_token = fields.String(dump_only=True)
    message = fields.String(dump_only=True)
    role = fields.String(dump_only=True)


class SearchSchema(Schema):
    departure_province_name = fields.String(dump_only=True)
    arrival_province_name = fields.String(dump_only=True)
    arrival_date = fields.Date(dump_only=True)


class TestClass():
    def __init__(self, str):
        self.message = str
