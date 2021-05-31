__doc__ = "find the prime factors of a number"

import itertools
import time
from typing import Iterator, Any

from sqrt import me_sqrt


def prime_factors_of(x: int) -> Iterator[int]:
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from prime_factors_of(x // 2)
        return
    for i in range(3, int(me_sqrt(x) + 0.5) + 1, 2):
        if x % i == 0:
            yield i
            if x // i > 1:
                yield from prime_factors_of(x // i)
            return
    yield x


def prime_factors_recursively(x: int) -> Iterator[int]:
    """
    purely recursive version of finding prime factors
    """

    def _factor_n(x: int, n: int):
        if n ** 2 > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x//n > 1:
                yield from _factor_n(x//n, n)
        else:
            yield from _factor_n(x, n+2)
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from prime_factors_recursively(x // 2)
        return
    yield from _factor_n(x, 3)


def min_max_of_generators(iterator: Iterator[Any]) -> tuple[Any, Any]:
    min_tee, max_tee = itertools.tee(iterator, 2)
    return min(min_tee), max(max_tee)


t1 = time.time()
try:
    print(min_max_of_generators(prime_factors_recursively(2**1000)))
except RecursionError:
    print('recursion error')
print(f'took {time.time() - t1} seconds')
