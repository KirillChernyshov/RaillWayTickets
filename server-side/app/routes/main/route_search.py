from sqlalchemy.orm import aliased
from app.model import *


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