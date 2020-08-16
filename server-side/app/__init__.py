from flask import Flask, jsonify, send_from_directory, render_template, request
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import  FlaskApiSpec
from .schemas import *
from flask_apispec import use_kwargs, marshal_with
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from .config import Config


app = Flask(__name__,
            static_folder="./static/dist",
            template_folder="./static")
app.config.from_object(Config)
client = app.test_client()

engine = create_engine('sqlite:///db.sqlite')
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

jwt = JWTManager(app)

docs = FlaskApiSpec()
docs.init_app(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='videoblog',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})

from .model import *

Base.metadata.create_all(bind=engine)




@app.route('/')
def index():
    # тут просто пробрасываем файлик, без всякого препроцессинга
    print("hi")
    return render_template("index.html")


@app.route('/dist/<path:path>')
def static_dist(path):
    # тут пробрасываем статику
    return send_from_directory("static/dist", path)


@app.route('/pang', methods=['GET'])
@marshal_with(TestSchema())
def pingf_pong():
    teststr = TestClass('pung!')
    return teststr

@app.route('/register', methods=['POST'])
def register():
    params = request.json
    user = User(**params)
    session.add(user)
    session.commit()
    token = user.get_token()
    return {'access_token': token}


@app.route('/login', methods=['POST'])
def login():
    params = request.json
    user = User.authenticate(**params)
    token = user.get_token()
    return {'access_token': token}



@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


from app.routes import test


docs.register(pingf_pong)
docs.register(register)
docs.register(login)

