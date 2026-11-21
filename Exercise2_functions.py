def calculate_sales(quantity, unit_price):
    return quantity * unit_price

result = calculate_sales(3, 1200.50)
print("****** Sales calculation ******")
print("Total Sales:", result)

# Step 2 - Reuse the function with different values
print("****** Reusing Function with Different Values ******")
print("Total Sales for 5 units at $1500.75 each:", calculate_sales(5, 1500.75))
print("Total Sales for 2 units at $800.00 each:", calculate_sales(2, 800.00))
print("Total Sales for 10 units at $250.25 each:", calculate_sales(10, 250.25))

#Step 3 - Check and convert data types
print("")
print("****** Data Type Check and Conversion ******")
quantity = "5" # string variable
print("Original quantity (string):", quantity)
quantity = int(quantity) # convert string to integer
print("Converted quantity (int):", quantity)
print("Total Sales after conversion:", calculate_sales(quantity, 500)) # call function

# Step 4 – Store multiple values in a List
sales = [1200, 850, 2400, 1750, 3200]
print("")
print("****** Store multiple values in a  list")
print("Sales:", sales)
print("First sale:", sales[0]) #indexing
print("Number of sales:", len(sales))