def next_(x, a):
    return (a + x / a) / 2


def repeat(f, a):
    yield round(a, 4)
    for val in repeat(f, f(a)):
        yield val


def within(epsilon, iterable):
    def head_tail(epsilon, a, iterable):
        b = next(iterable)
        if abs(a - b) <= epsilon:
            return b
        return head_tail(epsilon, b, iterable)

    return head_tail(epsilon, next(iterable), iterable)


def me_sqrt(n, epsilon=0.0001):
    return within(epsilon, repeat(lambda x: next_(n, x), 1.0))
