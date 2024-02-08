from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация 1'


@app.route('/index')
def index_1():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def prom():
    return ('<p>Человечество вырастает из детства.</p><br>'
            '<p>Человечеству мала одна планета.</p><br>'
            '<p>Мы сделаем обитаемыми безжизненные пока планеты.</p><br>'
            '<p>И начнем с Марса!</p><br>'
            '<p>Присоединяйся!</p><br>')


@app.route('/image_mars')
def mars():
    return render_template('mars.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
