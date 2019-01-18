"""
Checking if the user enters the wrong password
Checking if a value is equal to another value using ==
"""

secret_password = 'kittens'   # Super top secret password

password = input('Enter the secret password: ')

if password == secret_password:
    print('Welcome, authorized user')

