# import os
# print(os.getcwd())
from services.database import (
    create_table,
    create_category_details_table,
    insert_categories,
    load_products,
    create_views
)
from services.inventory import Inventory
from services.database import get_low_stock_view
#from models.product import Product
from models.food import Food
from models.medicines import Medicines
from models.electronics import Electronics
from services.file_handler import (
    #load_inventory,
    save_inventory,
    export_json,
    import_json,
    export_csv,
    import_csv,
    backup_inventory,
    restore_inventory
)

from utils.menu import show_menu

# Initialize Inventory
create_table()
create_views()
create_category_details_table()
insert_categories()
products=load_products()
inv=Inventory()
for product in products:
    inv.add_loaded_product(product)

print("=" * 40)
print("Welcome to ShelfLife V3.0")
print(f"{len(products)} products loaded successfully.")
print("=" * 40)

#========= User Menu =========
while True:
    show_menu()
    try:
        choice = int(input("Enter your Choice: "))

        # ----- ADD PRODUCT ----- 

        if choice == 1:

            print("\n----Select Product Type----")
            print("1. Food")
            print("2. Medicine")
            print("3. Electronics")

            ptype=int(input("Enter Your choice: "))

            print("~ Enter Product Details ~")
            #print("Loaded Products:", len(inv.get_products()))
            while True:
                pid = int(input("ID: "))
                if inv.id_exists(pid):
                    print("Product ID already exists. Please enter another ID.")
                else:
                    break

            pname=input("Name: ")
            qty=int(input("Quantity: "))

            if ptype==1:
                exp=input("Expiry Date (DD-MM-YYYY): ")
                storage = input("Storage Type: ")

                product=Food(pid,pname,qty,exp,storage)

            elif ptype==2:
                exp=input("Expiry Date (DD-MM-YYYY): ")
                manufacturer = input("Manufacturer: ")
                prescription = input("Prescription Required (Yes/No): ")

                product=Medicines(pid,pname,qty,exp,manufacturer,prescription)

            elif ptype==3:
                warranty=int(input("Warranty (Months): "))
                brand = input("Brand: ")

                product=Electronics(pid,pname,qty,warranty,brand)

            else:
                print("Invalid Product Type")
                continue
    
            inv.add_product(product)
            print("\nProduct Added Successfully!!")


        # ------ VIEW PRODUCT -----
        
        elif choice == 2:
            inv.display_products()


        # ----- SEARCH -------
        
        elif choice == 3:
            print("----Search Options----")
            print("1. Search by ID")
            print("2. Search by Name")
            print("3. Search by Category")
            ch=int(input("Enter Choice: "))
            if ch == 1:
                pid=int(input("Enter product ID to search: "))
                product=inv.search_by_Id(pid)
                if product:
                    print("\nProduct found!")
                    product.display()
                else:
                    print("\nProduct Not found!")
            elif ch == 2:
                name=input("Enter Name to be search: ")
                product=inv.search_by_name(name)
                if product:
                    print("\nProduct Found!")
                    for product in products:
                        product.display()
                else:
                    print("\nProduct Not Found!")
            elif ch == 3:
                category=input("Enter Category to be search: ")
                products=inv.search_by_category(category)
                if products:
                    print("\nProduct Found!")
                    for product in products:
                        product.display()
                else:
                    print("\nNo products found in this category!")
            else:
                print("Invalid Choice!")
                break

        # ----- UPDATE -----

        elif choice == 4:
            pid=int(input("Enter Prouduct ID to be updated: "))
            product=inv.search_by_Id(pid)
            if product:
                print("Product found!")
                amount = int(input("Enter quantity to add (+) or remove (-): "))
                if inv.update_product_qty(pid, amount):
                    product = inv.search_by_Id(pid)
                    print("\nQuantity Updated Successfully!")
                    print("Current Quantity:", product.get_qty())
                else:
                    print("Update Unsuccessful")
            else:
                print("Product ID: " ,pid," Not found!")

        # ----- REMOVE -----

        elif choice == 5:
            pid=int(input("Enter Prouduct ID to be Removed: "))
            product=inv.remove_product(pid)

        # ---- LOW STOCK -----

        elif choice == 6:
            rows = get_low_stock_view()

            if rows:
                print("\n===== LOW STOCK PRODUCTS =====")

                for row in rows:
                    print(row)
            else:
                print("\nNo low stock products found!")

        #----- EXPIRY REPORT -----
        
        elif choice == 7:
            inv.expiry_report()

        #----- Export JSON -----

        elif choice == 8:
            export_json(inv.get_products())

        #----- IMPORT JSON -----

        elif choice == 9:
            products=import_json()
            inv=Inventory()

            for product in products:
                inv.add_loaded_product(product)

            save_inventory(inv.get_products())
            print("JSON Imported Successfully!") 

        #----- EXPORT CSV -----

        elif choice == 10:
            export_csv(inv.get_products())   

        #----- IMPORT CSV -----

        elif choice == 11:
            products=import_csv()
            inv=Inventory()

            for product in products:
                inv.add_loaded_product(product)

            save_inventory(inv.get_products())
            print("CSV Imported Successfully!")

        #------ INVENTORY STATISTICS ------

        elif choice == 12:
            inv.inventory_statistics()

        #------ SORT PRODUCTS ----

        elif choice == 13:
            print()
            print("-"*30)
            print("SORT OPTIONS")
            print("-"*30)
            print("\n1. By ID")
            print("2. By Name")
            print("3. By Quantity")
            print("4. By Category")
            print("-"* 30)

            choice=input("Enter Choice: ")
            inv.sort_products(choice)

        #----- FILTER PRODUCTS -----

        elif choice == 14:

            print("\n---- Filter Products ----")
            print("1. Filter by Category")
            print("2. Filter by Low Stock")
            print("3. Filter by Quantity Range")
            print("4. Filter by Expiry")

            ch = input("Enter Choice: ")

            products = []

            if ch == "1":
                category = input("Enter Category: ")
                products = inv.filter_category(category)

            elif ch == "2":
                products = inv.filter_lowstock()

            elif ch == "3":
                minimum = int(input("Enter Minimum Quantity: "))
                maximum = int(input("Enter Maximum Quantity: "))

                products = inv.filter_qty(minimum, maximum)

            elif ch == "4":
                days = int(input("Show products expiring within how many days? "))
                products = inv.filter_expiry(days)

            else:
                print("Invalid Choice!")
                continue

            # Check result
            if len(products) > 0:

                print("\n===== Filtered Products =====")

                for product in products:
                    product.display()

            else:

                print("\nNo products found!")

        #---- BACKUP AND RESTORE -----

        elif choice == 15:
            ch=int(input("Enter (0) for Backup and (1) for Restore: "))

            if ch == 0:
                backup_inventory()

            elif ch == 1:
                restore_inventory()

                inv=Inventory()
                products= load_products()

                for i in products:
                    inv.add_loaded_product(i)

                print("Inventory restored and loaded successfully!")

        #--- EXIT ----

        elif choice ==0:
            print("Exited!")
            break
        else:
            print("Invalid Choice!")
        print()

    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"Unexpected Error: {e}")




