from product import Product
class food(Product):
    def __init__(self, id, name, category, quantity, expiry_date,storage_type):
        super().__init__(id, name,quantity, expiry_date)
        self.storage_type=storage_type

    def display(self):
        super().display()  
        print("Category: FOOD")
        print(f"Storage Type: {self.storage_type}")
        print("-"*40)  