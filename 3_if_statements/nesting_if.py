"""
Nested if statements. If it below 50F, tell user to wear a coat.
If it is cold and snowing, tell user to wear boots too.
"""

temperature = float(input('Enter the temperature in Fahrenheit: '))

if temperature <= 32:
    print('It is below freezing. Watch out for ice.')

    snowing = input('Enter "Y" if it is snowing today: ')

    if snowing == 'Y':
        print('Snow boots are recommend today')

else:
    print('It is above freezing today')


