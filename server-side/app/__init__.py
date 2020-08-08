from flask import Flask, jsonify, send_from_directory, render_template

app = Flask(__name__,
            static_folder = "./static/dist",
            template_folder = "./static")
app.config.from_object(__name__)

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
def pingf_pong():
    return jsonify('pung!')

from app.routes import test
