import pytest
import FizzBuzz

FB = FizzBuzz
#Setting up first test to check that Fizz is a given correctly for integers divisable by 3 in values from 1 to 100
@pytest.mark.parametrize("integer3, expectFizz", [
    (3, "Fizz"),
    (6, "Fizz"),
    (9, "Fizz"),
    (12, "Fizz"),
    (18, "Fizz"),
    (21, "Fizz"),
    (24, "Fizz"),
    (27, "Fizz"),
    (33, "Fizz"),
    (36, "Fizz"),
    (39, "Fizz"),
    (42, "Fizz"),
    (48, "Fizz"),
    (51, "Fizz"),
    (54, "Fizz"),
    (57, "Fizz"),
    (63, "Fizz"),
    (66, "Fizz"),
    (69, "Fizz"),
    (72, "Fizz"),
    (78, "Fizz"),
    (81, "Fizz"),
    (84, "Fizz"),
    (87, "Fizz"),
    (93, "Fizz"),
    (96, "Fizz"),
    (99, "Fizz")
])

def test_check_for_div_3(integer3, expectFizz):
    result = FB.checkNumber(integer3)
    assert result == expectFizz

@pytest.mark.parametrize("integer5, expectBuzz", [
    (5, "Buzz"),
    (10, "Buzz"),
    (20, "Buzz"),
    (25, "Buzz"),
    (35, "Buzz"),
    (40, "Buzz"),
    (50, "Buzz"),
    (55, "Buzz"),
    (65, "Buzz"),
    (70, "Buzz"),
    (80, "Buzz"),
    (85, "Buzz"),
    (95, "Buzz"),
    (100, "Buzz")
])

def test_check_for_div_5(integer5, expectBuzz):
    result = FB.checkNumber(integer5)
    assert result == expectBuzz