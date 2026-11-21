# Step 1 - creating and run python files
print("******Python foundations lab started******") # print function

# Step 2 - Create variables and data files

product = "Laptop" #string
quantity = 1000 #int var
unit_price = 10.5 #float var
in_stock = True # boolean

print("Product:", product)
print("quantity:", quantity)
print("unit_price:", unit_price)
print("in_stock:", in_stock)

print("jaki typ dla Product:", type(product))

# Step 3 - Perform a sales  calculation

total_sales = quantity * unit_price #calculate total sales
print("Total sales:", total_sales )

# Step 4 Apply conditional statements

if total_sales >= 2000:
    print("Sales target achieved!")
else:
    print("Sales target not achieved. Keep trying!")

#Step 5 - Process Multiple Sales using loop

sales = [1200, 1500, 3000] # list of sales amount
print("******Processing multiple sales*****")
for sale in sales:
    if sale >=2000:
        print(f"sale amount {sale} - Target achieved!")
    else:
        print(f"Sale amount {sale} - Target not achieved!")