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
def get_schedules(**kwargs):
    return search_routes(**kwargs)


def search_routes(departure_province, arrival_province, arrival_time, departure_time):
    arr_pr_stations = session.query(Station.id).filter(Station.province == arrival_province).all()
    dep_pr_stations = session.query(Station.id).filter(Station.province == departure_province).all()
    dep_st_alias = aliased(Stop, name='dep_st_alias')
    arr_st_alias = aliased(Stop, name='arr_st_alias')
    routes_info = session.query(dep_st_alias, arr_st_alias). \
        filter(dep_st_alias.station_id in arr_pr_stations, arr_st_alias.station_id in dep_pr_stations,
               dep_st_alias.route_id == arr_st_alias.route_id,dep_st_alias.id < arr_st_alias.id).\
        join(BaseRoute).filter(BaseRoute.id == dep_st_alias.route_id ,BaseRoute.id ==  arr_st_alias.route_id )
    return routes_info

docs.register(pingf_pong, blueprint='main')
