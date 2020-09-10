from functools import wraps
from flask import make_response
from flask_jwt_extended import get_jwt_identity
from app import session, session_lock
from app.model import User

def manager_level_access(f):
    @wraps(f)
    def decorated_f(*args, **kwargs):
        user_id = get_jwt_identity()
        user = session.query(User).get(user_id)
        if user.role != 'manager':
            return make_response({"msg": "no access to ticket deletion"},401)
        return f(*args, **kwargs)
    return decorated_f


def session_use_decorator(f):

    def decorated_f(*args,**kwargs):
        session_lock.acquire()
        f(*args,**kwargs)
        session_lock.release()
    return decorated_f
