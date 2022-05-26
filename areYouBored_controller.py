from flask import Flask, request, render_template, redirect
from areYouBored_model import get_restaurant, go_to_restaurant, id_generation, sorting

app = Flask(__name__)
restaurant_id = 0
user_location = ()


@app.route('/')
def home():
    global restaurant_id
    restaurant_id = id_generation()
    return render_template('index.html', message=None)


@app.route('/print')
def print():
    global restaurant_id
    get_restaurant(restaurant_id)
    return render_template('view.html', restaurants=get_restaurant(restaurant_id))


@app.route('/sort', methods=['POST'])
def sort_rest():
    global restaurant_id
    restaurant_id = sorting(int(request.values.get('distance')), int(request.values.get('rate')),int(request.values.get('price')))
    return render_template('index.html', message='Sorting restaurants...')


@app.route('/take_me_there')
def take_me_there():
    global restaurant_id
    return redirect(f" https://www.google.com/maps/search/?api=1&query={go_to_restaurant(restaurant_id)}")


if __name__ == '__main__':
    app.run(debug=True, port=1234)
