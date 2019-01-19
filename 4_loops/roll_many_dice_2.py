import random

# It's often a good idea to save all of your program's data in variables
number_of_dice = 5

# Using variables instead of the number 5 makes it easier to reuse
# and then if you need to roll 3 or 10 dice, you just need to
# change the number on line 4 once, instead of changing the number everywhere
print(f'About to roll {number_of_dice} dice...')

for dice in range(number_of_dice):
    dice_value = random.randint(1, 6)
    print(dice_value)


