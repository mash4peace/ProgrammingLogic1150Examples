""" Program that gets string, int, and float data from the user,
then does some math processing
and then prints the results, converting numbers to strings.
"""


# Get data about the items sold from the user
item_name = input('Enter name of item: ')

# Convert numerical data to the correct type
unit_price = float(input('Enter unit price of ' + item_name + ': '))
items_sold = int(input('Enter quantity of ' + item_name + ' sold: '))

# Calculate total for all items sold
total = unit_price * items_sold

# Print out invoice data
print()   # print a blank line
print(item_name + ' sales')
print('Quantity sold: ' + str(items_sold))
print('Unit price: ' + str(unit_price))
print('Total: ' + str(total))

