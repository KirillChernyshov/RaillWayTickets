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


class SeatTypeInfoSchema(Schema):
    type_name = fields.String(required=True)
    num_of_places = fields.Integer(required=True)
    cost = fields.Integer(required=True)

class WagonSeatsInfoSchema(Schema):
    wagon_num = fields.String(required=True)
    type_name = fields.String(required=True)
    empty_places = fields.List(fields.Integer,required=True)
    cost = fields.Integer(required=True)

class TrainSeatsResponse(Schema):
    wagon_seats_info = fields.List(fields.Nested(WagonSeatsInfoSchema,required=True))
    train_id = fields.Integer(required=True)


class RouteInfoSchema(Schema):
    departure_time = fields.DateTime(required=True)
    arrival_time = fields.DateTime(required=True)
    schedule_id = fields.Integer(required=True)
    dep_stop_id = fields.Integer(required=True)
    arr_stop_id = fields.Integer(required=True)
    dep_station_name = fields.String(required=True)
    arr_station_name = fields.String(required=True)
    route_name = fields.String(required=True)
    seats_info = fields.List(fields.Nested(SeatTypeInfoSchema),required=True)
    cost = fields.String(required=True)


class RoutesSearchResponseSchema(Schema):
    are_found = fields.Boolean(required=True)
    routes = fields.List(fields.Nested(RouteInfoSchema), required=True, allow_none=True)


class RouteSearchSchema(Schema):
    departure_province_name = fields.String(required=True)
    arrival_province_name = fields.String(required=True)
    arrival_date = fields.DateTime(required=True)


class WagonInfoSchema(Schema):
    wagon_id = fields.Integer(required=True)
    places_num = fields.Integer(required=True)
    empty_places = fields.List(fields.Integer(), required=True)


class TrainPlacesInfoSchema(Schema):
    train_id = fields.Integer(required=True)
    wagons_info = fields.List(fields.Nested(WagonInfoSchema), required=True)


class TicketBookingSchema(Schema):
    schedule_id = fields.Integer(required=True)
    arrival_stop_id = fields.Integer(required=True)
    departure_stop_id = fields.Integer(required=True)
    wagon_id = fields.Integer(required=True)
    place = fields.Integer(required=True)
    cost = fields.Integer(required=True)


class TicketInfoSchema(Schema):
    ticket_id = fields.Integer(required=True)
    route_name = fields.String(required=True)
    dep_station_name = fields.String(required=True)
    arr_station_name = fields.String(required=True)
    departure_time = fields.DateTime(required=True)
    arrival_time = fields.DateTime(required=True)
    wagon_id = fields.Integer(required=True)
    place = fields.Integer(required=True)
    cost = fields.String(required=True)
    is_booked = fields.Boolean(required=True)
    booking_end_date = fields.DateTime(missing=None)

class CitiesListSchema(Schema):
    city_name = fields.String(required=True)

class StatusMessageSchema(Schema):
    msg = fields.String(required=True)

class TicketSearchSchema(Schema):
    ticket_id = fields.Integer(missing=None)
    usr_email = fields.String(missing=None)






class TestClass():
    def __init__(self, str):
        self.message = str
