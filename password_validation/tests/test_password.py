# Python libraries
import pytest
# Own libraries
from src.main import isValid

"""
Conditions
- Minimum 8 characters
- At least one upper case letter
- At least on lower case letter
- At least one number
- At least one underscore

"""

class TestPassword:

    def test_good_password(self):
        password = 'aA1_aaaa'
        assert isValid(password) is True
