import pytest
import sys
from datetime import datetime, date, time

sys.path.append('..')

from app import app, Base, engine, session as db_session
from app.model import *


@pytest.yield_fixture(scope='function')
def testapp():
    _app = app

    Base.metadata.create_all(bind=engine)
    _app.connection = engine.connect()

    yield app

    Base.metadata.drop_all(bind=engine)
    _app.connection.close()


@pytest.fixture()
def session(testapp):
    ctx = app.app_context()
    ctx.push()

    yield db_session

    db_session.close_all()
    ctx.pop()


@pytest.fixture(scope='function')
def user(session):
    user = User(
        firstname='testn',
        lastname='testsg',
        email='testmail@mail.com',
        password='passw',
        role='client'
    )
    session.add(user)
    session.commit()

    return user

@pytest.fixture
def manager(session):
    manager = User(firstname='testmng', lastname='testmng',
                   email='mngemail@mail.com', password='mngpassw', role='manager')
    session.add(manager)
    session.commit()

    return manager


@pytest.fixture
def client(testapp):
    return testapp.test_client()


@pytest.fixture
def user_token(user, client):
    res = client.post('/login', json={
        'email': user.email,
        'password': 'passw'
    })
    return res.get_json()['access_token']

@pytest.fixture
def manager_token(manager,client):
    res = client.post('/login', json={
        'email': manager.email,
        'password': 'mngpassw'
    })
    return res.get_json()['access_token']


@pytest.fixture
def user_headers(user_token):
    headers = {
        'Authorization': f'Bearer {user_token}'
    }
    return headers


@pytest.fixture
def stations(session):
    stations = [Station(name="лубянка-1", province="Рязанская область"),
                Station(name="искра-1", province="Рязанская область"),
                Station(name="боровое-1", province="Рязанская область"),
                Station(name="Ковылкиноб", province="Мордовия")]
    session.add_all(stations)
    session.commit()
    return stations


@pytest.fixture
def routes(session, stations):
    routes = [BaseRoute(name="Рязань - Мордовия")]
    session.add_all(routes)
    session.commit()
    return routes


@pytest.fixture
def stops(session, stations, routes):
    stops = [Stop(station_id=stations[0].id, route_id=routes[0].id, departure=datetime(2020, 10, 1, 0, 0)),
             Stop(station_id=stations[1].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 2, 0), departure=datetime(2020, 10, 1, 2, 5)),
             Stop(station_id=stations[2].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 4, 0)),
             Stop(station_id=stations[3].id, route_id=routes[0].id,
                  arriving=datetime(2020, 10, 1, 7, 0))]
    session.add_all(stops)
    session.commit()
    return stops


@pytest.fixture
def trains(session):
    trains = [Train()]
    session.add_all(trains)
    session.commit()
    return trains


@pytest.fixture
def wagons(trains, session):
    wagons = [Wagon(train_id=trains[0].id, type='Купе', places_count=5),
              Wagon(train_id=trains[0].id, type='Плацкартовый', places_count=4),
              Wagon(train_id=trains[0].id, type='Купе', places_count=2)]
    session.add_all(wagons)
    session.commit()
    return wagons


@pytest.fixture
def schedules(session, trains, routes, stops):
    schedules = [Schedule(train_id=trains[0].id, base_route_id=routes[0].id, departure_time=stops[0].departure)]
    session.add_all(schedules)
    session.commit()
    return schedules


@pytest.fixture
def tickets(session, trains, routes, stops, schedules, wagons, user):
    tickets = [Ticket(departure_stop_id=stops[2].id, arrival_stop_id=stops[3].id, cost=34, wagon_id=wagons[0].id, place=2,
                      schedule_id=schedules[0].id, is_booked=False, user_id = user.id),
               Ticket(departure_stop_id=stops[1].id, arrival_stop_id=stops[3].id, cost=34, wagon_id=wagons[1].id, place=3,
                      schedule_id=schedules[0].id, is_booked=False, user_id = user.id),
               Ticket(departure_stop_id=stops[0].id, arrival_stop_id=stops[3].id, cost=34, wagon_id=wagons[1].id, place=1,
                      schedule_id=schedules[0].id, is_booked=True, user_id=user.id, book_end_date=datetime(2020,9,25,0,0))
               ]

    session.add_all(tickets)
    session.commit()
    return tickets
