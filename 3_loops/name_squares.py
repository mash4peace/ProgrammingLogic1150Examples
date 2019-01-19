"""
Printing a word in a square, both vertically and horizontally.
"""


name = input('Please enter your name: ')


print()
print('Your name, horizontal square')
print()

for letter in range(len(name)):
    print(name)


print()
print('Your name, vertical square')
print()

for letter in name:
    line = ''
    for count in range(len(name)):
        line = line + letter
    print(line)


print()
print('Your name, as a triangle')

counter = 1
for letter in name:
    line = ''
    for count in range(counter):
        line += letter
    print(line)
    counter = counter+1
