from flask import Flask, request, render_template
from areYouBored_model import load, get_restaurant, get_restaurant_list, sort_distance, sort_rating, sort_price

app = Flask(__name__)


@app.route('/')
def home():
    load()
    return render_template('index.html')


@app.route('/print')
def print():
    get_restaurant()
    return render_template('view.html', restaurants=get_restaurant())


@app.route('/sort', methods=['POST'])
def sort():
    restaurant = get_restaurant_list()
    try:
        sort_rating(restaurant, int(request.values.get('rate')))
    except TypeError:
        pass
    try:
        sort_price(restaurant, int(request.values.get('price')))
    except TypeError:
        pass
    try:
        sort_distance(restaurant, int(request.values.get('distance')))
    except TypeError:
        pass
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=1234)
