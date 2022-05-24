from random import randint
from databaseReader import create_activities
from activity import Activity
import sqlite3

restaurants = []
randomRestaurant = ""
chosenRestaurant = Activity(0, 0, 0, 0, 0, 0)

connection = sqlite3.connect("restaurant.db", check_same_thread=False)


# loads in a restaurant from restaurant_database and turns it into a string
def load():
    global restaurants
    global randomRestaurant
    global chosenRestaurant
    restaurants = create_activities("restaurant_database")
    chosenRestaurant = restaurants[randint(0, len(restaurants)) - 1]
    randomRestaurant = f"You could eat at {chosenRestaurant.get_name()}!"


def get_random_restaurant():
    global restaurants
    global randomRestaurant
    randomRestaurant = f"You could eat at {restaurants[randint(0, len(restaurants)) - 1].get_name()}!"


def sorting(in_distance, in_rating, in_price):
    global my_coords
    first_x = float(my_coords[0]) + (float(in_distance) * 0.00000899774)
    second_x = float(my_coords[0]) - (float(in_distance) * 0.00000899774)
    first_y = float(my_coords[1]) + (float(in_distance) * 0.00000899774)
    second_y = float(my_coords[1]) - (float(in_distance) * 0.00000899774)
    cursor = connection.cursor()
    cursor.execute(f"""
                    SELECT id
                    FROM restaurant 
                    WHERE 
                    x between {first_x} and {second_x} AND y between {first_y} and {second_y} AND
                    rating >= {in_rating} AND price <= {in_price}
                """)
    rv = cursor.fetchone()
    print(rv)



# Sorts based on distance
def sort_distance(rList, rRange):
    d = 0
    try:
        for i in range(len(rList)):
            if rList[i - d].get_distance() > rRange:
                del rList[i - d]
                d += 1
    except:
        pass
    return rList


# Sorts based on rating
def sort_rating(rList, rRange):
    d = 0
    try:
        for i in range(len(rList)):
            if rList[i - d].get_rating() < rRange:
                del rList[i - d]
                d += 1
    except:
        pass
    return rList


# Sorts based on price
def sort_price(rList, rRange):
    d = 0
    try:
        for i in range(0, len(rList)):
            if rList[i - d].get_price_int() > rRange:
                del rList[i - d]
                d += 1
    except:
        pass
    return rList


# def get_restaurant():
#     global restaurants
#     global randomRestaurant
#     global chosenRestaurant
#     try:
#         randomRestaurant = f"You could eat at {chosenRestaurant.get_name()}!"
#     except IndexError:
#         randomRestaurant = "There are no restaurants that matches your filters"
#     return randomRestaurant

def get_restaurant(id_number):
    rv = []
    cursor = connection.cursor()
    cursor.execute(f"""
            SELECT name 
            FROM restaurant 
            WHERE 
            id = {id_number}
        """)
    for row in cursor:
        rv.append(list(row))
    return f"You could eat at {''.join(rv[0])}!"


def id_generation():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM restaurant")
    results = cursor.fetchall()
    length = len(results)
    return randint(1, length)


def go_to_restaurant(id_number):
    cursor = connection.cursor()
    cursor.execute(f"""
                SELECT x, y
                FROM restaurant 
                WHERE 
                id = {id_number}
            """)
    tuple1 = cursor.fetchone()
    rv = f"{tuple1[0]},{tuple1[1]}"
    return rv


def get_restaurant_list():
    return restaurants
