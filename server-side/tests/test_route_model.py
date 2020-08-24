from app.model import *

def test_stations(stations, session):
    db_stations = session.query(Station).all()
    assert db_stations[0].province == "Рязанская область"
    assert db_stations[0].id == stations[0].id


def test_route(baseroute, stations, session):
    db_route = session.query(BaseRoute).get(1)
    db_stops = session.query(Stop).all()
    assert db_route.Name == baseroute[0].Name
    assert db_stops[0].route_id == baseroute[1][0].route_id
    assert db_stops[0].departure == baseroute[1][0].departure


def test_schedule(schedule,session, train,baseroute):
    db_schedules = session.query(Schedule).all()
    assert len(db_schedules) == 1
    assert db_schedules[0].departure_time == baseroute[1][0].departure
    assert db_schedules[0].base_route_id == baseroute[0].id
    assert db_schedules[0].train_id == train.id




