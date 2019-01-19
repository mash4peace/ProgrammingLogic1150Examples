"""
The good news is that you already know how to use functions.
Recap of functions we've used already

This program isn't for anything useful, it's just for examples of functions.
"""

import random


# print() is a function
print('You have used functions already!')


# input is a function that returns the data
# that you type in at the prompt
word = input('Please type some data and press enter: ')


# str() and int() and float() are functions that convert one
# type of data to another

day_of_month = int(input('What day of the month is is? '))
month = input('What month is it?')

miles_to_school = float(input('How many miles do you travel to school? '))

# Concatenating strings - must convert numbers to string
print('Today is ' + str(day_of_month) + ' of ' + month)
print('You travel ' + str(miles_to_school))

# You can do string formatting too
print(f'Today is {day_of_month} of {month}')
print(f'You travel {miles_to_school}')


# len() calculates the length of a string

assignment = 'ENGL 1001 Assignment 1. Today I read the book and it was very interesting.'
letter_count = len(assignment)


# random() for generating random numbers
# Remember to import random at the top of your program

random_number = random.randint(10)


# range() is used for creating a list of numbers to help a loop count
# the number of repetitions needed

for number in range(5):
    print(5)


# So, as you can see, you've already used many functions!