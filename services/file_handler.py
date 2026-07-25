from models.food import Food
from models.medicines import Medicines
from models.electronics import Electronics

def save_inventory(products):
    with open("inventory.txt","w") as file:
        for i in products:
            if isinstance(i,Food):
                line=(
                    f"Food | {i.get_id()} | {i.get_name()} | {i.get_qty()} | {i.ex}"
                )