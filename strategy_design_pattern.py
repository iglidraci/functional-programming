from typing import Callable


class Mersenne2:
    """
    compute 2 to the power of arg
    """
    def __init__(self, algorithm: Callable[[int], int]) -> None:
        self.pow_of_2 = algorithm

    def __call__(self, arg):
        return self.pow_of_2(arg) - 1


def shift_bits(x: int) -> int:
    return 1 << x


def recursive(x: int) -> int:
    if x == 0:
        return 1
    return 2 * recursive(x-1)


def faster(x: int) -> int:
    if x == 0:
        return 1
    if x % 2 == 1:
        return 2 * faster(x - 1)
    t = faster(x//2)
    return t*t


m1 = Mersenne2(shift_bits)
m2 = Mersenne2(recursive)
m3 = Mersenne2(faster)

print(f'{m1(20)} {m2(20)} {m3(20)}')
