"""
Adding numbers using a while loop
Adding up the prices for all textbooks needed this semester
"""

total = 0
more_books = True

while more_books:
    book_price = float(input('Enter the price of a textbook: '))
    total = total + book_price
    any_more = input('Any more books? Type "Y" for yes or "N" for no: ')
    if any_more == 'N':
        more_books = False


print(f'The total of all the books is {total}')

# print('The total of all the books is ' + str(total))   # The equivalent of the line above, joining strings
