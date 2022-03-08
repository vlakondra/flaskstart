import sqlite3
from flask import current_app, g



def get_db():
    print("GETDB")
    print(current_app)
    # print(current_app)