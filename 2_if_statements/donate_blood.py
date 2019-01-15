"""
To be a blood donor, you must be at least 17 years old, and weigh at least 115lbs.
This program asks the user for their age and weight,
and decides if they can give blood or not.
"""

weight = float(input('Please enter your weight, in pounds: '))
age = int(input('Please enter your age, in years: '))

if weight >= 115 and age >= 17:
    print('Great! You are eligible to be a blood donor. ')
elif weight >= 115 and age < 17:
    print('Sorry, you are not old enough. Please come back when you are 17 or older.')
elif weight < 115 and age >= 17:
    print('Sorry, you do not weigh enough. For the safety of donors, you must weigh at least 115lbs.')
else:
    print('Sorry, you are too young and do not weigh enough to give blood. Please come back when you are 17 or older.')
