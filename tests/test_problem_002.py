from euler.problem_002 import fibonacci


def test_fibonacci():
    assert list(fibonacci(100)) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
