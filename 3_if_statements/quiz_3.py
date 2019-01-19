"""
Quiz program, version 3. This prints a message if the user gets the
answer right or wrong.

It also converts the user's answer to lowercase and compares it to the
lowercase version of the right answer, so the user can answer in any case,
Madison and MADISON and madison are all right.

"""

print('Quiz program!')

answer = input('What is the capital of Wisconsin? ')  # It's Madison

if answer.lower() == 'madison':
    print('Correct!')
else:
    print('Sorry, the answer is Madison.')

