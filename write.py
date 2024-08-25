
def save_land(file_name, lands):
    """this function save the update on file"""
    with open(file_name, 'w') as file:
        for land in lands:
            # get details
            land_data = f"{land.kitta_number},{land.city},{land.direction},{land.anna},{land.price},{land.status}\n"
            # write in file
            file.write(land_data)
        print("file updated.")

def generate_invoice(invoice_all, transaction_type):
    # create file
    if not invoice_all:
        print("Bill data is empty")
    else:
        filename = f"transaction/{transaction_type}/{invoice_all[0]['Kitta Number']}_invoice_{transaction_type.lower()}_{invoice_all[0]['Customer_name'].lower().split()[0]}.txt"
        # Opening the file in write mode
        with open(filename, "w") as file:
            # Writing each data
            for invoice_data in invoice_all:
                # Writing the header
                file.write(f"----- {transaction_type} Invoice -----\n")
                for key, value in invoice_data.items():
                    file.write(f"{key}: {value}\n")
                # Writing a separator line
                file.write("-----------------------------\n")
            # Printing a message
            print(f"Invoice generated: {filename}")

def take_input():
    """this finction is use to take input data and handle the exception."""
    try:
        # take input
        data = int(input("Enter data: "))
        # handle negative value
        if data <= 0:
            print("data can not be negative.")
            return take_input()
        return data
    # handle exception.
    except ValueError:
        print("expecting int value, Try again.")
        return take_input()
