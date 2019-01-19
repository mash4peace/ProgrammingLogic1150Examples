"""

 String functions
 Many other string functions - see https://docs.python.org/3/library/stdtypes.html

"""

college = 'minNeaPolis colleGe'

# upper(), lower() and title() don't modify the original string
# they all return a new string, in the new case
# so you need to save that in a new variable

# In uppercase
college_uppercase = college.upper()
print(college_uppercase)  # MINNEAPOLIS COLLEGE

# in lowercase
college_lowercase = college.lower()
print(college_lowercase)  # minneapolis college

# In title case
college_title = college.title()
print(college_title)  # Minneapolis College


# Sometimes you don't need the original string, just the version
# in the case it's being converted to.
# So, you can overwrite the original value with the converted version
# This code replaces the uppercase email with the lowercase version in the email variable.

email = 'CONTACT@MINNEAPOLIS.EDU'
# emails are conventionally written in lowercase
# convert email to lowercase, and print it

email = email.lower()
print(email)  # contact@minneapolis.edu
