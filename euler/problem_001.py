def sum_of_multiples(limit, divisors):
    return sum(numbers(limit, divisors))


def numbers(limit, divisors):
    for i in range(1, limit):
        if any(divisible_by(i, n) for n in divisors):
            yield i


def divisible_by(x, n):
    return x % n == 0


if __name__ == '__main__':
    print(f'Multiples of 3 and 5: {sum_of_multiples(1000, [3, 5])}')
