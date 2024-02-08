from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index_1():
    return 'И на Марсе будут яблони цвести!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
