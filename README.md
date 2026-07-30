# 📦 ShelfLife v3.0

ShelfLife is a terminal-based Inventory Management System built in Python to practice Object-Oriented Programming and gradually learn advanced Python concepts by building a real-world project.

The project follows a modular architecture with separate models, services, and utility modules, making it easy to maintain and extend.

> **Project Goal:** Learn Python by building a complete inventory management system that evolves from a simple CLI application to a full-stack Django web application.

---

# ✨ Features

### Inventory Management
- Add Products
- View Products
- Search Products
  - By ID
  - By Name
  - By Category
- Update Product Quantity
- Remove Products

### Reports
- Low Stock Report
- Expiry Report
  - Expired Products
  - Expires Today
  - Expires Within 7 Days
  - Remaining Days

### File Handling
- Automatic Save to Text File
- Automatic Load on Startup
- JSON Export
- JSON Import
- CSV Export
- CSV Import

### Inventory Analytics
- Inventory Statistics
  - Total Products
  - Food Count
  - Medicines Count
  - Electronics Count
  - Total Quantity

### Product Operations
- Sort Products
  - By ID
  - By Name
  - By Quantity
- Filter Products
  - By Category
  - Low Stock Products

### Backup & Restore
- Create Inventory Backup
- Restore Inventory from Backup

### Other
- Modular Project Structure
- Exception Handling
- Interactive Terminal Menu
- Input Validation

---

# 🧠 OOP Concepts Demonstrated

ShelfLife was built to practice real-world Object-Oriented Programming.

## * Classes & Objects

Creating reusable Product and Inventory objects.

##  Constructors

Using `__init__()` for object initialization.

## * Encapsulation

Private attributes protect important data.

```python
__id
__quantity
__expiry_date
```

## * Inheritance

```
                Product
                   │
        ┌──────────┼──────────┐
        │          │          │
      Food     Medicines   Electronics
```

## * Method Overriding

Each child class overrides `display()`.

## * Runtime Polymorphism

```python
for product in products:
    product.display()
```

Python automatically calls the correct display method.

## * Composition

Inventory stores multiple Product objects.

## * Object Interaction

Objects communicate using methods rather than directly accessing data.

---

# 📁 Project Structure

```text
ShelfLife/
│
├── data/
│   ├── inventory.txt
│   ├── inventory.json
│   ├── inventory.csv
│   └── backup.txt
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

# 🖥 Terminal Menu

```text
========================================
           📦 ShelfLife v3.0
========================================

1. Add Product
2. View Products
3. Search Product
4. Update Quantity
5. Remove Product
6. Low Stock Report
7. Expiry Report
8. Export JSON
9. Import JSON
10. Export CSV
11. Import CSV
12. Inventory Statistics
13. Sort Products
14. Filter Products
15. Backup Inventory
16. Restore Inventory
0. Exit
```

---

#  Product Types

## Food

- Expiry Date
- Storage Type

## Medicines

- Expiry Date
- Manufacturer
- Prescription Required

## Electronics

- Brand
- Warranty Period

---

# 🚀 Roadmap

## ✅ Version 1

- Product Management
- OOP Concepts
- Search
- Update
- Remove
- Reports

## ✅ Version 2

- File Handling
- Automatic Save
- Automatic Load
- Better Exception Handling
- Improved Project Structure

## ✅ Version 3 (Current)

- JSON Export/Import
- CSV Export/Import
- Inventory Statistics
- Product Sorting
- Product Filtering
- Backup & Restore

---

## 🔜 Version 4

- SQLite Database
- CRUD Operations
- SQL Queries
- Advanced Search
- Database Persistence

---

## 🔜 Version 5

- Tkinter / CustomTkinter GUI
- Dashboard
- Tables
- Forms
- Charts

---

## 🌐 Final Version

- Django
- Authentication
- Product Dashboard
- Analytics
- Email Expiry Notifications
- REST API
- Deployment

---

#  Concepts Practiced

- Object-Oriented Programming
- Encapsulation
- Inheritance
- Polymorphism
- Composition
- File Handling
- JSON
- CSV
- Exception Handling
- Sorting
- Filtering
- Backup & Restore
- Modular Programming
- datetime
- shutil

---

# 🛠 Technologies Used

- Python 3
- Object-Oriented Programming
- JSON
- CSV
- File Handling
- datetime
- shutil
- Terminal / CLI

---

#  Learning Journey

ShelfLife is a long-term learning project.

Each version introduces new Python concepts and expands the application.

```
Python Basics
      ↓
Object-Oriented Programming
      ↓
Inheritance & Polymorphism
      ↓
File Handling
      ↓
JSON & CSV
      ↓
Sorting & Filtering
      ↓
Backup & Restore
      ↓
SQLite
      ↓
GUI
      ↓
Django
```

The goal is to gradually transform ShelfLife into a production-ready inventory management system.

---

# 📌 Current Status

**Current Version:** `v3.0`

- Modular Architecture

- OOP Concepts

- File Handling

- JSON Support

- CSV Support

- Inventory Statistics

- Product Sorting

- Product Filtering

- Backup & Restore

🚀 Ready for Version 4 (SQLite Database)