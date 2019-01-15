password = input('Please enter the password to check if it is long enough')

password_min_length = 8  # Passwords must be at least 8 characters

if len(password) < password_min_length:
    print('Sorry, your password is not long enough, it must be 8 characters')
else:
    print('Well done, your password is long enough.')
