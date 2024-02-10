"""
Conditions
- Minimum 8 characters
- At least one upper case letter
- At least on lower case letter
- At least one number
- At least one underscore
"""

def isValid(password):
    has_minimal_length = len(password) >= 8
    has_upper_case = any([letter.isupper() for letter in password])
    has_lower_case = any([letter.islower() for letter in password])
    has_number = any([letter.isdigit() for letter in password])
    has_underscore = '_' in password
    return has_minimal_length and has_upper_case and has_lower_case and has_number and has_underscore