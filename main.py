class Product:
    def __init__(self,id,name,category,quantity,expiry_date):
        self.__id=id
        self.name=name
        self.category=category
        self.__quantity=quantity
        self.__expiry_date=expiry_date
    
    def display(self):
        print("-"*30)
        print(f"Id: {self.__id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Quantity: {self.__quantity}")
        print(f"Expiry Date: {self.__expiry_date}")
        print("-"*30)

    def update_qty(self,amount):
        self.__quantity+=amount

    def get_qty(self):
        return self.__quantity

    def get_id(self):
        return self.__id

    def is_low_stock(self):
        return self.__quantity<5

class Inventory:
    def __init__(self):
        self.__products=[]

    def add_products(self,product):
        self.__products.append(product)
        print("\nProduct Added Successfully!!")

    def display_products(self):
        print("==== Product Details ====")
        for product in self.__products:
            product.display()

    def search_product(self,product_id):  #search by ID
        for p in self.__products:
            if p.get_id()==product_id:
                return p

    def remove_product(self,id):
        for p in self.__products:
            if p.get_id()==id:
                self.__products.remove(p)
                print(f"Product: {id} is Removed Successfully!")
                return True
        print("Failed Remove!")
        return False
    def low_stock_products(self):
        low_stock=[]
        for product in self.__products:
            if product.is_low_stock():
                low_stock.append(product)
        return low_stock

inv=Inventory()

p1=Product(
    id=101,
    name="Milk",
    category="Food",
    quantity=2,
    expiry_date="18-08-2026"
)
inv.add_products(p1)

#========= User Menu =========
while True:

    print("---- ShelfLife ----")
    print("1. Add Product")
    print("2. View Product")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Remove Product")
    print("6. Check Low Stock Products")
    print("7. Exit!")
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
            inv.add_products(product)
        
        elif choice == 2:
            inv.display_products()
        
        elif choice == 3:
            id=int(input("Enter product ID to search: "))
            product=inv.search_product(id)
            if product:
                print("\nProduct found!")
                product.display()
            else:
                print("\nProduct Not found!")
        elif choice == 4:
            id=int(input("Enter Prouduct ID to be updated: "))
            product=inv.search_product(id)
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
        else:
            print("Exited!")
            break
        print()
    except ValueError:
        print("Please enter a valid number!")




