from random import randint
from databaseReader import create_activities
from activity import Activity

restaurants = []
randomRestaurant = ""
chosenRestaurant = Activity(0, 0, 0, 0, 0, 0)
import sqlite3

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
    return randint(0, 12)


def go_to_restaurant(id_number):
    rv = []
    cursor = connection.cursor()
    cursor.execute(f"""
                SELECT x, y
                FROM restaurant 
                WHERE 
                id = {id_number}
            """)
    for row in cursor:
        rv.append(list(row))
    print(rv)


def get_restaurant_list():
    return restaurants
