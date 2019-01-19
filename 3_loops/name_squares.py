"""
Printing a word in a square, both vertically and horizontally.
"""


name = input('Please enter your name: ')

print('Your name, vertical square')
print()

for letter in name:
    line = ''
    for count in range(len(name)):
        line = line + letter
    print(line)


print()
print('Your name, horizontal square')
print()

for letter in range(len(name)):
    print(name)
