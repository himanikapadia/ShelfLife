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

    elif isinstance(product, Electronics):
        cursor.execute("""INSERT INTO products VALUES(?,?,?,?,?,?,?,?,?,?)""",
                       (
                            product.get_id(),
                            product.get_name(),
                            product.get_category(),
                            product.get_qty(),
                            "N/A",
                            None,
                            None,
                            None,
                            product.get_warranty(),
                            product.get_brand()
                       ))
    conn.commit()
    conn.close()

def load_products():
    conn=connect_db()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows=cursor.fetchall()

    products=[]

    for i in rows:
        if i[2]=="Food":
            product=Food(
                i[0],      # id
                i[1],      # name
                i[3],      # quantity
                i[4],      # expiry
                i[5]       # storage
            )
        elif i[2]== "Medicines":
            product=Medicines(
                i[0],      # id
                i[1],      # name
                i[3],      # quantity
                i[4],      # expiry
                i[6],      # Manufacturer
                i[7]       # Prescription
            )
        elif i[2]== "Electronics":
            product=Electronics(
                i[0],      # id
                i[1],      # name
                i[3],      # quantity
                i[8],      # Warranty
                i[9]       # Brand
            )
        else:
            continue

        products.append(product)
    conn.close()
    return products

def update_qty(product_id,quantity):
    print("Updating database...", product_id, quantity)
    conn= connect_db()
    cursor=conn.cursor()

    cursor.execute("""UPDATE products SET quantity=? WHERE id = ?""",(quantity,product_id))
    conn.commit()
    print("Rows updated:", cursor.rowcount)
    conn.close()

def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM products
        WHERE id = ?
    """, (product_id,))

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted > 0

def search_by_id(product_id):
    conn=connect_db()
    cursor=conn.cursor()

    cursor.execute("""SELECT * FROM product where id = ?""",(product_id,))

    row=cursor.fetchone()

    conn.close()
    return row

def search_by_name(name):
    conn=connect_db()
    cursor=conn.execute()

    cursor.execute("""
        SELECT * FROM products
        WHERE name LIKE ?
    """, (f"%{name}%",))

    rows = cursor.fetchall()

    conn.close()

    return rows

def search_by_category(category):
    conn=connect_db()
    cursor=conn.execute()

    cursor.execute("""SELECT * FROM products WHERE category= ?""",(category,))

    rows = cursor.fetchall()

    conn.close()

    return rows
