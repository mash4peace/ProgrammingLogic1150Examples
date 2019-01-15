"""
Checking if a value is not equal to another value using !=
"""

secret_password = 'kittens'   # Super top secret password

password = input('Enter the secret password: ')

if password != secret_password:
    print('ACCESS DENIED!!!')
else:
    print('Welcome, authorized user')