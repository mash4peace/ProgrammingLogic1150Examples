"""
Long way of converting lowercase latin characters in a string to uppercase
"""

example_class_code = 'itec 1234'

uppercase_class_code = ''

for letter in example_class_code:
    # Convert letter to unicode value
    character_code = ord(letter)
    # Is this a lowercase letter? Is it between 97 and 122?
    if character_code >= 97 and character_code <= 122:
        # Subtract 32 to get the code for the matching uppercase letter
        uppercase_character_code = character_code - 32
        # Convert the unicode to a character
        uppercase_letter = chr(uppercase_character_code)
        # Append to the output string
        uppercase_class_code = uppercase_class_code + uppercase_letter
    else:
        # Not a lowercase letter. Append it to the output string
        uppercase_class_code = uppercase_class_code + letter

print(f'The class code in uppercase is {uppercase_class_code}')

