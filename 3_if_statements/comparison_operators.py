""" Examples of using all the comparison operators """

# Using the equals operator to check if a number is equal to another number
book_price = float(input('Enter the price of the textbook: '))
if book_price == 0:
    print('Cool! Your book is free.')

# Using the equals operator to check if a string is equal to another string
college = input('Enter the college you attend: ')
if college == 'Minneapolis College':
    print('Great choice. Glad you are taking classes here at Minneapolis College.')

# Using the not equals operator != to check if a number is different to another number
answer = int(input('Quiz time. How many cents in a dollar? '))
if answer != 100:
    print('Sorry, that is the wrong answer. There are 100 cents in a dollar.')

# Using the not equals operator != to check if a string is different to another string
password = input('Please enter your new password. It cannot be "kittens". ')
if password != 'kittens':
    print('Your new password is accepted. ')


# Using the greater than > operator to check if a number is greater (larger) than another number
temperature = float(input('Enter the number of students in class'))
if temperature > 32:
    print('The temperature is above freezing. ')


# Using the less than than < operator to check if a number is less (smaller) than another number
students = int(input('There can be a maximum of 30 students in this class. Enter the number of students in class'))
if students < 30:    # This is False if students is 30
    print('There is space left in the class.')


# Using the greater than or equal to >= operator to check if a number is greater (larger) or equal to another number
age = int(input('To become President of the USA, you need to be at least 35 years old. Please enter your age: '))
if age >= 35:
    print('You are old enough to be President.')


# Using the less than or equal to <= operator to check if a number is less (smaller) or equal to another number
number_of_pennies = int(input('Enter the number of pennies you have'))
if number_of_pennies <= 100:
    print('You have a dollar or less in pennies')


