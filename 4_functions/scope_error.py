""" This program does not work.
The length, width, and height variables don't exist outside of main
 So calculate_volume can't access them. """


def main():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    calculate_volume()


def calculate_volume ():
    # This DOESN'T work  – the calculate_volume function
    # can't access variables from the main function. They are LOCAL to main.
    volume = length * width * height
    print(f'The volume of the box is: {volume}')


main()


