from flask import jsonify
from app import app

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
