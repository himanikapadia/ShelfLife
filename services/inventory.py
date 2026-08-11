from services.file_handler import save_inventory
from services.database import insert_product
from datetime import datetime
from services.database import update_qty
from services.database import delete_product
from services.database import search_by_id, search_by_name, search_by_category

class Inventory:
    def __init__(self):
        self.__products=[]

    # Add product

    def add_product(self,product):
        self.__products.append(product)
        insert_product(product)

    # Prevent Duplicate Ids

    def id_exists(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return True
        return False

    # Update Qty

    def update_product_qty(self, product_id, amount):

        product = self.search_by_Id(product_id)

        if product:
            if product.update_qty(amount):
                update_qty(product_id,product.get_qty())
                return True

        return False

    # Display Products

    def display_products(self):
        if not self.__products:
            print("Inventory is Empty!")
        else:
            print("==== Product Details ====")
            for product in self.__products:
                product.display()

    def get_products(self):
        return self.__products

    #SEARCH FUNCTIONS

    def search_by_Id(self,product_id):  
         return search_by_id(product_id)
        
    def search_by_name(self,name):
         return search_by_id(name)
        
    def search_by_category(self,category):
         return search_by_id(category)

    def add_loaded_product(self, product):
        self.__products.append(product)

    # Remove Products

    def remove_product(self,product_id):
        if delete_product(product_id):

            self.__products = [
                product for product in self.__products
                if product.get_id() != product_id
            ]
            print("Product Removed successfully!")
            return True
        print("Failed Remove!")
        return False

    # Low Stock Products
    
    def low_stock_products(self):
        low_stock=[]
        for product in self.__products:
            if product.is_low_stock():
                low_stock.append(product)
        return low_stock

    # Expiry Report
    
    def expiry_report(self):
        print("\n====== Expiry Report ======")
        for product in self.__products:
            if product.get_category().lower() == "electronics":
                continue
            days = product.days_left()
            product.display()
            if days < 0:
                print("Expired")
            elif days == 0:
                print("⚠ Expires Today")
            elif days <= 7:
                print(f"⚠ Expires in {days} day(s)")
            else:
                print(f"{days} day(s) remaining")
            print()

    # Inventory Statistics

    def inventory_statistics(self):
        total_products=len(self.__products)
        total_qty=0
        food =0
        medicines=0
        electronics=0

        low_stock=0
        expired=0

        for product in self.__products:
            total_qty += product.get_qty()

            category = product.get_category()

            if category == "Food":
                food+=1
            elif category =="Medicines":
                medicines+=1
            elif category == "Electronics":
                electronics += 1

            if product.is_low_stock():
                low_stock += 1

            # Electronics don't expire
            if category != "Electronics":
                if product.days_left() < 0:
                    expired += 1

        print("\n" + "=" * 40)
        print("      INVENTORY STATISTICS")
        print("=" * 40)
        print(f"Total Products     : {total_products}")
        print(f"Total Quantity     : {total_qty}")
        print(f"Food Items         : {food}")
        print(f"Medicine Items     : {medicines}")
        print(f"Electronics Items  : {electronics}")
        print(f"Low Stock Products : {low_stock}")
        print(f"Expired Products   : {expired}")
        print("=" * 40)

    # SORT FUNCTIONS

    def sort_products(self,choice):
        if not self.__products:
            print("Inventory Is Empty!!")
            return

        if choice == "1":
            self.__products.sort(key=lambda x: x.get_id())
            print("Products Sorted by ID.")

        elif choice == "2":
            self.__products.sort(key=lambda x: x.get_name())
            print("Products Sorted by Name.")

        elif choice == "3":
            self.__products.sort(key=lambda x: x.get_qty())
            print("Products Sorted by Quantity.")

        elif choice == "4":
            self.__products.sort(key= lambda x: x.get_category())
            print("Producrs Sorted by Category.")

        else:
            print("Invalid Choice!")
            return

        for x in self.__products:
            x.display()

    # Filter Functions

    def filter_category(self,category):

        filtered=[]
        # by category
        for product in self.__products:
            if product.get_category().lower()==category.lower():
                filtered.append(product)

        return filtered

    def filter_lowstock(self):

        filtered=[]
        for product in self.__products:
            if product.is_low_stock():
                filtered.append(product)

        return filtered

    def filter_qty(self,min,max):

        filtered=[]
        for product in self.__products:
            qty=product.get_qty()

            if min<=qty<=max:
                filtered.append(product)

        return filtered

    def filter_expiry(self,days):
        filtered=[]

        for product in self.__products:
            if product.get_category()=="Electronics":
                continue
            if product.days_left()<=days:
                filtered.append(product)

        return filtered

