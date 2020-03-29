from flask import Flask
import flask

app = Flask(__name__)


@app.route('/')
def route():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    a = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
         'Присоединяйся!']
    return '<br>'.join(a)


@app.route('/image_mars')
def picture():
    return '<head><title>Привет, Марс!</title></head>' \
           '<h1>Жди нас, Марс!</h1>' \
           '<img src="/static/img/mars.png">' \
           '<figcaption>Вот она какая, красная планета.</figcaption>'


if '__main__' == __name__:
    app.run(port=8080, host='127.0.0.1')