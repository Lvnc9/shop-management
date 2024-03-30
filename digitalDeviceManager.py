# Start
# Modules
import pprint
import pandas as pd
import csv


class DeviceManager:
    """ 
    adds,
    edits,
    removes,
    searches,
    shows all the digital devices
    """

    #PHONE, TV = ("DEACTIVE", "DEACTIVE") 

    def __init__(self):
        self.devices = []

    def add_devices(self):
        answer = ("yes", "no")

        phone = input("is it a Mobile phone?[yes/no]").lower()
        while not phone in answer:
            phone = input("is it a Mobile phone?[yes/no]").lower()
        
        if phone == "yes":
            DeviceManager.PHONE = "ACTIVE"

            phone_size = float(input("size of mobile phone: "))
            phone_color = input("color of mobile phone: ")
        
        tv = input("is it a Tv?[yes/no]").lower()
        while not tv in answer:
            tv = input("is it a Tv?[yes/no]").lower()
        
        if tv == "yes":
            DeviceManager.TV = "ACTIVE"

            tv_size = float(input("Size of Tv: "))
            tv_color = input("Color of Tv: ")

        name = input("Name of product: ")
        code = int(input("Code of product: "))
        brand = input("brand of product: ")
        n = int(input("number of products: "))
        details = input("Details and description: ")
        price = float(input("price of product: "))

        if phone != "yes" and tv == "yes":
            product = {
                "name" : name,
                "code" : code,
                "brand" : brand,
                "n" : n,
                "details" : details,
                "price" : price,
                "tv_size" : tv_size,
                "tv_color" : tv_color,
            }
        
        elif phone == "yes" and tv != "yes":
            product = {
                "name" : name,
                "code" : code,
                "brand" : brand,
                "n" : n,
                "details" : details,
                "price" : price,
                "phone_size" : phone_size,
                "phone_color" : phone_color,
            }
        elif phone == "yes" and tv == "yes":
            product = {
                "name" : name,
                "code" : code,
                "brand" : brand,
                "n" : n,
                "details" : details,
                "price" : price,
                "tv_size" : tv_size,
                "tv_color" : tv_color,
                "phone_size" : phone_size,
                "phone_color" : phone_color,
            }
        else:
            product = {
                    "name" : name,
                    "code" : code,
                    "brand" : brand,
                    "n" : n,
                    "details" : details,
                    "price" : price,
             }
       
        self.devices.append(product)

    def edit(self):               # editting the full profile of devices
        indx = 0

        code = int(input("Code of product: "))
        for idx in self.devices:
            for key, value in idx.items():
                if key == "code" and value == code:
                    print("\nprofile founded!")
                    del self.devices[indx]
                    self.add_devices()
                    return True
            indx += 1

    def buying(self, code, cost):
        indx = 0
        counter = 0
        for idx in self.devices:
            for elem in idx:
                if code == code:
                    indx = counter
            counter += 1
        number = self.devices[indx].get("n")
        number = number - cost
        #self.devices[indx].setdefault("n", number)
        self.devices[indx]["n"] = number

    def remove(self):
        indx = 0

        code = int(input("Code of product: "))
        n = int(input("number of products: "))
        for idx in self.devices:
            for key, value in idx.items():
                if key == "code" and value == code:    
                    new_number = self.devices[indx].get("n")
                    new_number = new_number - n
                    if new_number > 0:
                        print("Successfully bought")
                        self.devices[indx]["n"] = new_number
                    else:
                        print("to much items!")
            indx += 1
                        
    def find(self, code=0, name=""):
        indx = 0
        
        if not name:
            name = input("Name of product: ")
        if not code:
            code = int(input("Code of product: "))
        
        for idx in self.devices:
            for key, value in idx.items():
                if key == "code" and value == code:
                    print(pprint.pprint(self.devices[indx]))
                    return True
                elif key == "name" and value == name:
                    print(pprint.pprint(self.devices[indx]))
                    return True
            indx += 1

    def save_devices(self):                # turn it to csv file and than edit it with pandaas 
        if DeviceManager.PHONE == "DEACTIVE" and DeviceManager.TV == "ACTIVE":
            header = [
                    "name",
                    "code", 
                    "brand", 
                    "n", 
                    "details", 
                    "price", 
                    "tv_size", 
                    "tv_color"
                    ]
        elif DeviceManager.PHONE == "ACTIVE" and DeviceManager.TV == "DEACTIVE":
            header = [
                    "name",
                    "code", 
                    "brand", 
                    "n", 
                    "details", 
                    "price", 
                    "phone_size", 
                    "phone_color"
                    ]
            
        elif DeviceManager.PHONE and DeviceManager.TV == "ACTIVE":
            header = [
                "name",
                "code", 
                "brand", 
                "n", 
                "details", 
                "price", 
                "tv_size", 
                "tv_color",
                "phone_size",
                "phone_color",
                ]
        else:
            header = [
                "name", 
                "code", 
                "brand", 
                "n", 
                "details", 
                "price"
                ]
        with open("./items.csv", "w") as f:
            writer = csv.DictWriter(f, header)
            writer.writeheader()

            for row in self.devices:
                writer.writerow(row)
    
    def show_file(self):
        print("\n\n\n")
        print("\t".join(self.devices[0].keys()))
        for row in self.devices:
            print("\t".join(str(x) for x in row.values()))

# End