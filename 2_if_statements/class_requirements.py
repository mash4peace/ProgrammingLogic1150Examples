"""
Using the or operator

Requirements for taking the Apple Mobile Development class is
either C# ("c-sharp") programming, or Java programming, or both.
Ask the user if they have taken C# programming,
Ask the user if they have taken Java programming,
and then print a message if they are eligible to take Apple Mobile Development.
"""

csharp = input('Have you taken C# programming? Type "yes" if so: ')
java = input('Have you taken Java programming? Type "yes" if so: ')

if csharp == 'yes' or java == 'yes':
    print('You can take the Apple Mobile Development class.')
else:
    print('Sorry, you need to take either C# or Java before you can take Apple Mobile Development')
