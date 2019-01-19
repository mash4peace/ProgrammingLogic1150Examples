""" Function to check if the number of credits in a semester is valid
 The number has to be between 0 and 24 credits.

 This program has three functions.
 """


def main():
    credit_count = int(input('Please enter the number of credits this semester: '))

    while not credits_valid(credit_count):
        print('That is not a valid number of credits.')
        credit_count = int(input('Please enter the number of credits this semester, between 0 and 24: '))

    status_message = full_time_part_time(credit_count)

    print(f'Your status is a {status_message} student.')


def credits_valid(credit_count):
    if credit_count < 0 or credit_count > 24:
        return False
    else:
        return True


def full_time_part_time(credit_count):
    if credit_count >= 12:
        return 'full time'
    elif credit_count >= 6:
        return 'part time'
    else:
        return 'less than part time'


main()


