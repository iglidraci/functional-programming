from typing import Callable


y = lambda x: str(neg(int(x)))
neg = lambda x: -x


class Failure:
    def __init__(self, value, has_failed=False):
        self.value = value
        self._has_failed = has_failed

    def bind(self, func: Callable):
        if self._has_failed:
            return self
        try:
            result = func(self.value)
            return Failure(result)
        except:
            return Failure(None, True)

    def __str__(self):
        return f"{self.value}, {self._has_failed}"

    def __or__(self, other: Callable):
        return self.bind(other)


if __name__ == '__main__':
    x = "10"
    # print(y(x))
    print(Failure(x).bind(int).bind(neg).bind(str))
    y = Failure(x) | int | neg | str
    print(y.value)
