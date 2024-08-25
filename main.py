# import modules
from operations import Method
from read import load_land
from write import take_input,generate_invoice

# initialize file name and method instance
file_name = "land_data.txt"
method_instance = Method(file_name)
lands = load_land("land_data.txt")

# print menu
print("1. Rent land.")
print("2. Return land.")
print("3. Display available lands")
print("4. Quit")


# run loop for performing operation untill user want
while True:
    # take choice from menu
    choice = input("Enter choice: ").strip()
    if choice == "1":
        invoivce_all = []
        while True:
            # take input kitta number
            print("Enter kitta number")
            kitta_number = take_input()
            # search kitta number in land data
            for land in lands:
                # check kitta number found or not
                if land.kitta_number == kitta_number:
                    # take required data for rent
                    customer_name = input("Enter customer name: ")
                    print("Enter duration in months")
                    duration = take_input()
                    # call the function rent_land for genrating bill
                    invoice_data = method_instance.rent_land(lands,land,kitta_number,customer_name,duration)
                    if invoice_data != None:
                        invoivce_all.append(invoice_data)
                    break
            else:
                print("Land not Found")
            option = input("Do you want to continue Y/N?").strip().lower()
            if option == 'y':
                continue
            else:
                # gentare the bill
                generate_invoice(invoivce_all,"rent")
                # display the bill
                print("".center(70,"-"))
                method_instance.display_invoice_data(invoivce_all) 
                break
            
            
    elif choice == "2":
        invoivce_all = []
        customer_name = ""
        while True:
            # take input kitta number
            print("Enter kitta number: ")
            kitta_number = take_input()
            # search kitta number in land data
            for land in lands:
                # check found or not
                if land.kitta_number == kitta_number:
                    # take input requred data like customer name and returned monts
                    customer_name = input("Enter customer name: ")
                    print("Enter return months")
                    return_months = take_input()
                    # call function to return land.
                    invoice_data = method_instance.return_rent(lands,land,kitta_number,customer_name,return_months)
                    if invoice_data != None:
                        invoivce_all.append(invoice_data)
                    break
            else:
                print("Land not found.")

            option = input("Do you want to continue Y/N?").strip().lower()
            if option == 'y':
                continue
            else:
                # gentare the bill
                generate_invoice(invoivce_all,"rent_return")
                # display all bill
                print("".center(70,"-"))
                method_instance.display_invoice_data(invoivce_all)
                break

    elif choice == "3":
        # call the function to display all tha availabal lands
        method_instance.display_available_lands(lands)
    elif choice == "4":
        print("Program ended. Thank you")
        break
    else:
        print("Invalid input. Try again.")
    