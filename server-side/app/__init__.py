from flask import Flask, jsonify, send_from_directory, render_template, request
from apispec.ext.marshmallow import MarshmallowPlugin
# from apispec_webframeworks.flask import FlaskPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from .schemas import UserSchema, AuthSchema, TestClass, TestSchema
from flask_apispec import use_kwargs, marshal_with
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
from .config import Config
#from app.model import *
from datetime import datetime
import logging
import threading


app = Flask(__name__,
            static_folder="./static/dist",
            template_folder="./static")

app.config.from_object(Config)
app.config.from_object(__name__)

CORS(app)

client = app.test_client()

engine = create_engine('sqlite:///db.sqlite')
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

blacklist = set()

session_lock = threading.Lock()

Base = declarative_base()
Base.query = session.query_property()

jwt = JWTManager(app)

docs = FlaskApiSpec()

spec = APISpec(
    title='railwaytickets',
    version='v1',
    openapi_version='2.0.0',
    plugins=[MarshmallowPlugin()],
)

jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

spec.components.security_scheme("jwt", jwt_scheme)

app.config.update({
    'APISPEC_SPEC': spec,
    'APISPEC_SWAGGER_URL': '/swagger/'
})


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('log/api.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


from app.routes import test

from .routes.users.views import users
from .routes.main.views import main
from .routes.profile.views import profile

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(profile)

docs.init_app(app)
jwt.init_app(app)
