"""
Using a while loop to check that the user enters 0 or a positive number for a number of credits.
"""

number_of_credits = int(input("Enter the number of credits you are taking this semester? "))

# This loop repeats while the input is invalid - the number of credits is less than 0
while number_of_credits < 0:
    print('Error - please enter 0 or a positive number.')
    number_of_credits = int(input("Enter the number of credits you are taking this semester? "))


if number_of_credits >= 12:
    print('You are a full-time student')
elif number_of_credits >= 6:
    print('You are a half-time student')
else:
    print('You are less than half-time')




