"""
Examples of format strings
"""

total = 1234
print(f'The total is {total}')


weather = 'snow'
temperature = 29.5
day_of_month = 20

# This prints "On January 20, the temperature is 29.5 and the current weather is snow."
print(f'On January {day_of_month}, the temperature is {temperature} and the current weather is {weather}.')

# Equivalent with concatenating strings, converting numerical values to string
# Prints exactly the same string, but takes more typing.
print('On January ' + str(day_of_month) + ', the temperature is ' + str(temperature) + ' and the current weather is ' + weather + '.')


college = 'Minneapolis College'
department = 'ITEC'
sd_program = 'Software Development'
sd_program_credits = 60
sd_students = 291
total_students = 572

percent_sd_students = sd_students / total_students * 100



print(f'The {sd_program} in the {department} at {college} requires {sd_program_credits} credits.')

print(f'{percent_sd_students}% of students in the {department} are in the {sd_program}')

# Often you want to reduce the number of decimal places shown
print(f'{percent_sd_students:.2f}% of students in the {department} are in the {sd_program}')

# Can do math, call functions inside a format string. Don't make it too complicated though.
print(f'{total_students - sd_students} students in the {department} have other majors')


