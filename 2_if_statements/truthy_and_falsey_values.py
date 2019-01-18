""" Python considers an empty string - with no characters in - to be false. """


# An empty string is considered to be False.

text = ''  # An empty string

if text:
    print('There is text in the string.')
else:
    print('There is no text in the string.')  # This prints


# Any string with text in it is considered to be True
more_text = 'Beyonce'

if more_text:
    print('There is text in the string.')   # This prints
else:
    print('There is no text in the string.')


# The number 0 is considered to be false
number = 0

if number:
    print('number is not zero.')
else:
    print('number is zero')     # This prints


# Any other number, positive or negative, is considered to be True
number = -3

if number:
    print('number is not zero.')   # This prints
else:
    print('number is zero')

number = 100

if number:
    print('number is not zero.')  # This prints
else:
    print('number is zero')

