import sqlite3
import activity
from databaseReader import create_activities

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
    price text,
    PRIMARY KEY (id)
);
"""

if index_option_one:
    indexes = """
CREATE INDEX namedim ON restaurant(name);
CREATE INDEX ratingdim ON restaurant(rating);
CREATE INDEX pricedim ON restaurant(price);"""
else:
    indexes = """
CREATE INDEX dims ON restaurant(name,rating,price);
"""

connection = sqlite3.connect("restaurant.db")
rest_from_file = create_activities("restaurant_database")


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
        '{in_price}')
    """)
    connection.commit()


def get_rating(in_rating):
    rv = []
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT * 
        FROM restaurant 
        WHERE 
        rating = {in_rating}
    """)
    for row in cursor:
        rv.append(list(row))
    return rv


define_db()
try:
    for i in range(len(rest_from_file)):
        add_restaurant(rest_from_file[i].get_name(), rest_from_file[i].get_coords_x(), rest_from_file[i].get_coords_y(),
                       rest_from_file[i].get_rating(), rest_from_file[i].get_price())
    print("The database was created!")

except:
    print("There was an error creating the database")
