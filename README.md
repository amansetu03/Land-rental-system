## Algorithm
  - Step-1: start
  - Step-2: Read land data from land_data.txt file
  - Step-3: Ask user to which operation they want to perform.
  - Step-4: take choice if choice is taking rant land
  - Step-5: ask user to which land they want to take rent then search kitta number that the land is exist in land data or not
  - Step-6: if land is available then ask user for duration and make changes in land_data.txt file land status “Available” to “Not Available”
  - Step 7: if user want to rent more land at same time, then again take required otherwise generate the invoice
  - Step 8: again, ask for user to chose which operation they want to perform and same step follow for return land 
  - Step-9: when user return the land then the land status change “Not Available” to “Available”
  - Step-10: it displays all the available data when user chose to display available land
  - Step11: if user chose close program, then the program stopped.
  - Step 12: stop.

## Flowchart
<img src="https://github.com/user-attachments/assets/9f8a1afc-a0a4-4a63-af43-535a43cc9f36" width="55%">

## PseudoCode
1.	Load_land :
	```Create empty list lands = []
	Open land_data.txt as file
	Loop in file:
		Create object of Land that store individual land data 
		Append object in lands list```
2.	Rent_land:
  ```If land.status == “available”:
    Price = land_price * duration
  Land`.status = “Not available”
  Save update
  Return invoice_data
  ```
3.	return_rent:
  ```if find land then check
  if land.status == “Available” 
  	find delay fine 
  total_price = price + fine_price
  update land.status = "Available"
  save the file 
  generate invoice
  ```
4.	display_available land:
  ```loop in lands:
  	if land.status == “Available”
  	print land details
  ```
5.	gentrate_invoice
 ``` create file with unique name 
  loop in all invoice data
  write all invoice data
  save file.
 ```
6.	Take_input
  	```Try: 
	   Data = int( Input())
	    If data < 0:
		Print negative value and again take input
	Except valueError
	    Print error take input again```

## Input/Output

### input
<img src="https://github.com/user-attachments/assets/a4a3e6cf-d42c-4c43-acbb-675473dcf5e6" width="50%">

### output
<img src="https://github.com/user-attachments/assets/1105ef3f-10f9-44db-911b-ee813d3ca50d" width="50%">
<br>
<a href="/transaction">Tranjuction Folder</a>
