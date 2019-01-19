"""
Add up all textbook prices with a for loop
"""

# How many books does the user need to buy?
number_of_books = int(input('How many books to buy? '))

# Create a variable for the total, set to zero
total = 0

# Loop needs to repeat once per book
for book in range(number_of_books):
    book_price = float(input('Enter book price $'))
    # Price is zero, the book was free. Print a message.
    if book_price == 0:
        print('Yay, free book!')
    # Add latest book price to total
    total = total + book_price

print(f'The total price for all {number_of_books} books is ${total}')


