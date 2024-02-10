"""
Conditions
- Minimum 8 characters
- At least one upper case letter
- At least on lower case letter
- At least one number
- At least one underscore
"""

def isValid(password):
    has_upper_case = any([letter.isupper() for letter in password])
    return len(password) >= 8 and has_upper_case