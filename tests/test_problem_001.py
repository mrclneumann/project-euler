import pytest

from euler.problem_001 import numbers_divisible_by, sum_of_multiples


def test_numbers_divisible_by():
    assert list(numbers_divisible_by(stop=10, divisors=[3, 5])) == [3, 5, 6, 9]


@pytest.mark.parametrize('stop,expected', [
    (10, 23),
    (1000, 233168)
])
def test_sum_of_multiples(stop, expected):
    assert sum_of_multiples(stop=stop, divisors=[3, 5]) == expected
