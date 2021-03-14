from flask import Flask
from url_generator.url_generator import get_random

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/url_generate/')
def generate():
    return get_random()


if __name__ == '__main__':
    app.run()
