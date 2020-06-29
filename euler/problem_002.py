from itertools import takewhile


def sum_of_even_fibonacci(n):
    return sum(x for x in fibonacci(n) if is_even(x))


def fibonacci(stop):
    def fib_gen():
        a, b = 1, 1

        while True:
            yield b
            a, b = b, a + b

    return takewhile(lambda x: x <= stop, fib_gen())


def is_even(x):
    return x % 2 == 0


if __name__ == '__main__':
    print(f'Even Fibonacci numbers: {sum_of_even_fibonacci(4_000_000)}')
