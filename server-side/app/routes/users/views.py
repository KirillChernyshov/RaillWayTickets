from flask import Blueprint, jsonify
from app import logger, session, docs, blacklist
from app.schemas import UserSchema, AuthSchema, StatusMessageSchema
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity, get_raw_jwt
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

@users.route('/logout', methods=['DELETE'])
@jwt_required
@marshal_with(StatusMessageSchema)
def logout():
    try:
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
    except Exception as e:
        logger.warning(
            f'logout failed with errors: {e}')
        return {'message': str(e)}, 400
    return {"msg": "Successfully logged out"}, 200

@users.errorhandler(422)
def handle_error(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid Request.'])
    logger.warning(f'Invalid input params: {messages}')
    if headers:
        return jsonify({'message': messages}), 400, headers
    else:
        return jsonify({'message': messages}), 400

docs.register(logout, blueprint='users')
docs.register(register, blueprint='users')
docs.register(login, blueprint='users')

