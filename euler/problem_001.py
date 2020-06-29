from itertools import count, takewhile


def sum_of_multiples(stop, divisors):
    return sum(numbers_divisible_by(stop, divisors))


def numbers_divisible_by(stop, divisors):
    def generator():
        return filter(lambda x: any(divisible_by(x, k) for k in divisors), count(1))

    return takewhile(lambda x: x < stop, generator())


def divisible_by(x, k):
    return x % k == 0


if __name__ == '__main__':
    print(f'Multiples of 3 and 5: {sum_of_multiples(1000, [3, 5])}')
