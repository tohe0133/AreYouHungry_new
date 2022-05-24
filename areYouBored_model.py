from random import randint
from databaseReader import create_activities
from activity import Activity
import sqlite3

connection = sqlite3.connect("restaurant.db", check_same_thread=False)




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


def sort(in_rating, in_price):
    global my_coords

    cursor = connection.cursor()
    cursor.execute(f"""
                    SELECT id
                    FROM restaurant 
                    WHERE 
                    rating >= {in_rating} AND price <= {in_price}
                """)
    rv = []
    for row in cursor:
        rv.append(list(row))
    return f"You could eat at {''.join(rv[0])}!"


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