from flask import render_template, Blueprint, jsonify, Flask, send_from_directory
from app import logger, docs, session
from sqlalchemy.orm import aliased
from flask_apispec import use_kwargs, marshal_with
from app.schemas import *
from app.model import *
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

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


@main.route('/search', methods=['GET'])
@use_kwargs(SearchSchema)
@marshal_with(RoutesSearchResponseScheema)
def get_schedules(**kwargs):
    routes_info = get_all_routes(kwargs.get("departure_province_name"), kwargs.get("arrival_province_name"),
                                 kwargs.get("arrival_date"))
    routes = get_fit_routes(routes_info.all())
    if (len(routes)):
        return {'are_found': True, 'routes': routes}
    else:
        return {'are_found': False}


def get_fit_routes(routes_info):
    routes = []
    for i in range(len(routes_info)):
        places = get_places(routes_info[i][0], routes_info[i][2], routes_info[i][1])
        if places != 0:
            routes.append(serialize_fit_route(routes_info[0], places))
    return routes


def serialize_fit_route(route_info, places):
    arr_station_name = session.query(Station.name).filter(Station.id == route_info[2].station_id).one_or_none()
    dep_station_name = session.query(Station.name).filter(Station.id == route_info[1].station_id).one_or_none()
    route_name = session.query(BaseRoute.Name).one_or_none()
    return {'departure_time': route_info[1].departure,
            'arrival_time': route_info[2].arriving,
            'schedule_id': route_info[0].id, 'dep_stop_id': route_info[1].station_id,
            'arr_stop_id': route_info[2].station_id, 'arr_station_name': arr_station_name,
            'dep_station_name': dep_station_name, 'route_name': route_name, 'places': places, 'cost': 101}


def get_all_routes(departure_province, arrival_province, arrival_time):
    # departure_province = "Рязанская область"
    # arrival_province = "Мордовия"
    # arrival_time = datetime(2020, 10, 1, 4, 0)
    dep_stop = aliased(Stop, name='dep_stop')
    arr_stop = aliased(Stop, name='arr_stop')
    dep_station = aliased(Station, name='dep_station')
    arr_station = aliased(Station, name='arr_station')
    routes_info = session.query(Schedule, dep_stop, arr_stop). \
        join(dep_stop, dep_stop.route_id == Schedule.base_route_id). \
        join(dep_station, dep_station.id == dep_stop.station_id).filter(dep_station.province == departure_province). \
        join(arr_stop, arr_stop.route_id == Schedule.base_route_id). \
        filter(arr_stop.id > dep_stop.id, arr_stop.arriving < arrival_time). \
        join(arr_station, arr_station.id == arr_stop.station_id).filter(arr_station.province == arrival_province)
    return routes_info


def get_places(schedule, arr_stop, dep_stop):
    train_struc, wagon_types = get_train_struct(schedule.train_id)
    tickets = get_tickets(schedule.id)
    for ticket in tickets:
        if (((ticket.departure_stop < dep_stop.id) == (ticket.arrival_stop > arr_stop.id)) |
                ((ticket.departure_stop < dep_stop.id) & (ticket.arrival_stop > dep_stop.id)) |
                ((ticket.departure_stop < arr_stop.id) & (ticket.arrival_stop > arr_stop.id))):
            train_struc[ticket.wagon_id][ticket.place_num] = False
    empty_places = 0
    places = list(train_struc.values())
    for i in range(len(places)):
        for y in range(len(places[i])):
            if places[i][y]:
                empty_places += 1
    # arr_station = session.query(Station.name).fliter(Station.id == arr_stop.station_id)
    #     dep_station = session.query(Station.name).filter(Station.id == dep_stop.station_id)
    #     route_name = session.query
    #     routings.append([schedule.id, arr_station, dep_station,arr_stop.arriving, dep_stop.departure])
    return empty_places


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


def get_places_plan(wagon_id, schedule, arr_stop, dep_stop):
    train_struc = get_train_struct(schedule.train_id)
    tickets = get_tickets(schedule.id)
    for ticket in tickets:
        if (((ticket.departure_stop < dep_stop.id) == (ticket.arrival_stop > arr_stop.id)) |
                ((ticket.departure_stop < dep_stop.id) & (ticket.arrival_stop > dep_stop.id)) |
                ((ticket.departure_stop < arr_stop.id) & (ticket.arrival_stop > arr_stop.id))):
            train_struc[ticket.wagon_id][ticket.place_num] = False
    return train_struc


docs.register(get_schedules, blueprint="main")
docs.register(pingf_pong, blueprint='main')
