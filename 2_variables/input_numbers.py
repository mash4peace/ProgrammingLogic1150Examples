""" Getting number input from the user """

# Ask user for a float input. Notice that the data has to be converted to a float.
# If you want to try this out, it's 1391.25 miles from downtown Minneapolis to downtown Seattle.
miles_to_seattle = float(input('How many miles to Seattle? '))

# Do math - one mile is 1.609, so to convert miles to kilometers, multiply my 1.609.
km_to_seattle = miles_to_seattle * 1.609

# Display the answer for the user. Notice that the number has to be converted to a string for printing.
print('It is ' + str(km_to_seattle) + ' kilometers to Seattle.')

