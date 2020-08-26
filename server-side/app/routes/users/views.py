from flask import Blueprint, jsonify
from app import logger, session, docs
from app.schemas import UserSchema, AuthSchema
from flask_apispec import use_kwargs, marshal_with
from app.model import User

users = Blueprint('users', __name__)


@users.route('/register', methods=['POST'])
@use_kwargs(UserSchema)
@marshal_with(AuthSchema)
def register(**kwargs):
    try:
        user = User(**kwargs, role='client')
        session.add(user)
        session.commit()
        token = user.get_token()
    except Exception as e:
        logger.warning(
            f'registration failed with errors: {e}')
        return {'message': str(e)}, 400
    return {'access_token': token, 'firstname': user.firstname, 'lastname': user.lastname, 'role': user.role}


@users.route('/login', methods=['POST'])
@use_kwargs(UserSchema(only=('email', 'password')))
@marshal_with(AuthSchema)
def login(**kwargs):
    try:
        user = User.authenticate(**kwargs)
        token = user.get_token()
    except Exception as e:
        logger.warning(
            f'login with email {kwargs["email"]} failed with errors: {e}')
        return {'message': str(e)}, 400

    return {'access_token': token , 'firstname': user.firstname, 'lastname': user.lastname, 'role': user.role}


docs.register(register, blueprint='users')
docs.register(login, blueprint='users')
