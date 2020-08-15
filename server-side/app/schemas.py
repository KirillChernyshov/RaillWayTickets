from marshmallow import Schema, validate, fields

class TestSchema(Schema):
    message = fields.String(dump_only=True)

class TestClass():
    def __init__(self, str):
        self.message = str
