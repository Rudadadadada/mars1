from flask import Flask, request, render_template
from planets import planets
from PIL import Image
from io import BytesIO


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


@app.route('/promotion_image')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href="/static/css/style.css" type="text/css">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png">
                    <h5 class="alert alert-dark" role="alert">
                        Человечество вырастает из детства.
                    </h5>
                    <h5 class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                    </h5>
                    <h5 class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </h5>
                    <h5 class="alert alert-warning" role="alert">
                        И начнем с Марса!
                    </h5>
                    <h5 class="alert alert-danger" role="alert">
                        Присоединяйся!
                    </h5>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection_form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        return render_template('form1.html')


@app.route('/choice/<planet_name>')
def choice(planet_name):
    dictionary = dict()
    if planet_name.lower() in planets:
        dictionary['planet_name'] = planet_name.lower().capitalize()
        for i in range(1, 6):
            dictionary['text' + str(i)] = planets[planet_name.lower()][i - 1]
        return render_template('choice.html', **dictionary)
    else:
        dictionary['planet_name'] = planet_name.lower().capitalize()
        return render_template('choice1.html', **dictionary)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    dictionary = dict()
    dictionary['nickname'] = nickname.lower().capitalize()
    dictionary['level'] = str(level).lower().capitalize()
    dictionary['rating'] = str(rating).lower().capitalize()
    return render_template('result.html', **dictionary)


@app.route('/load_photo', methods=['POST', 'GET'])
def photo():
    if request.method == 'GET':
        return render_template('photo.html')
    elif request.method == 'POST':
        photo = request.files['photo']
        im = Image.open(BytesIO(photo.read()))
        im.save('static/img/person.png')
        return render_template('photo1.html')


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')

if '__main__' == __name__:
    app.run(port=8080, host='127.0.0.1')