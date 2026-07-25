class Inventory:
    def __init__(self):
        self.__products=[]

    def add_product(self,product):
        self.__products.append(product)

    def display_products(self):
        if not self.__products:
            print("Inventory is Empty!")
        else:
            print("==== Product Details ====")
            for product in self.__products:
                product.display()

    def search_by_Id(self,product_id):  
        for p in self.__products:
            if p.get_id()==product_id:
                return p
    def search_by_name(self,name):
        for p in self.__products:
            if p.get_name()==name:
                return p
    def search_by_category(self,category):
        products=[]
        for p in self.__products:
            if p.get_category().lower()==category.lower():
                products.append(p)
        return products

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