from typing import *


def group_by_sequence(sequence: [], n: int) -> [Tuple[Any]]:
    """
    group a sequence into tuples of length n if possible
    """
    flat_iter = iter(sequence)
    full_sized_iter = list(
        tuple(next(flat_iter) for _ in range(n))
        for _ in range(len(sequence) // n)
    )
    left = tuple(flat_iter)
    if left:
        return full_sized_iter + [left]
    return full_sized_iter


def group_by_iter(iterator: Iterator, n: int):
    """tail-recursion optimization"""
    row = tuple(next(iterator) for _ in range(n))
    while row:
        yield row
        row = tuple(next(iterator) for _ in range(n))


if __name__ == '__main__':
    flat = range(100)
    print(group_by_sequence(list(filter(lambda x: x % 3 == 0, flat)), 3))

