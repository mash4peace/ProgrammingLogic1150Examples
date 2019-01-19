"""
Counting total value of coins
"""



pennies = 13  # User has 12 pennies
nickels = 4  # user has 4 nickels
dimes = 3  # user has 3 dimes
quarters = 7  # user has 7 quarters

nickel_value = 5
dime_value = 10
quarter_value = 25

pennies_total = pennies
nickel_total = nickels * nickel_value
dime_total = dimes * dime_value
quarter_total = quarters * quarter_value

total_cents = pennies_total + nickel_total + dime_total + quarter_total
total_dollars = total_cents / 100
print(f'The total value of coins is {total_cents} cents')
print(f'The total value of coins is ${total_dollars:.2f}')

