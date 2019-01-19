"""
What happens if you switch the order of the arguments when you call the report function?
"""


def main():
    credits_completed = 34
    college = 'Minneapolis College'
    # report(credits_completed, college)

    # What happens if you called the function like this?
    report(college, credits_completed)


def report(cr, col):
    print('Your school is', col)
    print(f'You need {60 - cr} credits to graduate')


main()

