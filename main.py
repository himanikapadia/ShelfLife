class Product:
    def __init__(self,name,category,id,quantity,expiry_date):
        self.name=name
        self.category=category
        self.__id=id
        self.__quantity=quantity
        self.__expiry_date=expiry_date
    
    def display_product(self):
        print("==== Product Details ====")
        print(f"Id: {self.__id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Quantity: {self.__quantity}")
        print(f"Expiry Date: {self.__expiry_date}")

    def update_qty(self,amount):
        self.__quantity+=amount

    def is_low_stock(self):
        return self.__quantity<5



