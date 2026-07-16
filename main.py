class Product:
    def __init__(self,name,category,id,quantity,expiry_date):
        self.name=name
        self.category=category
        self.__id=id
        self.__quantity=quantity
        self.__expiry_date=expiry_date
    
    def display(self):
        print("==== Product Details ====")
        print(f"Id: {self.__id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Quantity: {self.__quantity}")
        print(f"Expiry Date: {self.__expiry_date}")

    def update_qty(self,amount):
        self.__quantity+=amount

    def get_id(self):
        return self.__id

    def is_low_stock(self):
        return self.__quantity<5

class Inventory:
    def __init__(self):
        self.__products=[]

    def add_products(self,product):
        self.__products.append(product)

    def display_product(self):
        for product in self.__products:
            product.display()

    def search_product(self,product_id):  #search by ID
        for p in self.__products:
            if p.get_id()==product_id:
                print("--- Product found! ---")
                return p
            else:
                return none



