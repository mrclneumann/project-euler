from euler.problem_1 import numbers, sum_of_multiples


def test_numbers():
    assert list(numbers(limit=10, divisors=[3, 5])) == [3, 5, 6, 9]


def test_sum_of_multiples():
    assert sum_of_multiples(limit=10, divisors=[3, 5]) == 23
