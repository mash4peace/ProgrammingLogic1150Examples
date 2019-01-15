"""

A shipping company charges different rates per pound, based on how heavy the package is.

If the package is 10 lbs or less, it will cost $2 per pound
If the package is 20 lbs or less, it will cost $1.50 per pound
If the package is 30 lbs or less, it will cost $1.15 per pound

The company does not ship package that weigh over 30 lbs.

Ask the user for the weight of the package. Print a message with the shipping cost if
it can be shipped, or a message saying the package can't be shipped otherwise.

"""

weight = float(input('Enter weight of package, in lbs: '))

if weight > 30:
    print('This package is too heavy to be shipped.')
elif weight <= 0:
    print('Your package can\'t have a zero or negative weight!')
else:

    if weight <= 10:
        price_per_pound = 2
    elif weight <= 20:
        price_per_pound = 1.5
    else:
        price_per_pound = 1.15


    shipping_cost = weight * price_per_pound

    print('Your ' + str(weight) + 'lb package costs $' + str(shipping_cost) + ' to ship.')
