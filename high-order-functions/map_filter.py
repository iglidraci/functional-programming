from typing import Callable

from prime import is_prime_rec


start = lambda x: x[0]
end = lambda x: x[1]
dist = lambda x: x[2]

to_miles = lambda x: (start(x), end(x), 1.6 * dist(x))


def numbers_from_rows(conversion_func: Callable, text: str):
    return (
        conversion_func(number)
        for row in text.splitlines()
        for number in row.split(' ')
    )


if __name__ == "__main__":
    tp = (
        ((100, 200), (300, 500), 1000),
        ((300, 500), (300, 500), 9877)
    )

    miles = list(map(to_miles, tp))
    prime_numbers = list(filter(is_prime_rec, range(100)))
    print(prime_numbers)
    text = "1 2 3\n4 5 6"
    print(list(numbers_from_rows(int, text)))
