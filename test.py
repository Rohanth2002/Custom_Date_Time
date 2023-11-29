import pytest
from EnhancedDate import EnhancedDate

# Test for creating EnhancedDate with specific values
def test_init_with_values():
    test_date = EnhancedDate(2025, 3, 15, 10, 45, 30)
    assert test_date.year == 2025
    assert test_date.month == 3
    assert test_date.day == 15
    assert test_date.hour == 10
    assert test_date.minute == 45
    assert test_date.second == 30

# Test for creating EnhancedDate with default values (current date and time)
def test_init_default():
    test_date_default = EnhancedDate()
    current = EnhancedDate.from_standard_format(EnhancedDate().to_standard_format())
    assert test_date_default.to_standard_format().startswith(current.to_standard_format())

# Test for standard ISO format conversion
def test_standard_iso_format():
    test_date_iso = EnhancedDate(2022, 5, 21, 16, 20, 10)
    assert test_date_iso.to_standard_format() == "2022-05-21T16:20:10"

# Test for readable format conversion
def test_readable_format():
    test_date_readable = EnhancedDate(2024, 7, 4, 11, 30, 55)
    assert test_date_readable.to_readable_format() == "2024-07-04 11:30:55"

# Test for validating dates
def test_check_date_validity():
    assert EnhancedDate.check_date_validity(2024, 12, 31) == True
    assert EnhancedDate.check_date_validity(2025, 2, 29) == False

# Test for calculating the difference between two dates
def test_difference_between_dates():
    date_one = EnhancedDate(2025, 1, 1)
    date_two = EnhancedDate(2025, 1, 20)
    assert abs(EnhancedDate.difference_between_dates(date_one, date_two, measurement='days')) == 19

# Test for creating a date object from a string
def test_create_from_string():
    date_string = "2024-06-10 09:15:25"
    test_date_from_str = EnhancedDate.create_from_string(date_string)
    assert test_date_from_str.to_readable_format() == "2024-06-10 09:15:25"
