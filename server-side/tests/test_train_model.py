from app.model import *
from app.routes.main.views import get_train_struct

def test_train(session, trains):
    db_trains = session.query(Train).all()
    assert db_trains[0].id == trains[0].id

def test_wagons(session, trains, wagons):
    db_wagons = session.query(Wagon).all()
    assert db_wagons[0].id == wagons[0].id
    assert db_wagons[0].train_id == wagons[0].train_id

def test_train_struct(session, trains, wagons):
    train_struct, wagon_types = get_train_struct(trains[0].id)
    db_wagons = session.query(Wagon).filter(Wagon.train_id == trains[0].id).all()
    assert len(db_wagons) == 3
    for i in range(len(db_wagons)):
        assert len(train_struct[db_wagons[i].id]) == db_wagons[i].places_count
        for y in range(db_wagons[i].places_count):
            assert train_struct[db_wagons[i].id][y] == True
