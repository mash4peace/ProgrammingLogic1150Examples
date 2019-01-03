""" Using the len() function to calculate the number of characters in a string """

school = 'Minneapolis College'

# Use the len function to count the number of characters in a string.
# All the characters, including spaces, are counted.
# The total is saved in the variable letters.
letters = len(school)  # letters is an int variable. 

print(letters)
print('The string "' + school + '" contains ' + str(letters) + ' letters.')