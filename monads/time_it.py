from functools import wraps
from time import sleep, time


# Decorator to time function execution
def time_it(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        return TimedValue(result, end - start)

    return wrapper


# let's define some functions


@time_it
def fast(x):
    return x + 1


@time_it
def slow(x):
    sleep(0.1)
    return x + 1


@time_it
def slow2(x):
    sleep(0.1)
    return x + 2


# def bind(value_and_time, f):
#     """
#     :param value_and_time: Tuple[T, float]
#     :param f: Callable[[T], Tuple[U, float]]
#     :rtype: Tuple[U, float]
#     """
#     result, t = f(value_and_time[0])
#     return result, t + value_and_time[1]


class TimedValue(object):

    def __init__(self, value, time=0.):
        self.value = value
        self.time = time

    def bind(self, f):
        timed_value = f(self.value)
        new_value = timed_value.value
        new_time = self.time + timed_value.time
        return TimedValue(new_value, new_time)


if __name__ == '__main__':
    # Method 1: the obvious way

    # x0, time0 = fast(1)
    # x1, time1 = slow(x0)
    # x2, time2 = slow2(x1)
    #
    # total_time = time0 + time1 + time2
    #
    # print(total_time)
    # x2, t = bind(bind(fast(1), slow), slow2)
    # print(f"x2 is {x2} and t is {t}")
    timed_value = (fast(1).bind(slow).bind(slow2))

    value = timed_value.value
    time = timed_value.time
    print(f"Value is {value} and time is {time}")
