"""
A program with an if-elif-else statement to decide if the current temperature
is above freezing, below freezing, or exactly freezing
"""

current_temperature = float(input('Enter the current temperature, in F '))

if current_temperature < 32:
    print('It is below freezing')
elif current_temperature == 32:
    print('It is freezing')
else:
    print('It is above freezing')
