from product import Product
class Food(Product):
    def __init__(self, id, name,quantity, expiry_date,storage_type):
        super().__init__(id, name,quantity, expiry_date)
        self.storage_type=storage_type

    def display(self):
        super().display()  
        print("Category: FOOD")
        print(f"Storage Type: {self.storage_type}")
        print("-"*30)  

    def get_category(self):
        return "Food"