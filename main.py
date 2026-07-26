from services.inventory import Inventory
from models.product import Product
from models.food import Food
from models.medicines import Medicines
from models.electronics import Electronics
from services.file_handler import load_inventory

inv=Inventory()
products=load_inventory()
for product in products:
    inv.add_loaded_product(product)

print(f"{len(products)} products loaded successfully.\n")

#========= User Menu =========
while True:

    print("="*40)
    print("\tShelfLife V2")
    print("Terminal Inventory Management System")
    print("="*40)
    print("1. Add Product")
    print("2. View Product")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Remove Product\n")
    print("----- Reports -----")
    print("6. Check Low Stock Products")
    print("7. Expiry Report\n")
    print("----- Import/Export -----")
    print("8. Export to JSON")
    print("9. Import from JSON")
    print("10. Export from CSV")
    print("11. Import from CSV\n")
    print("0. Exit!")
    try:
        choice = int(input("Enter your Choice: "))
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
        
        elif choice == 2:
            inv.display_products()
        
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
        elif choice == 4:
            id=int(input("Enter Prouduct ID to be updated: "))
            product=inv.search_by_Id(id)
            if product:
                print("Product found!")
                amount = int(input("Enter quantity to add (+) or remove (-): "))
                product.update_qty(amount)
                print("Updated quantity: ",product.get_qty())
            else:
                print("Product ID: " ,id," Not found!")
                print("Update Unsuccessful")
        elif choice == 5:
            id=int(input("Enter Prouduct ID to be Removed: "))
            product=inv.remove_product(id)
        elif choice == 6:
            products=inv.low_stock_products()
            if products:
                print("\n==== Low Stock Products ====")
                for product in products:
                    product.display()
            else:
                print("\nNo low stock products found.")
        elif choice == 7:
            inv.expiry_report()
        elif choice ==0:
            print("Exited!")
            break
        else:
            print("Invalid Choice!")
        print()
    except Exception as e:
        print(type(e).__name__, ":", e)




