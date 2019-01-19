""" Print the cube of numbers - function is called many times from a loop"""


def main():

    print('The cubes of the numbers 1 to 10 are:')
    for number in range(1, 11):
        print_cube(number)


def print_cube(x):   # definition of the cube function
    number_cubed = x**3
    print(f'The cube of {x} is {number_cubed}.')


main()  # main function is finally called

