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
        name='testnick',
        email='testmail@mail.com',
        password='passw',
        role='idiot'
    )
    session.add(user)
    session.commit()

    return user

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
def user_headers(user_token):
    headers = {
        'Authorization': f'Bearer {user_token}'
    }

    return headers

@pytest.fixture
def stations(session):
    stationsi = [Station(name="лубянка-1", province="Рязанская область"),
                 Station(name="искра-1", province="Рязанская область"),
                 Station(name="боровое-1", province="Рязанская область")]
    session.add_all(stationsi)
    session.commit()
    return stationsi

@pytest.fixture
def baseroute(session, stations):
    route = BaseRoute(Name="Рязань Лубянка - Искра")
    stops = [Stop(station_id = stations[0].id, route_id= route.id, departure = datetime(2020,10,1,0,0)),
             Stop(station_id=stations[1].id, route_id=route.id,
                  arriving=datetime(2020, 10, 1, 2, 0), departure=datetime(2020, 10, 1, 2, 5)),
             Stop(station_id=stations[2].id, route_id=route.id,
                  arriving=datetime(2020, 10, 1, 4, 0))]
    session.add(route)
    session.add_all(stops)
    session.commit()
    return route, stops

@pytest.fixture
def train(session):
    train = Train()
    session.add(train)
    session.commit()
    return train

@pytest.fixture
def wagons(train, session):
    wagons = [Wagon(train_id = train.id, type = 'type-1', places_count=50),
              Wagon(train_id=train.id, type='type-2', places_count=40),
              Wagon(train_id=train.id, type='type-3', places_count=20)]
    session.add_all(wagons)
    session.commit()
    return wagons

@pytest.fixture
def schedule(session, train, baseroute):
    schedule = Schedule(train_id = train.id, base_route_id = baseroute[0].id, departure_time = baseroute[1][0].departure)
    session.add(schedule)
    session.commit()
    return schedule
