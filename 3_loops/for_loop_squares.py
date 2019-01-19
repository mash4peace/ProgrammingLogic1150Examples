"""
Printing a square with nested for loop
"""

square_size = 10
square_character = '*'

for y in range(square_size):
    line = ''
    for x in range(square_size):
        line = line + square_character
    print(line)
