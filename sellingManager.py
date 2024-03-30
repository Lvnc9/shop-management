# Start
# by Sam Mohammadi

# Modules
import digitalDeviceManager as ddm
import memberManager as mm
import csv
import datetime



class SellingManager:
    """
    takes a national_code and code of 
    selected product
    
    but first takes the full information of customer
    and it's shopping
    """

    def __init__(self, device, member):
        self.device = device
        self.member = member
        self.customer_shoppings = []
        self.sold_products = []

    def shopping(self):
        national_code = input("National code of customer: ")
        product_code = int(input("Code of product: "))
        
        if self.member.search(national_code) and self.device.find(product_code):            # validation
            print("Verified!")
            number_of_goods = int(input("How many of this product you want?: "))            # buying
            self.device.buying(product_code, number_of_goods)                               # buying method of ddm
        else:
            print("didn't match anything.")
            return False

        sold_product = {
            "code" : product_code,
            "number_of_bought_goods" : number_of_goods,
            "date" : datetime.datetime.now()
        }

        self.sold_products.append(sold_product)

        product_header = ["code", "number_of_bought_goods", "date"]
        with open("./bout_items.csv", "w") as f:
                writer = csv.DictWriter(f, product_header)
                writer.writeheader()
    
                for row in self.sold_products:
                    writer.writerow(row)
        shoppin = {
            "national_code" : national_code,
            "code" : product_code,
            "number_of_goods" : number_of_goods,
            "date" : datetime.datetime.now()
        }
        self.customer_shoppings.append(shoppin)

        customer_header = ["national_code", "code", "number_of_goods", "date"]
        with open("./customer_history.csv", "w") as f:
                writer = csv.DictWriter(f, customer_header)
                writer.writeheader()
    
                for row in self.customer_shoppings:
                    writer.writerow(row)


    def customer_report(self):
        if len(self.customer_shoppings) > 0:
            print("\n\n\n")
            print("\t".join(self.customer_shoppings[0].keys()))
            for row in self.customer_shoppings:
                print("\t".join(str(x) for x in row.values()))
                print('\n')
        else:
            print("there is no saved reports")

    def product_report(self):
        if len(self.sold_products) > 0:
            print("\n\n\n")
            print("\t".join(self.sold_products[0].keys()))
            for row in self.sold_products:
                print("\t".join(str(x) for x in row.values()))
                print('\n')
        else:
            print("there is no saved reports")

# End