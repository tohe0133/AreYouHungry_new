from random import randint
import sqlite3

connection = sqlite3.connect("restaurant.db", check_same_thread=False)
my_coords = (63.82587043650309, 20.26303012372108)


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
                    x < {first_x} AND x > {second_x} AND 
                    y < {first_y} AND y < {second_y} AND
                    rating >= {in_rating} AND 
                    price <= {in_price}
                """)
    results = cursor.fetchall()
    print(results)
    length = len(results)
    return randint(1, length)