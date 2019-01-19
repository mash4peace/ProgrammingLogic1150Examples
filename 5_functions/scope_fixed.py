""" This program does not work.
The length, width, and height variables don't exist outside of main
 So calculate_volume can't access them. """


def main():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    calculate_volume(length, width, height)


def calculate_volume(length, width, height):
    # Fixed - the necessary data is supplied as parameters.
    volume = length * width * height
    print(f'The volume of the box is: {volume}')


main()


