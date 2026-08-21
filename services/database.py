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

    cursor.execute("""SELECT * FROM products where id = ?""",(product_id,))

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
def inventory_statistics():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(quantity) FROM products")
    total_quantity = cursor.fetchone()[0]

    cursor.execute("""
        SELECT category, COUNT(*)
        FROM products
        GROUP BY category
    """)

    category_counts = cursor.fetchall()

    conn.close()

    return total_products, total_quantity, category_counts

def create_views():
    conn=connect_db()
    cursor=conn.cursor()

    #Low stock view
    cursor.execute("""CREATE VIEW IF NOT EXISTS low_stock_products AS 
    SELECT * FROM products  WHERE quantity <= 2""")

    #Food and Medicine expiry view
    cursor.execute("""CREATE VIEW IF NOT EXISTS expiring_products AS
    SELECT * FROM products WHERE category != 'Electronics' """)

    #Category Summary View
    cursor.execute("""CREATE VIEW IF NOT EXISTS category_summary AS
    SELECT category,COUNT(*) AS total_products, SUM(quantity) AS total_quantity FROM
    products GROUP BY category""")

    conn.commit()
    conn.close()

def get_low_stock_view():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM low_stock_products
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def create_category_details_table():
    conn=connect_db()
    cursor=conn.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS category_details(
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT UNIQUE NOT NULL,
            description TEXT
        )""")

    conn.commit()
    conn.close()

def insert_categories():
    conn = connect_db()
    cursor = conn.cursor()

    categories=[
        ("Food", "Food and grocery products"),
        ("Medicines", "Medicines and healthcare products"),
        ("Electronics", "Electronic products and devices")
    ]

    cursor.executemany("""INSERT OR IGNORE INTO category_details
        (category_name, description)
        VALUES (?, ?)""",categories)

    conn.commit()
    conn.close()

def get_products_with_categories():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            products.id,
            products.name,
            products.category,
            products.quantity,
            category_details.description
        FROM products
        INNER JOIN category_details
        ON products.category = category_details.category_name
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_all_products_with_categories():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            products.id,
            products.name,
            products.category,
            category_details.description
        FROM products
        LEFT JOIN category_details
        ON products.category = category_details.category_name
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def category_summary():
    conn= connect_db()
    cursor=conn.cursor()

    