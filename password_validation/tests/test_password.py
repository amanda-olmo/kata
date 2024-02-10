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

    def test_password_should_have_minimal_length(self):
        password = 'aA1_aaa'
        assert isValid(password) is False

    def test_password_should_have_at_least_one_uppercase_letter(self):
        password = '123456_a'
        assert isValid(password) is False

    def test_password_should_have_at_least_one_lowercase_letter(self):
        password = '123456_A'
        assert isValid(password) is False

    def test_password_should_have_at_least_one_number(self):
        password = 'aaaaaa_A'
        assert isValid(password) is False
