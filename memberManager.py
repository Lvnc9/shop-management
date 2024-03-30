# Start
# by Sam Mohammadi

# Modules
import pprint
import csv

class MemberManager:
    """ 
    manage the constent customers
    """

    def __init__(self):
        self.members = []

    def add_members(self):
        flag = 1
        
        name = input("Name of customer: ")
        lname = input("Last name of customer: ")
        national_code = input("National code of customer: ")
        phone_number = input("Phone number of customer: ")

        #if len(self.members) > 0:
        #    for elem in self.members:
        #        if elem.get("national_code") != national_code:
        #            flag = 0
        #
        if len(self.members) > 0:
            for elem in self.members:
                ss = elem.get("national_code")
                if ss == national_code:
                    flag = 0
        
        if flag == 1:    
            customer = {
                "name" : name,
                "Last_name" : lname,
                "national_code" : national_code,
                "phone_number" : phone_number
            }
            self.members.append(customer)

            header = ["name", "Last_name", "national_code", "phone_number"]
            with open("./customer.csv", "w") as f:
                writer = csv.DictWriter(f, header)
                writer.writeheader()
    
                for row in self.members:
                    writer.writerow(row)

    def edit_profile(self):
        national_code = input("National code of customer: ")
        edited = False
        if len(self.members) > 0:
            for elem in self.members:
                ss = elem.get("national_code")
                if ss == national_code:
                    print(pprint.pprint(elem))
                    print("\n\n\n")
                    self.add_members()
                    edited = True
            if not edited:
                print("profile not found!\n")

    def search(self, national_code=""):
        if not national_code:
            national_code = input("National code of customer: ")
        
        if len(self.members) > 0:
            for elem in self.members:
                ss = elem.get("national_code")
                if ss == national_code:
                    print("profile exists:\n")
                    print(pprint.pprint(elem))
                    return True

# End