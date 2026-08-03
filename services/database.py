import sqlite3

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