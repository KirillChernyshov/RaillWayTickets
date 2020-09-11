from flask import render_template, Blueprint, jsonify, Flask, send_from_directory, make_response
from app import logger, docs, session
from sqlalchemy.orm import aliased
from flask_apispec import use_kwargs, marshal_with
from flask_apispec.annotations import doc
from app.schemas import *
from app.model import *
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.base_view import BaseView
from app.decorators import manager_level_access, check_access
from operator import xor

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
            tickets = session.query(Ticket).filter(Ticket.user_id == user.id).all()
        except Exception as e:
            logger.warning(
                f'user:{user_id} - failed to read profile: {e}')
            return {'message': str(e)}, 400
        return UsersTickets.prepare_to_serialize(tickets)

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
            ticket_dict = {'ticket_id': ticket.id,
                           'route_name': route.name,
                           'dep_station_name': dep_station.fullname(),
                           'arr_station_name': arr_station.fullname(),
                           'departure_time': dep_station_stop.departure,
                           'arrival_time': arr_station_stop.arriving,
                           'wagon_id': ticket.wagon_id,
                           'place': ticket.place_num,
                           'cost': ticket.cost,
                           'is_booked': ticket.is_booked,
                           'booking_end_date': ticket.book_end_date}
            ticket_data.append(ticket_dict)
        return ticket_data


# class
@profile.route('/search_tickets', methods=['POST'])
@doc(tag=['pet'], description='desc')
@jwt_required
@manager_level_access
@use_kwargs(TicketSearchSchema)
@marshal_with(TicketInfoSchema(many=True))
def search_tickets(**kwargs):
    manager_id = get_jwt_identity()
    tickets = get_tickets(**kwargs)
    logger.info(f'manager {manager_id}  accessed tickets list')
    return UsersTickets.prepare_to_serialize(tickets)


@profile.route('/delete_ticket', methods=['POST'])
@doc(tag=['pet'], description='desc')
@jwt_required
@use_kwargs(TicketInfoSchema(only=['ticket_id']))
@marshal_with(StatusMessageSchema)
def delete_ticket(**kwargs):
    user_id = get_jwt_identity()
    try:
        role = check_access()
        ticket = session.query(Ticket).get(kwargs.get('ticket_id'))
        if ((not ticket.is_booked) & ( role == "manager")) |\
                (ticket.is_booked & ((ticket.user_id == user_id) | (role == "manager"))):
            session.delete(ticket)
            session.commit()
        else:
            return{'msg': "not allowed to delete the ticket" }, 401
    except Exception as e:
        session.rollback()
        logger.warning(
            f'user: {user_id} - failed to delete ticket: {e}')
        return {'message': str(e)}, 400
    logger.info(f'user {user_id} deleted ticket')
    return {"msg": "Successfully deleted ticket"}, 200


@profile.route('/verify_ticket', methods=['POST'])
@doc(tag=['pet'], description='desc')
@jwt_required
@manager_level_access
@use_kwargs(TicketInfoSchema(only=['ticket_id']))
@marshal_with(StatusMessageSchema)
def verify_ticket(**kwargs):
    manager_id = get_jwt_identity()
    try:
        ticket_id = kwargs.get('ticket_id')
        kwargs.get('ticket_id')
        session.query(Ticket).filter(Ticket.id == ticket_id). \
            update({'is_booked': False, 'book_end_date': None}, synchronize_session='evaluate')
        logger.info(f'manager {manager_id} verified ticket {ticket_id}')
    except Exception as e:
        logger.warning(
            f'manager: {manager_id} - failed to verify ticket: {e}')
        return {'message': str(e)}, 400
    return {"msg": "Successfully verified ticket"}, 200


docs.register(verify_ticket, blueprint='profile')
docs.register(delete_ticket, blueprint='profile')
docs.register(search_tickets, blueprint='profile')
UserInfoView.register(profile, docs, '/profile', 'userinfoview')
UsersTickets.register(profile, docs, '/user_tickets', 'userstickets')


def get_tickets(**kwargs):
    if (kwargs.get('usr_email') is not None):
        return session.query(Ticket).join(User, User.id == Ticket.user_id). \
            filter(User.email == kwargs.get('usr_email')).all()
    if (kwargs.get('ticket_id') is not None):
        return [session.query(Ticket).get(kwargs.get('ticket_id'))]
    return []
