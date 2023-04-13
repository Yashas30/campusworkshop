"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq4qpmbg5e4khqmrk0-a.oregon-postgres.render.com",
        database="workshop_fh5q",
        user="workshop_fh5q_user",
        password="Xv33JEpyObqdbxQ5eYPiYbDu0uzJr5hS")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
