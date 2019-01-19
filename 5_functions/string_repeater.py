""" Repeat a string, a given number of times """


def main():
    string = input('Please enter a string: ')
    repeat = int(input('How many times to repeat? '))
    result = string_repeater(string, repeat)  # function call
    print(result)


def string_repeater(text, n):
    repeated_string = text * n
    return repeated_string


main()
