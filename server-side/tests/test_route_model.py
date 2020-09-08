from app.model import *
from datetime import datetime
from app.routes.main.views import get_all_routes
from sqlalchemy.orm import aliased
from app.routes.main.views import get_all_routes, get_fit_routes


def test_stations(stations, session):
    db_stations = session.query(Station).all()
    assert db_stations[0].province == "Рязанская область"
    assert db_stations[0].id == stations[0].id


def test_route(routes, stops, session):
    db_route = session.query(BaseRoute).get(1)
    db_stops = session.query(Stop).all()
    assert db_route.Name == routes[0].name
    assert db_stops[0].route_id == stops[0].route_id
    assert db_stops[0].departure == stops[0].departure


def test_schedule(schedules, session, trains, routes, stops):
    db_schedules = session.query(Schedule).all()
    assert len(db_schedules) == 1
    assert db_schedules[0].departure_time == stops[0].departure
    assert db_schedules[0].base_route_id == routes[0].id
    assert db_schedules[0].train_id == trains[0].id


def test_route_search(client, session, schedules , tickets, trains, routes, stops, wagons, stations):
    routes_info = get_all_routes("Рязанская область", "Мордовия", datetime(2020, 10, 1, 8, 0))

    #print(routes_info)
    assert len(routes_info.all()) == 3
    assert routes_info[0][0].id == 1
    routes = get_fit_routes(routes_info.all())
    assert len(routes) == 3
    print(routes)
    result = client.get('/search', json={'departure_province_name': "Рязанская область",
                                         'arrival_province_name': "Мордовия",
                                         'arrival_date': datetime.isoformat(datetime(2020, 10, 1, 8, 0))})
    assert result.status == '200 OK'
    assert result.get_json().get('are_found')
    assert len(result.get_json().get('routes')) == 3



# , arr_stop.arriving < arrival_time
# .filter(dep_station.province == departure_province)
# .filter(arr_station.province == arrival_province)
