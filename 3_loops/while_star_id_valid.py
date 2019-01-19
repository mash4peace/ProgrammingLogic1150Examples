"""
Validation for StarID - checking if 8 characters

To do, in the future - check if it's the right pattern of characters, aa1234bb
"""

star_id = input('Enter your StarID: ')

while len(star_id) != 8:
    print('Error - a valid StarID has 8 characters.')
    star_id = input('Please enter your StarID: ')

print(f'Thank you, your StarID is {star_id}')


