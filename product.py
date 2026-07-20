from datetime import datetime
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
        if self.__quantity+ amount>0:
            self.__quantity+=amount
        else:
            print("Quantity Cannot be Negative!")

    def get_qty(self):
        return self.__quantity

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def is_low_stock(self):
        return self.__quantity<5

    def is_expired(self):
        expiry = datetime.strptime(self.__expiry_date, "%d-%m-%Y")
        today = datetime.today()

        return expiry < today
    def is_expiring_soon(self):
        expiry = datetime.strptime(self.__expiry_date, "%d-%m-%Y")
        today = datetime.today()

        days_left = (expiry - today).days

        return 0 <= days_left <= 7
    def days_left(self):
        expiry = datetime.strptime(self.__expiry_date, "%d-%m-%Y")
        today = datetime.today()

        return (expiry - today).days