from flask import Flask, jsonify, send_from_directory, render_template, request
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import  FlaskApiSpec
from .schemas import *
from flask_apispec import use_kwargs, marshal_with
from flask_cors import CORS

app = Flask(__name__,
            static_folder="./static/dist",
            template_folder="./static")
app.config.from_object(__name__)

CORS(app)

client = app.test_client()

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



from app.routes import test


docs.register(pingf_pong)
