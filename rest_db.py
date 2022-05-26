import sqlite3
import os
from textfile_loader import create_activities

build_indexes = True
index_option_one = False

definition = """

DROP TABLE IF EXISTS restaurant;

CREATE TABLE restaurant(
    id integer,
    name text,
    x real,
    y real,
    rating integer,
    price integer,
    PRIMARY KEY (id)
);
"""

try:
    os.remove("restaurant.db")
except:
    pass

connection = sqlite3.connect("restaurant.db")
rest_from_file = create_activities("restaurants_textfile")

def define_db():
    cursor = connection.cursor()
    for command in definition.split(";"):
        cursor.execute(command)


def add_restaurant(in_name, in_x, in_y, in_rating, in_price):
    cursor = connection.cursor()
    cursor.execute(f"""
        INSERT INTO restaurant(name,x,y,rating,price) VALUES (
        '{in_name}',
        {in_x},
        {in_y},
        {in_rating},
        {in_price})
    """)
    connection.commit()


define_db()

try:
    for i in range(len(rest_from_file)):
        add_restaurant(rest_from_file[i].get_name(), rest_from_file[i].get_coords_x(), rest_from_file[i].get_coords_y(),
                       rest_from_file[i].get_rating(), rest_from_file[i].get_price())
    print("The database was created!")

except:
    print("There was an error creating the database")
