# -*- coding: utf-8 -*-
import pytest

# Done in colaboration with Mario Pinto
# Coding Dojo 16/11/2023
# organized by Agile & Craftsmanship Canarias

# Rewritten to use pytest
# Original used unittest and assertpy

"""
TODO:

(1993) -> False
(4) -> True
(100) -> False
(400) -> True

(-1) -> "no sabemos"  ---> EDGE CASE 
(0) -> False

EDGE CASES  (Donde el parametro no sea un int)
(2000.0) -> EDGE CASE
("milcuatrocientos doce")  --> EDGE CASE
"""

def is_leap_year(year):
    year_is_not_integer = not isinstance(year, int)
    if year_is_not_integer:
        raise TypeError('Year has to be integer')
    is_unexistent_year = year == 0
    if is_unexistent_year:
        raise UnExistentNotAllowed('al acabar el Año I A.C. empieza el Año I D.C.')

    is_negative = year < 0
    if is_negative:
        raise NegativeYearsNotAllowed('Calendar not defined for negative years')
    is_divisible_by_four = year % 4 == 0
    is_not_divisible_by_first_excluded_year = year % 100 != 0
    is_exceptional_year = year % 400 == 0
    if (is_divisible_by_four and
        (is_exceptional_year or is_not_divisible_by_first_excluded_year)
    ):
        return True
    return False

class NegativeYearsNotAllowed(Exception):
    pass

class UnExistentNotAllowed(Exception):
    pass

class TypeError(Exception):
    pass

# tests
# class should begin with Test
# functions also begin with test

class TestLeapYear:
    def test(self):
        assert 0 == 0

    def test_determine_when_a_year_is_not_leap_year(self):
        no_leap_year = 1993
        assert is_leap_year(no_leap_year) is False

    def test__determine_leap_year_when_year_is_four(self):
        minimum_leap_year = 4
        assert is_leap_year(minimum_leap_year) is True

    def test__determine_leap_year_when_year_divisible_by_four(self):
        leap_year = 20
        assert is_leap_year(leap_year) is True

    def test__determine_no_leap_year_for_the_first_excluded_year(self):
        first_excluded_year = 100
        assert is_leap_year(first_excluded_year) is False

    def test__determine_leap_year_when_year_is_divisible_by_first_exceptionl_year(self):
        first_exceptional_year = 400
        assert is_leap_year(first_exceptional_year) is True

    def test__not_allow_negative_years(self):
        negative_year = -1
        with pytest.raises(NegativeYearsNotAllowed):
            is_leap_year(negative_year)

    def test__not_allow_unexistent_year(self):
        unexistent_year = 0
        with pytest.raises(UnExistentNotAllowed):
            is_leap_year(unexistent_year)

    def test__not_allow_float_years(self):
        float_year = 4.5
        with pytest.raises(TypeError):
            is_leap_year(float_year)

    def test__not_allow_string_years(self):
        string_year = "2000"
        with pytest.raises(TypeError):
            is_leap_year(string_year)