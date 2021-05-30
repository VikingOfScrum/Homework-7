import pytest
import TestLeapYear

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