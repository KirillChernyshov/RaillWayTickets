from app.model import *

def test_train(session, train):
    db_trains = session.query(Train).all()
    assert db_trains[0].id == train.id

def test_wagons(session, train, wagons):
    db_wagons = session.query(Wagon).all()
    assert db_wagons[0].id == wagons[0].id
    assert db_wagons[0].train_id == wagons[0].train_id
