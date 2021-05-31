import math
from typing import Iterable


class NullAware:
    def __init__(self, some_func):
        self.some_func = some_func

    def __call__(self, args):
        return None if args is None else self.some_func(args)


class SumFilter:
    def __init__(self, map_func, filter_func):
        self.map_func = map_func
        self.filter_func = filter_func

    def __call__(self, iterable: Iterable):
        return sum(
            self.map_func(x)
            for x in iterable if self.filter_func(x)
        )


if __name__ == '__main__':
    print(list(map(NullAware(math.log), [1, 2, 3, None, 4])))
    count_non_none = SumFilter(lambda x: 1, lambda x: x is not None)
    sum_non_none = SumFilter(lambda x: x, lambda x: x is not None)
    print(count_non_none([1, 2, 3]))
    print(sum_non_none([1, 2, 3, None, None, 4]))
