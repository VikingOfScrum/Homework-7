import pytest
import LeapYear

LY = LeapYear

#First Test to check if return value is divisiable by 4
@pytest.mark.parametrize("year4, expected", [
    (1804, "is a Leap Year"),
    (1808, "is a Leap Year"),
    (1812, "is a Leap Year"),
    (1816, "is a Leap Year"),
    (1920, "is a Leap Year"),
    (1924, "is a Leap Year"),
    (2028, "is a Leap Year"),
    (2032, "is a Leap Year"),
    (2036, "is a Leap Year"),
    (2140, "is a Leap Year"),

])
def test_div_by_4(year4, expected):
    result = LY.isLeapYear(year4)
    assert result == expected

#Check years that are divisable by 100 as not being leap years
@pytest.mark.parametrize("year100, expected100", [
    (100, "is not a Leap Year"),
    (200, "is not a Leap Year"),
    (300, "is not a Leap Year"),
    (500, "is not a Leap Year"),
    (600, "is not a Leap Year"),
    (700, "is not a Leap Year"),
    (900, "is not a Leap Year"),
    (1000, "is not a Leap Year"),
    (1100, "is not a Leap Year"),
    (1300, "is not a Leap Year"),
    (1800, "is not a Leap Year"),
    (1900, "is not a Leap Year"),
    (2100, "is not a Leap Year"),
    (2200, "is not a Leap Year"),
    (2300, "is not a Leap Year"),
])

def test_div_by_100(year100, expected100):
    result = LY.isLeapYear(year100)
    assert result == expected100