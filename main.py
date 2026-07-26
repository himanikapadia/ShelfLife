from services.inventory import Inventory
from models.product import Product
from models.food import Food
from models.medicines import Medicines
from models.electronics import Electronics
from services.file_handler import (
    load_inventory,
    export_json,
    import_json,
    export_csv,
    import_csv
)
from utils.menu import show_menu

# Initialize Inventory

inv=Inventory()
products=load_inventory()
for product in products:
    inv.add_loaded_product(product)

print("=" * 40)
print("Welcome to ShelfLife V2")
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
            pid=int(input("ID: "))
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
                id=int(input("Enter product ID to search: "))
                product=inv.search_by_Id(id)
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
            id=int(input("Enter Prouduct ID to be updated: "))
            product=inv.search_by_Id(id)
            if product:
                print("Product found!")
                amount = int(input("Enter quantity to add (+) or remove (-): "))
                if inv.update_product_qty(pid, amount):
                    product = inv.search_by_Id(pid)
                    print("\nQuantity Updated Successfully!")
                    print("Current Quantity:", product.get_qty())
            else:
                print("Product ID: " ,id," Not found!")
                print("Update Unsuccessful")

        # ----- REMOVE -----

        elif choice == 5:
            id=int(input("Enter Prouduct ID to be Removed: "))
            product=inv.remove_product(id)

        # ---- LOW STOCK -----

        elif choice == 6:
            products=inv.low_stock_products()
            if products:
                print("\n==== Low Stock Products ====")
                for product in products:
                    product.display()
            else:
                print("\nNo low stock products found.")

        #----- EXPIRY REPORT -----
        
        elif choice == 7:
            inv.expiry_report()
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




