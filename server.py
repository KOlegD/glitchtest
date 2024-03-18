import os

import flask
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"

@app.route('/api')
def get_api():
    return flask.jsonify({'a': 'мой первый ответ json'})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)