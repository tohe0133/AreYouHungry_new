from flask import Flask, request, render_template, redirect
from areYouBored_model import get_restaurant, go_to_restaurant, id_generation, sorting

app = Flask(__name__)
restaurant_id = 0

distance = 2000
rating = 1
price = 3
is_sorted = False


@app.route('/')
def home():
    global restaurant_id, is_sorted
    is_sorted = False
    restaurant_id = id_generation()
    return render_template('index.html', message=None)


@app.route('/print')
def print():
    global restaurant_id, is_sorted, distance, rating, price
    if is_sorted == False:
        restaurant_id = id_generation()
        get_restaurant(restaurant_id)
        return render_template('view.html', restaurants=get_restaurant(restaurant_id))
    else:
        restaurant_id = sorting(distance, rating, price)
        if restaurant_id == 0:
            return render_template('index.html', message='Could not find any restaurant. Try again')
        else:
            get_restaurant(restaurant_id)
            return render_template('view.html', restaurants=get_restaurant(restaurant_id))


@app.route('/sort', methods=['POST'])
def sort_rest():
    global distance, rate, price, is_sorted
    try:
        distance = int(request.values.get('distance'))
    except TypeError:
        pass
    try:
        rate = int(request.values.get('rate'))
    except TypeError:
        pass
    try:
        price = int(request.values.get('price'))
    except TypeError:
        pass
    is_sorted = True
    return render_template('index.html', message='Sorting restaurants...')


@app.route('/take_me_there')
def take_me_there():
    global restaurant_id
    return redirect(f" https://www.google.com/maps/search/?api=1&query={go_to_restaurant(restaurant_id)}")


if __name__ == '__main__':
    app.run(debug=True, port=1234)
