"""
Generate random numbers for the user
Emulate rolling a dice, until user wants to quit
"""

import random

want_to_quit = False

while not want_to_quit:
    dice_value = random.randint(1, 6)

    print(f'You rolled a {dice_value}')

    want_to_quit = input('Press enter to roll again, any other key to quit ')

