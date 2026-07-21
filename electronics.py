from product import Product
class Electronics(Product):
    def __init__(self, id, name,quantity, expiry_date,warranty_months,brand):
        super().__init__(id, name,quantity,"N/A")
        self.warranty_months=warranty_months
        self.brand=brand

    def display(self):
        super().display()
        print("Category : Electronics")
        print(f"Brand : {self.brand}")
        print(f"Warranty : {self.warranty_months} Months")
        print("-" * 30)