# import modules
from tabulate import tabulate
from write import save_land,generate_invoice
class Land:
    def __init__(self,kitta_number, city, direction, anna, price, status) -> None:
        """initialize the Land data"""
        self.kitta_number = kitta_number
        self.city = city
        self.direction = direction
        self.anna = anna
        self.price = price
        self.status = status
        

class Method:
    def __init__(self,file_name) -> None:
        self.file_name = file_name
        self.duration_record = {}


    def display_invoice_data(self, invoice_data_all):
        """this function display the incoice data"""
        if not invoice_data_all:
            print("No record found")
            return
        for invoice_data in invoice_data_all:
            # print the invoice data
            for key in invoice_data:
                print(f"{key} = {invoice_data[key]}")
            print("".center(70,"-"))

        
    def display_available_lands(self,lands):
        """this method display all the land that have status as 'Available'"""
        # check if lands data is available 
        if not lands:
            print("No records found.")
            return
        
        print("Available Lands".center(74,'-'))
        #make header
        header = ["Kitta number","City","Direction","Anna","Price","Status"]
        data = []
        # print(type(lands[0].kitta_number))
        # store all the land details or we can say fillter data
        for land in lands:
            if land.status.lower() == "available":
                row = [land.kitta_number,land.city,land.direction,land.anna,land.price,land.status]
                data.append(row)
        # print the data 
        print(tabulate(data, headers=header, tablefmt="grid"))
    


    def rent_land(self,lands,land,kitta_number,customer_name,duration):
        "this method create incoice for rent and also make changes in stock data that now land is not available"
        # chack status

        if land.status.lower() == "available":
            # calculate price
            price = land.price * duration
            # save duration data
            self.duration_record[kitta_number] = duration
            # update status in land_data.txt
            land.status = "Not Available"
            save_land(self.file_name,lands)
            # make dictonary to store invoice data
            invoice_data = {
                "Customer_name": customer_name,
                "Kitta Number": land.kitta_number,
                "City": land.city,
                "Direction":land.direction,
                "anna": land.anna,
                "Price per month":land.price,
                "Duration of Rent": f"{duration} months",
                "Amount": f"NPR {price}"
                }
            # return invoice data
            return invoice_data      
        else:
            print(f"Land {land.status}")
            return None
        
    def return_rent(self,lands, land, kitta_number, customer_name, duration):
        """thid methode create invoice for returning the land."""
        # check status
        if land.status.lower() != "available":
            # get months for rented duration
            rented_duration = self.duration_record[kitta_number] if kitta_number in self.duration_record else duration
            # calculate original price
            price = land.price * rented_duration
            fine_price = 0
            # check fine is aplicable or not
            if duration < rented_duration:
                final_price = land.price * duration
            elif duration > rented_duration:
                # calculate fine price
                fine_price = 0.1 * ((duration - rented_duration) * land.price) 
            final_price = price + fine_price
            # update the status
            land.status = "Available"
            # update the file
            save_land(self.file_name,lands)
            invoice_data = {
            "Customer_name": customer_name,
            "Kitta Number": land.kitta_number,
            "City": land.city,
            "Direction":land.direction,
            "anna": land.anna,
            "Price per month":land.price,
            "Duration of Rent": f"{rented_duration} months",
            "Return month":f"{duration} months",
            "Bill Amount": f"NPR {price}",
            "Delay Fine":f"NPR {fine_price}",
            "Paybal Amount":f"NPR {final_price}"
            }
            # update duration record
            self.duration_record[kitta_number] = 0
            return invoice_data
                    
        else:
            print(f"Sorry, Land {land.status}")
            return None
            