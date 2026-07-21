# 📦 ShelfLife v1.1

ShelfLife is a terminal-based inventory management application built in Python as a hands-on project to practice Object-Oriented Programming (OOP).

The application allows users to manage inventory items, search products, monitor low stock levels, and track expiry dates through an interactive command-line interface.

Unlike a single-file Python script, ShelfLife follows a modular architecture where different responsibilities are separated into dedicated classes and modules, making the project scalable and easier to maintain.

> **Project Goal:** Learn Python by building a real-world project that grows with every new concept learned—from OOP to File Handling, Databases, GUI development, and finally a Django web application.

---

# ✨ Features

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
- Interactive terminal menu
- Input validation

---

# 🧠 OOP Concepts Demonstrated

ShelfLife was built to practice real-world Object-Oriented Programming concepts.

### ✅ Classes & Objects
Creating reusable Product and Inventory objects.

### ✅ Constructors
Using `__init__()` to initialize every object.

### ✅ Encapsulation
Important product details are hidden using private attributes.

```python
__id
__quantity
__expiry_date
```

### ✅ Inheritance

The project uses inheritance to represent different product types.

```text
                Product
                   │
        ┌──────────┼──────────┐
        │          │          │
      Food     Medicine   Electronics
```

Each child class inherits common functionality from the `Product` class.

### ✅ Method Overriding

Every child class overrides the `display()` method to show its own unique information.

### ✅ Runtime Polymorphism

The Inventory stores different product types together.

```python
for product in products:
    product.display()
```

Python automatically calls the correct `display()` method depending on whether the object is a Food, Medicine, or Electronics product.

### ✅ Composition

The Inventory class manages multiple Product objects.

### ✅ Object Interaction

Objects communicate through methods instead of directly manipulating internal data.

---

# 📁 Project Structure

```text
ShelfLife/
│
├── main.py                 # Entry point & terminal menu
├── inventory.py            # Inventory class
├── product.py              # Parent Product class
├── food.py                 # Food class
├── medicine.py             # Medicine class
├── electronics.py          # Electronics class
├── .gitignore
└── README.md
```

---

# Terminal Menu

```text
========================================
            📦 ShelfLife v1.1
     Terminal Inventory Management
========================================

1. Add Product
2. View Products
3. Search Product
4. Update Quantity
5. Remove Product
6. Low Stock Report
7. Expiry Report
8. Exit
```

---

# 📌 Product Information

Each product stores:

- Product ID
- Product Name
- Category
- Quantity
- Expiry Date

Additional information depends on the product type.

### Food

- Storage Type

### Medicine

- Manufacturer
- Prescription Required

### Electronics

- Brand
- Warranty Period

---

# 🚀 Roadmap

## ✅ Version 1.1 (Current)

- [x] Modular project structure
- [x] Product class
- [x] Inventory class
- [x] Food class
- [x] Medicine class
- [x] Electronics class
- [x] Encapsulation
- [x] Inheritance
- [x] Method Overriding
- [x] Runtime Polymorphism
- [x] Add products
- [x] View products
- [x] Search by ID
- [x] Search by Name
- [x] Search by Category
- [x] Update quantity
- [x] Remove products
- [x] Low stock report
- [x] Expiry report
- [x] Input validation

---

## 📂 Version 2

- File Handling
- Save inventory automatically
- Load inventory on startup
- Better exception handling
- Improved terminal UI

---

## 📄 Version 3

- JSON support
- CSV support
- Data import/export
- Product statistics

---

## 🗄️ Version 4

- SQLite Database
- CRUD using SQL
- Persistent storage
- Advanced searching

---

## 🖥️ Version 5

- Tkinter / CustomTkinter GUI
- Tables
- Forms
- Dashboard

---

## 🌐 Final Version

- Django
- Authentication
- Inventory Dashboard
- Product Analytics
- Email Reminder System
- Deployment

---

# 🎯 Learning Purpose

ShelfLife is a long-term learning project.

Instead of building everything at once, the project evolves after every major Python topic.

Current progression:

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

This repository documents my journey from learning basic Python to building a complete inventory management system.

---

# Technologies Used

- Python 3
- Object-Oriented Programming
- Encapsulation
- Inheritance
- Method Overriding
- Runtime Polymorphism
- Composition
- `datetime` module
- Terminal / Command Line Interface

---

# 📸 Current Status

**Current Version:** `v1.1`

✔️ Modular architecture

✔️ Multiple Python modules

✔️ Inheritance implemented

✔️ Runtime polymorphism implemented

✔️ Core inventory management features completed

---

## ⭐ Future Vision

ShelfLife is not just a practice project—it's a project that will continuously evolve as I learn new technologies.

The goal is to transform it from a simple terminal application into a complete, production-ready inventory management system with database support, a graphical interface, and a full-stack Django web application.