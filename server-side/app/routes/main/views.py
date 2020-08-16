from flask import render_template, Blueprint, jsonify, Flask, send_from_directory
from app import logger, docs
from flask_apispec import use_kwargs, marshal_with
from app.schemas import TestSchema,TestClass
from flask_jwt_extended import jwt_required, get_jwt_identity


main = Blueprint('main', __name__)



@main.route('/')
def index():
    # тут просто пробрасываем файлик, без всякого препроцессинга
    print("hi")
    return render_template("index.html")

@main.route('/dist/<path:path>')
def static_dist(path):
    # тут пробрасываем статику
    return send_from_directory("static/dist", path)

@main.route('/pang', methods=['GET'])
@marshal_with(TestSchema())
def pingf_pong():
    teststr = TestClass('pung!')
    return teststr