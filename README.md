# 📦 ShelfLife v2.0

ShelfLife is a terminal-based inventory management application built in Python to practice Object-Oriented Programming (OOP) by developing a real-world project.

The application allows users to manage inventory, search products, monitor low stock, track expiry dates, and automatically save data using multiple file formats.

Rather than being a single-file script, ShelfLife follows a modular architecture with separate models, services, utilities, and data handling modules, making it scalable and maintainable.

> **Project Goal:** Build an inventory management system while progressively learning Python concepts—from OOP and File Handling to Databases, GUI development, and finally a Django web application.

---

#  Features

- Add new products
- View all products
- Search products
  - By ID
  - By Name
  - By Category
- Update product quantity
- Remove products
- Low stock detection
- Expiry report
  - Expired products
  - Products expiring today
  - Products expiring within 7 days
  - Remaining days until expiry
- Automatic inventory saving
- Automatic inventory loading
- Export inventory to JSON
- Import inventory from JSON
- Export inventory to CSV
- Import inventory from CSV
- Interactive terminal menu
- Input validation
- Exception handling

---

# 🧠 OOP Concepts Demonstrated

ShelfLife was built to practice real-world Object-Oriented Programming concepts.

##  Classes & Objects

Creating reusable Product and Inventory objects.

##  Constructors

Using `__init__()` to initialize objects.

##  Encapsulation

Important product details are protected using private attributes.

```python
__id
__quantity
__expiry_date
```

##  Inheritance

```text
                Product
                   │
        ┌──────────┼──────────┐
        │          │          │
      Food     Medicines   Electronics
```

Each child class inherits common functionality from `Product`.

##  Method Overriding

Each product type overrides `display()` to show category-specific information.

##  Runtime Polymorphism

```python
for product in products:
    product.display()
```

Python automatically executes the correct `display()` method depending on the object type.

##  Composition

The `Inventory` class manages multiple `Product` objects.

##  Object Interaction

Objects communicate through methods instead of directly modifying internal state.

---

# 📁 Project Structure

```text
ShelfLife/
│
├── data/
│   ├── inventory.txt
│   ├── inventory.json
│   └── inventory.csv
│
├── models/
│   ├── product.py
│   ├── food.py
│   ├── medicines.py
│   └── electronics.py
│
├── services/
│   ├── inventory.py
│   └── file_handler.py
│
├── utils/
│   └── menu.py
│
├── main.py
└── README.md
```

---

#  Terminal Menu

```text
========================================
            📦 ShelfLife v2.0
========================================

1. Add Product
2. View Products
3. Search Product
4. Update Quantity
5. Remove Product
6. Low Stock Report
7. Expiry Report
8. Export to JSON
9. Import from JSON
10. Export to CSV
11. Import from CSV
0. Exit
```

---

#  Product Information

Every product stores:

- Product ID
- Product Name
- Category
- Quantity
- Expiry Date

Additional information depends on the product type.

###  Food

- Storage Type

###  Medicines

- Manufacturer
- Prescription Required

###  Electronics

- Brand
- Warranty Period

---

#  Data Persistence

ShelfLife automatically saves inventory data after every change.

Supported formats:

- TXT (default persistent storage)
- JSON
- CSV

This allows inventory to persist between application runs and enables easy data sharing through import/export.

---

#  Roadmap

## ✅ Version 2.0 (Current)

- [x] Modular project structure
- [x] Product hierarchy
- [x] Inventory management
- [x] Encapsulation
- [x] Inheritance
- [x] Method Overriding
- [x] Runtime Polymorphism
- [x] Add products
- [x] Search products
- [x] Update quantity
- [x] Remove products
- [x] Low stock report
- [x] Expiry report
- [x] Automatic save/load
- [x] JSON export/import
- [x] CSV export/import
- [x] Exception handling

---

##  Version 3

- SQLite Database
- CRUD operations
- Advanced searching
- Product statistics

---

##  Version 4

- Tkinter / CustomTkinter GUI
- Dashboard
- Tables
- Forms
- Charts

---

##  Final Version

- Django
- User Authentication
- Inventory Dashboard
- Product Analytics
- Email Notifications
- REST API
- Deployment

---

#  Learning Journey

```
OOP
      ↓
Inheritance & Polymorphism
      ↓
File Handling
      ↓
JSON / CSV
      ↓
SQLite
      ↓
GUI
      ↓
Django
```

ShelfLife grows alongside my Python learning journey, with each version introducing new concepts and technologies.

---

# 🛠 Technologies Used

- Python 3
- Object-Oriented Programming
- File Handling
- JSON
- CSV
- Encapsulation
- Inheritance
- Method Overriding
- Runtime Polymorphism
- Composition
- `datetime`
- Terminal / CLI

---

# 📈 Current Status

**Current Version:** `v2.0`

✅ Modular architecture

✅ Inventory persistence

✅ TXT storage

✅ JSON support

✅ CSV support

✅ Import/Export functionality

✅ Low stock & expiry reporting

✅ OOP concepts implemented

---

#  Future Vision

ShelfLife is more than a practice project—it's a long-term learning project that evolves with every new Python concept I learn.

The goal is to transform it from a terminal application into a complete inventory management system with database support, a graphical interface, REST APIs, authentication, and a full-stack Django web application.