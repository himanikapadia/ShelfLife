from product import Product

class Medicines(Product):
    def __init__(self, id, name, category, quantity, expiry_date,manufacturer,prescription):
        super().__init__(id, name, category, quantity, expiry_date)
        self.manufacturer=manufacturer
        self.prescription=prescription

    def display(self):
        super().display() 
        print("Category : Medicine")
        print(f"Manufacturer : {self.manufacturer}")
        print(f"Prescription Required : {self.prescription_required}")
        print("-" * 30)