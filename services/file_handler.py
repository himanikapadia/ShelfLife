from models.food import Food
from models.medicines import Medicines
from models.electronics import Electronics
import json
import csv
import shutil

def save_inventory(products):
    with open("data/inventory.txt","w") as file:
        for i in products:
            if isinstance(i,Food):
                line=(
                    f"Food|{i.get_id()}|{i.get_name()}|{i.get_qty()}|{i.get_expiry()}|{i.get_storage()}\n"
                )
            elif isinstance(i,Medicines):
                line=(
                    f"Medicines|{i.get_id()}|{i.get_name()}|{i.get_qty()}|{i.get_expiry()}|{i.get_manufacturer()}|{i.get_prescription()}\n"
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

def export_json(products):
    data =[]
    for product in products:
        if product.get_category() == "Food":

            data.append({
                "type": "Food",
                "id": product.get_id(),
                "name": product.get_name(),
                "quantity": product.get_qty(),
                "expiry": product.get_expiry(),
                "storage": product.get_storage()
            })
        elif product.get_category() == "Medicines":
            data.append({
                "type": "Medicines",
                "id": product.get_id(),
                "name": product.get_name(),
                "quantity": product.get_qty(),
                "expiry": product.get_expiry(),
                "manufacturer": product.get_manufacturer(),
                "prescription": product.get_prescription()
            })
        elif product.get_category() == "Electronics":
            data.append({
                "type": "Electronics",
                "id": product.get_id(),
                "name": product.get_name(),
                "quantity": product.get_qty(),
                "brand": product.get_brand(),
                "warranty": product.get_warranty()
            })

    #print(data)
    with open("data/inventory.json","w") as file:
        json.dump(data,file,indent=4)

    print("Inventory exported to JSON successfully!")

def import_json():
    products=[]

    with open("data/inventory.json","r")as file:
        data=json.load(file)

        for i in data:
            if i["type"]=="Food":
                product=Food(
                    i["id"],
                    i["name"],
                    i["quantity"],
                    i["expiry"],
                    i["storage"]
                )
            elif i["type"]=="Medicines":
                product=Medicines(
                    i["id"],
                    i["name"],
                    i["quantity"],
                    i["expiry"],
                    i["manufacturer"],
                    i["prescription"]
                )
            elif i["type"]=="Electronics":
                product=Electronics(
                    i["id"],
                    i["name"],
                    i["quantity"],
                    i["warranty"],
                    i["brand"]
                )
            else:
                continue
            products.append(product)

    return products
def export_csv(products):
    with open("data/inventory.csv","w",newline="") as file:
        writer=csv.writer(file)

        writer.writerow([
            "Type",
            "ID",
            "Name",
            "Quantity",
            "Expiry",
            "Extra1",
            "Extra2"
        ])

        for product in products:
            if product.get_category()=="Food":
                writer.writerow([
                    "Food",
                    product.get_id(),
                    product.get_name(),
                    product.get_qty(),
                    product.get_expiry(),
                    product.get_storage(),
                    ""
                ])
            elif product.get_category()=="Medicines":
                writer.writerow([
                    "Medicines",
                    product.get_id(),
                    product.get_name(),
                    product.get_qty(),
                    product.get_expiry(),
                    product.get_manufacturer(),
                    product.get_prescription()
                ])

            elif product.get_category()=="Electronics":
                writer.writerow([
                    "Electronics",
                    product.get_id(),
                    product.get_name(),
                    product.get_qty(),
                    product.get_warranty(),
                    product.get_brand(),
                    ""
                ])

    print("Inventory exported to CSV Successfully")

def import_csv():
    products=[]

    with open("data/inventory.csv","r") as file:
        reader=csv.reader(file)

        next(reader)

        for row in reader:
            if row[0]=="Food":
                product=Food(
                    int(row[1]),
                    row[2],
                    int(row[3]),
                    row[4],
                    row[5]
                )
            elif row[0]=="Medicines":
                product=Medicines(
                    int(row[1]),
                    row[2],
                    int(row[3]),
                    row[4],
                    row[5],
                    row[6]
                )
            elif row[0]=="Electronics":
                product=Electronics(
                    int(row[1]),
                    row[2],
                    int(row[3]),
                    int(row[4]),
                    row[5]
                )
            else:
                continue
            products.append(product)

    return products

def backup_inventory():
    shutil.copy("data/inventory.txt","data/backup.txt")
    print("Inventory backup created successfully!")

def restore_inventory():
    shutil.copy("data/backup.txt", "data/inventory.txt")
    print("Inventory restored successfully!")