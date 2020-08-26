from app import db, session, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import bcrypt


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)

    def __init__(self, **kwargs):
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.email = kwargs.get('email')
        self.role = kwargs.get('role')
        self.password = bcrypt.hash(kwargs.get('password'))

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta)
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not bcrypt.verify(password, user.password):
            raise Exception('No user with this password')
        return user


class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True)
    departure_time = Column(DateTime, nullable=False)
    base_route_id = Column(Integer, ForeignKey('routes.id'))
    train_id = Column(Integer, ForeignKey('trains.id'))


class BaseRoute(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=True)
    schedules = relationship('Schedule', backref='base_route', lazy=True)


class Train(Base):
    __tablename__ = "trains"
    id = Column(Integer, primary_key=True)
    schedules = relationship('Schedule', backref='train', lazy=True)
    wagons = relationship('Wagon', backref='train', lazy=True)


class Wagon(Base):
    __tablename__ = "wagons"
    id = Column(Integer, primary_key=True)
    train_id = Column(Integer, ForeignKey('trains.id'))
    type = Column(String(50), nullable=False)
    places_count = Column(Integer, nullable=False)


class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)


class Stop(Base):
    __tablename__ = "stops"
    id = Column(Integer, primary_key=True)
    station_id = Column(Integer, ForeignKey('stations.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))
    arriving = Column(DateTime, nullable=True)
    departure = Column(DateTime, nullable=True)


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    departure_stop = Column(Integer, ForeignKey('stops.id'))
    arrival_stop = Column(Integer, ForeignKey('stops.id'))
    cost = Column(Integer, nullable=False)
    wagon_id = Column(Integer, ForeignKey('wagons.id'), nullable=False)
    place_num = Column(Integer, nullable=False)
    is_booked = Column(Boolean, nullable=False)
    book_end_date = Column(DateTime, nullable=False)
