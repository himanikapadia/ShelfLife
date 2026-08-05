import sqlite3

from models.food import Food
from models.electronics import Electronics
from models.medicines import Medicines

def connect_db():
    conn=sqlite3.connect("data/inventory.db")
    return conn 

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            expiry TEXT,
            storage TEXT,
            manufacturer TEXT,
            prescription TEXT,
            warranty INTEGER,
            brand TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_product(product):
    conn= connect_db()
    cursor= conn.cursor()

    if isinstance(product, Food):
        cursor.execute("""INSERT INTO products VALUES(?,?,?,?,?,?,?,?,?,?)""", 
                       (
                           product.get_id(),
                           product.get_name(),
                           product.get_category(),
                           product.get_qty(),
                           product.get_expiry(),
                           product.get_storage(),
                           None,
                           None,
                           None,
                           None
                       ))

    elif isinstance(product, Medicines):
        cursor.execute("""INSERT INTO products VALUES(?,?,?,?,?,?,?,?,?,?)""",
                       (
                           product.get_id(),
                           product.get_name(),
                           product.get_category(),
                           product.get_qty(),
                           product.get_expiry(),
                           None,
                           product.get_manufacturer(),
                           product.get_prescription(),
                           None,
                           None
                       ))
