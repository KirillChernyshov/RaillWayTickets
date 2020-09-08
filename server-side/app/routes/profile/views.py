from flask import render_template, Blueprint, jsonify, Flask, send_from_directory
from app import logger, docs, session
from sqlalchemy.orm import aliased
from flask_apispec import use_kwargs, marshal_with
from flask_apispec.annotations import doc
from app.schemas import *
from app.model import *
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.base_view import BaseView

profile = Blueprint('profile', __name__)


class UserInfoView(BaseView):
    @jwt_required
    @marshal_with(UserSchema)
    def get(self):
        user_id = get_jwt_identity()
        try:
            user = User.query.get(user_id)
            if not user:
                raise Exception('User not found')
        except Exception as e:
            logger.warning(
                f'user:{user_id} - failed to read profile: {e}')
            return {'message': str(e)}, 400
        return user


class UsersTickets(BaseView):
    @doc(tag=['pet'], description='get tcikets of a user')
    @jwt_required
    @marshal_with(TicketInfoSchema(many=True))
    def get(self):
        user_id = get_jwt_identity()
        try:
            user = User.query.get(user_id)
            if not user:
                raise Exception('User not found')
            tickets = session.query(Ticket).filter(Ticket.user_id==user.id).all()
        except Exception as e:
            logger.warning(
                f'user:{user_id} - failed to read profile: {e}')
            return {'message': str(e)}, 400
        return UsersTickets.prepare_to_serialize(tickets)

    @jwt_required
    @doc(tag=['pet'], description='desc')
    def post(self):
        pass

    @classmethod
    def prepare_to_serialize(self, tickets):
        ticket_data = []
        for ticket in tickets:
            schedule = Schedule.query.get(ticket.schedule_id)
            route = BaseRoute.query.get(schedule.base_route_id)
            dep_station_stop = Stop.query.get(ticket.departure_stop)
            arr_station_stop = Stop.query.get(ticket.arrival_stop)
            dep_station = Station.query.get(dep_station_stop.station_id)
            arr_station = Station.query.get(arr_station_stop.station_id)
            ticket_data.append({'ticket_id': ticket.id,
                                'route_name': route.name,
                                'dep_station_name': dep_station.fullname(),
                                'arr_station_name': arr_station.fullname(),
                                'departure_time': dep_station_stop.departure,
                                'arrival_time': arr_station_stop.arriving,
                                'wagon_id': ticket.wagon_id,
                                'place': ticket.place_num,
                                'cost': ticket.cost})
        return ticket_data

#class


UserInfoView.register(profile, docs, '/profile', 'userinfoview')
UsersTickets.register(profile, docs, '/user_tickets', 'userstickets')

