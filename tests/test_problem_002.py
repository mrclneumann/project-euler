import pytest

from euler.problem_002 import fibonacci, sum_of_even_fibonacci


def test_fibonacci():
    assert list(fibonacci(100)) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


@pytest.mark.parametrize('stop,expected', [
    (100, 44),
    (4_000_000, 4613732)
])
def test_sum_of_even_fibonacci(stop, expected):
    assert sum_of_even_fibonacci(stop) == expected
