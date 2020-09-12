from flask import render_template, Blueprint, jsonify, Flask, send_from_directory, make_response
from app import logger, docs, session
from flask_apispec.annotations import doc
from sqlalchemy.orm import aliased
from flask_apispec import use_kwargs, marshal_with
from app.schemas import *
from app.model import *
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from .route_search import *
from app.decorators import manager_level_access

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # тут просто пробрасываем файлик, без всякого препроцессинга
    print("hi")
    return render_template("index.html")


@main.route('/dist/<path:path>')
def static_dist(path):
    # тут пробрасываем статику
    return send_from_directory("static/dist", path)


@main.route('/pang', methods=['GET'])
@marshal_with(TestSchema)
def pingf_pong():
    teststr = TestClass('pung!')
    return teststr


@main.route('/cities', methods=['GET'])
@marshal_with(CitiesListSchema(many=True))
def get_cities():
    cities = session.query(Station.province).group_by(Station.province).all()
    return [{'city_name': city[0]} for city in cities]


@main.route('/search', methods=['POST'])
@use_kwargs(RouteSearchSchema)
@marshal_with(RoutesSearchResponseSchema)
def get_schedules(**kwargs):
    routes_info = get_all_routes(kwargs.get("departure_province_name"), kwargs.get("arrival_province_name"),
                                 kwargs.get("arrival_date"))
    routes = get_fit_routes(routes_info.all())
    if (len(routes)):
        return {'are_found': True, 'routes': routes}
    else:
        return {'are_found': False}


@main.route('/get_route_info', methods=['POST'])
@doc(tag=['pet'], description='get empty seats on a train for a fragment of the schedule')
@use_kwargs(RouteInfoSchema(only=['schedule_id', 'dep_stop_id', 'arr_stop_id']))
@marshal_with(TrainSeatsResponse)
def get_empty_places(**kwargs):
    schedule = session.query(Schedule).get(kwargs.get('schedule_id'))
    print(kwargs.get('schedule_id'))
    arrival_stop = session.query(Stop).get(kwargs.get('dep_stop_id'))
    print(kwargs.get('dep_stop_id'))
    departure_stop = session.query(Stop).get(kwargs.get('arr_stop_id'))
    print(kwargs.get('arr_stop_id'))
    return get_detailed_seats_info(schedule, arrival_stop, departure_stop)


@main.route('/book_ticket', methods=['POST'])
@doc(tag=['pet'], description='for booking a ticket')
@jwt_required
@use_kwargs(TicketBookingSchema(exclude=["buyer_email"]))
@marshal_with(StatusMessageSchema)
def book_ticket(**kwargs):
    user_id = get_jwt_identity()
    now_time = datetime.now()
    train_dep_time = session.query(Schedule).get(kwargs.get('schedule_id')).departure_time
    late_booking_limit = train_dep_time - timedelta(days=4)
    # late_booking_limit = train_dep_time - timedelta(days=4)
    if (late_booking_limit < now_time):
        print(train_dep_time)
        print(now_time)
        return make_response({'msg': 'can no longer book tickets for this train.'}, 409)
    early_booking_limit = now_time + timedelta(days=30)
    book_end_date = min(early_booking_limit, late_booking_limit)
    print(book_end_date)
    print(kwargs.get('place'))
    ticket = Ticket(user_id=user_id, book_end_date=book_end_date, **kwargs)
    try:
        session.add(ticket)
        session.commit()
    except Exception as e:
        session.rollback()
        logger.warning(
            f'ticket booking failed with errors: {e}')
        return {'message': str(e)}, 400
    return make_response({'msg': 'ticket succesfully booked'}, 200)

@main.route('/place_ticket', methods=['POST'])
@doc(tag=['pet'], description='for booking a ticket')
@jwt_required
@manager_level_access
@use_kwargs(TicketBookingSchema)
@marshal_with(StatusMessageSchema)
def place_ticket(**kwargs):
    if kwargs.get('buyer_email') is None:
        user_id = None
    else:
        user = session.query(User).filter(User.email == kwargs.get('buyer_email')).one_or_none()
        if user is None:
            return {'msg': "no user with this email"}, 400
        user_id = user.id
    ticket = Ticket(user_id=user_id, **kwargs)
    try:
        session.add(ticket)
        session.commit()
    except Exception as e:
        session.rollback()
        logger.warning(
            f'ticket booking failed with errors: {e}')
        return {'msg': str(e)}, 400
    return make_response({'msg': 'ticket succesfully booked'}, 200)


@main.errorhandler(422)
def handle_error(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid Request.'])
    logger.warning(f'Invalid input params: {messages}')
    if headers:
        return jsonify({'message': messages}), 400, headers
    else:
        return jsonify({'message': messages}), 400


docs.register(get_schedules, blueprint="main")
docs.register(place_ticket, blueprint="main")
docs.register(book_ticket, blueprint='main')
docs.register(get_empty_places, blueprint='main')
docs.register(get_cities, blueprint='main')


def get_fit_routes(routes_info):
    routes = []
    for i in range(len(routes_info)):
        train_struc, wagon_types = get_seats_info(routes_info[i][0], routes_info[i][2], routes_info[i][1])
        seats_info = get_empty_train_seats_info(train_struc, wagon_types)
        if seats_info != {}:
            routes.append(serialize_fit_route(routes_info[i], seats_info))
    return routes


def serialize_fit_route(route_info, seats_info):
    arr_station_name = session.query(Station).get(route_info[2].station_id).name
    dep_station_name = session.query(Station).get(route_info[1].station_id).name
    route_name = session.query(BaseRoute).get(route_info.Schedule.base_route_id).name
    route_info_dict = {'departure_time': route_info[1].departure, 'arrival_time': route_info[2].arriving,
                       'schedule_id': route_info[0].id, 'dep_stop_id': route_info[1].station_id,
                       'arr_stop_id': route_info[2].station_id, 'arr_station_name': arr_station_name,
                       'dep_station_name': dep_station_name, 'route_name': route_name, 'seats_info': []}
    for type_name, type_info in seats_info.items():
        route_info_dict['seats_info'].append({'type_name': type_name, 'num_of_places': type_info['num_of_places'],
                                              'cost': type_info['cost']})
    return route_info_dict


def serialize_seats_info(wagons_stat, schedule, arr_stop, dep_stop):
    empty_seats_info = []
    for wagon_num, wagon_places in wagons_stat.items():
        wagon_info = wagon_places
        wagon_info.update({'wagon_num': wagon_num})
        empty_seats_info.append(wagon_info)
    arr_station_name = session.query(Station.name).filter(Station.id == arr_stop.station_id).one_or_none()
    dep_station_name = session.query(Station.name).filter(Station.id == dep_stop.station_id).one_or_none()
    route_name = session.query(BaseRoute.name).one_or_none()
    train_id = session.query(Train).get(schedule.train_id).id
    route_info_dict = {'train_id':schedule.train_id,'wagon_seats_info': empty_seats_info}
    return route_info_dict


type_factors = {'Купе': 1.1, 'Плацкартовый': 0.75}


def get_detailed_seats_info(schedule, arr_stop, dep_stop):
    train_struc, wagon_types = get_seats_info(schedule, arr_stop, dep_stop)
    wagons_stat = get_wagons_info(train_struc, wagon_types)
    return serialize_seats_info(wagons_stat, schedule, arr_stop, dep_stop)


def get_seats_info(schedule, arr_stop, dep_stop):
    train_struc, wagon_types = get_train_struct(schedule.train_id)
    mark_booked_seats(train_struc, schedule, arr_stop, dep_stop)
    places_stat = get_empty_train_seats_info(train_struc, wagon_types)
    return train_struc, wagon_types


def get_train_struct(train_id):
    wagons = session.query(Wagon).filter(Wagon.train_id == train_id).all()
    train_struct = {}
    wagon_types = {}
    for wagon in wagons:
        places = [True] * wagon.places_count
        train_struct[wagon.id] = places
        wagon_types[wagon.id] = wagon.type
    return train_struct, wagon_types


def get_tickets(schedule_id):
    tickets = session.query(Ticket).filter(Ticket.schedule_id)
    return tickets


def mark_booked_seats(train_struc, schedule, arr_stop, dep_stop):
    tickets = get_tickets(schedule.id)
    for ticket in tickets:
        if (((ticket.departure_stop < dep_stop.id) == (ticket.arrival_stop > arr_stop.id)) |
                ((ticket.departure_stop < dep_stop.id) & (ticket.arrival_stop > dep_stop.id)) |
                ((ticket.departure_stop < arr_stop.id) & (ticket.arrival_stop > arr_stop.id))):
            train_struc[ticket.wagon_id][ticket.place_num - 1] = False


def get_wagons_info(train_struc, wagon_types):
    ride_cost = 4
    wagons_stat = {}
    for wagon_id, wagon_places in train_struc.items():
        if wagons_stat.get(wagon_id) is None:
            wagons_stat[wagon_id] = \
                {'type_name': wagon_types[wagon_id], 'empty_places': [],
                 'cost': ride_cost * type_factors[wagon_types[wagon_id]]}
        for place_num in range(len(wagon_places)):
            if wagon_places[place_num]:
                wagons_stat[wagon_id]['empty_places'].append(place_num + 1)
        blacklist = []
        for wagon_num, wagon_stat in wagons_stat.items():
            if len(wagon_stat['empty_places']) == 0:
                blacklist.append(wagon_num)
        for wagon_num in blacklist:
            wagons_stat.pop(wagon_num)
    return wagons_stat


def get_empty_train_seats_info(train_struc, wagon_types):
    places_stat = {}
    ride_cost = 4
    for wagon_id, wagon_places in train_struc.items():
        if places_stat.get(wagon_types[wagon_id]) is None:
            places_stat[wagon_types[wagon_id]] = \
                {'num_of_places': 0, 'cost': ride_cost * type_factors[wagon_types[wagon_id]]}
        for place_num in range(len(wagon_places)):
            if wagon_places[place_num]:
                places_stat[wagon_types[wagon_id]]['num_of_places'] += 1
    blacklist = []
    for type_name, type_stat in places_stat.items():
        if type_stat['num_of_places'] == 0:
            blacklist.append(type_name)
    for type_name in blacklist:
        places_stat.pop(type_name)
    return places_stat
