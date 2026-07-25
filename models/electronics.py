from models.product import Product
class Electronics(Product):
    def __init__(self, id, name,quantity,warranty_months,brand):
        super().__init__(id, name,quantity,"N/A")
        self.warranty_months=warranty_months
        self.brand=brand

    def display(self):
        super().display()
        print("Category : Electronics")
        print(f"Brand : {self.brand}")
        print(f"Warranty : {self.warranty_months} Months")
        print("-" * 30)

    def get_category(self):
        return "Electronics"

    def get_warranty(self):
        return self.warranty_months

    def get_brand(self):
        return self.brand