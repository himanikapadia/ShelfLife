from models.food import Food
from models.medicines import Medicines
from models.electronics import Electronics

def save_inventory(products):
    with open("inventory.txt","w") as file:
        for i in products:
            if isinstance(i,Food):
                line=(
                    f"Food|{i.get_id()}|{i.get_name()}|{i.get_qty()}|{i.get_expiry()}|{i.get_storage()}\n"
                )
            elif isinstance(i,Medicines):
                line=(
                    f"Medicines|{i.get_id()}|{i.get_name()}|{i.get_qty()}|{i.get_expiry()}|{i.get_manufacture()}|{i.get_prescription()}\n"
                )
            elif isinstance(i,Electronics):
                line=(
                    f"Electronics|{i.get_id()}|{i.get_name()}|{i.get_qty()}|{i.get_expiry()}|{i.get_warranty()}|{i.get_brand()}\n"
                )
            file.write(line)

def load_inventory():
    products=[]
    with open("data/inventory.txt","r") as file:
        for line in file:
            line=line.strip() #remove new line
            data=line.split("|")
            product_type=data[0]
            if product_type == "Food":
                product=Food(
                    int(data[1]),
                    data[2],
                    int(data[3]),
                    data[4],
                    data[5]
                )
            elif product_type == "Medicines":
                product=Medicines(
                    int(data[1]),
                    data[2],
                    int(data[3]),
                    data[4],
                    data[5],
                    data[6]
                )
            elif product_type == "Electronics":
                product=Electronics(
                    int(data[1]),
                    data[2],
                    int(data[3]),
                    int(data[4]),
                    data[5]
                )
            products.append(product)
    return products
