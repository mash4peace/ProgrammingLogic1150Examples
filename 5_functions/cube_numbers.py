""" Print the cube of numbers"""


def main():
    number1 = int(input('Please type a number: '))
    print_cube(number1) # function call
    number2 = int(input('Please type another number: '))
    print_cube(number2) # same function, different argument


def print_cube(x):   # definition of the cube function
    number_cubed = x**3
    print(f'The cube of {x} is {number_cubed}.')


main()  # main function is finally called


