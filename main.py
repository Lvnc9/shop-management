# Start
# by Sam Mohammadi
# Modules
import digitalDeviceManager as ddm
import memberManager as mm
import sellingManager as sm
import os

products = ddm.DeviceManager()
users = mm.MemberManager()
sellings = sm.SellingManager(products, users)

def space():
    print(""" 
    \n\n\n\n
    """)

def screen():
    corr_answ_menue1 = (1, 2, 3, 4)
    menue1 = int(input(""" 
        digital device manager: 1
        member manager:         2
        selling manager:        3
        reports:                4
        """))

    while not menue1 in corr_answ_menue1:
        menue1 = int(input(""" 
            digital device manager: 1
            member manager:         2
            selling manager:        3
            reports:                4
            """))
    if menue1 == 1:
        space()
        corr_answ_menue2 = (1, 2, 3, 4, 5, 6)
        menue2 = int(input(""" 
            add_devices:            1
            edit:                   2
            find:                   3
            remove:                 4
            show_file:              5
            save_devices:           6
            """))
        
        while not menue2 in corr_answ_menue2:
            menue2 = int(input(""" 
                add_devices:            1
                edit:                   2
                find:                   3
                remove:                 4
                show_file:              5
                save_devices:           6
                """))

        if menue2 == 1:                             # checking different inputs and scenarios
            products.add_devices()                  # Adding devices 
        elif menue2 == 2:
            products.edit()
        elif menue2 == 3:
            products.find()
        elif menue2 == 4:
            products.remove()
        elif menue2 == 5:
            products.show_file()
        elif menue2 == 6:
            products.save_devices()

    elif menue1 == 2:
        space()
        corr_answ_menue3 = (1, 2, 3)
        menue3 = int(input(""" 
            add_members:            1
            edit_profile:           2
            search:                 3
            """))
        
        while not menue3 in corr_answ_menue3:
            menue3 = int(input(""" 
                add_members:            1
                edit_profile:           2
                search:                 3
                """))
        if menue3 == 1:
            users.add_members()
        elif menue3 == 2:
            users.edit_profile()
        elif menue3 == 3:
            users.search()

    elif menue1 == 3:
        space()
        corr_answ_menue4 = (1)
        menue4 = int(input(""" 
            shopping:               1
            """))
        
        while not menue4 == corr_answ_menue4:
            menue4 = int(input(""" 
                shopping:               1
                """))
        sellings.shopping()

    elif menue1 == 4:
        space()
        corr_answ_menue5 = (1, 2)
        menue5 = int(input("""
            customer_report:        1
            customer_shoppings:     2
            """))
        while not menue5 in corr_answ_menue5:
            menue5 = int(input("""
                customer_report:        1
                customer_shoppings:     2
                """))
            
        if menue5 == 1:
            sellings.customer_report()
        elif menue5 == 2:
            sellings.product_report()
        
def main():
    while True:
        screen()

main()
# End   