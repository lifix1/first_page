from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'


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


@app.route('/promotion_image')
def mars():
    return render_template('mars.html')


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['educ'])
        print(request.form['prof'])
        print(request.form['gender'])
        print(request.form['motiv'])
        print('Да') if request.form['stay_on_mars'] == 'on' else print('Нет')
        return render_template('form.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
