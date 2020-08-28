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


class RouteInfoSchema(Schema):
    departure_time = fields.DateTime(required=True)
    arrival_time = fields.DateTime(required=True)
    schedule_id = fields.Integer(required=True)
    dep_stop_id = fields.Integer(required=True)
    arr_stop_id = fields.Integer(required=True)
    dep_station_name = fields.String(required=True)
    arr_station_name = fields.String(required=True)
    route_name = fields.String(required=True)
    places = fields.String(required=True)
    cost = fields.String(required=True)


class RoutesSearchResponseScheema(Schema):
    are_found = fields.Boolean(required=True)
    routes = fields.List(fields.Nested(RouteInfoSchema), required=True, allow_none=True)


class SearchSchema(Schema):
    departure_province_name = fields.String(required=True)
    arrival_province_name = fields.String(required=True)
    arrival_date = fields.DateTime(required=True)


class WagonInfoSchema(Schema):
    wagon_id = fields.Integer(required=True)
    places_num = fields.Integer(required=True)
    empty_places = fields.List(fields.Integer(), required=True)


class TrainPlacesInfoSchema(Schema):
    train_id = fields.Integer(requied=True)
    wagons_info = fields.List(fields.Nested(WagonInfoSchema), required=True)


class TestClass():
    def __init__(self, str):
        self.message = str
