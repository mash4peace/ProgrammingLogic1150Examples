"""
Checking if a class code matches the pattern of a valid class code
Valid class codes (eg. SPAN 1000 or ITEC 2560 or WEBI 1345 ) have
four uppercase letters, a space, then four numbers.

Uses regex patterns to validate the user has entered a valid class code.
More info: https://docs.python.org/3/library/re.html
"""

import re

class_code = input('Enter class code: ')

class_code_pattern = re.compile('[A-Z]{4} [\d]{4}')

while not class_code_pattern.fullmatch(class_code):
    print('Error - a valid class code must be four uppercase letters, space, four numbers. Example: "ITEC 1150"')
    class_code = input('Please enter the class code: ')

print('Thank you, the class code you entered is valid.')