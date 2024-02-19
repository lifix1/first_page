from flask import Flask, render_template

app = Flask(__name__)


class AnswerForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    educ = StringField('Образование', validators=[DataRequired()])
    prof = StringField('Профессия', validators=[DataRequired()])
    gender = StringField('Пол', validators=[DataRequired()])
    motiv = StringField('Мотивация', validators=[DataRequired()])
    stay_on_mars = StringField('Готовы ли вы остаться на марсе?', validators=[DataRequired()])
    submit = SubmitField('Отправить')


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    form = AnswerForm()
    if form.validate_on_submit():
        return render_template('auto_answer.html', form=form)
    return render_template('answer.html', form=form)


@app.route('/auto_answer', methods=['GET', 'POST'])
def auto_answer():
    form = AnswerForm()
    if form.validate_on_submit():
        return render_template('auto_answer.html', form=form)
    return render_template('answer.html', form=form)


@app.route('/index/<user_input>')
def index(user_input):
    params = {}
    params['Title'] = user_input
    return render_template('base.html', **params)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
