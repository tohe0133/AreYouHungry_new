from random import randint
from databaseReader import create_activities

restaurants = []
randomRestaurant = ""


# loads in a restaurant from restaurant_database and turns it into a string
def load():
    global restaurants
    global randomRestaurant
    restaurants = create_activities("restaurant_database")
    randomRestaurant = f"You could eat at {restaurants[randint(0, len(restaurants)) - 1].get_name()}!"


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


def get_restaurant():
    global restaurants
    global randomRestaurant
    try:
        randomRestaurant = f"You could eat at {restaurants[randint(0, len(restaurants)) - 1].get_name()}!"
    except IndexError:
        randomRestaurant = "There are no restaurants that matches your filters"
    return randomRestaurant


def get_restaurant_list():
    return restaurants
