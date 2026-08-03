import sqlite3

def connect_db():
    conn=sqlite3.connect("data/inventory.db")
    return conn 