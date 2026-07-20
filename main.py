from inventory import Inventory
from product import Product
# from food import Food
# from medicine import Medicine
# from electronics import Electronics
inv=Inventory()

p1=Product(
    id=101,
    name="Milk",
    category="Food",
    quantity=2,
    expiry_date="18-08-2026"
)
inv.add_product(p1)

#========= User Menu =========
while True:

    print("="*40)
    print("\tShelfLife V1")
    print("Terminal Inventory Management System")
    print("="*40)
    print("1. Add Product")
    print("2. View Product")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Remove Product")
    print("6. Check Low Stock Products")
    print("7. Expiry Report")
    print("8. Exit!")
    try:
        choice = int(input("Enter your Choice: "))
        if choice == 1:
            print("~ Enter Product Details ~")
            pid=int(input("ID: "))
            pname=input("Name: ")
            category=input("Category: ")
            qty=int(input("Quantity: "))
            exp=input("Expiry Date (DD-MM-YYYY): ")
    
            product=Product(pid,pname,category,qty,exp)
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
        elif choice ==8:
            print("Exited!")
            break
        else:
            print("Invalid Choice!")
        print()
    except ValueError:
        print("Please enter a valid number!")




