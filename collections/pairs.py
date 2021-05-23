__doc__ = "create pairs from a collection of values a1, a2, a3, a4, a5 => " \
          "(a1, a2), (a2, a3), (a4, a5)"

from math import radians, sin, cos, asin
from typing import Iterator, Tuple

from functional_programming.sqrt import me_sqrt


def pairs_recursive(iterator: Iterator):
    def make_pair(head, tail):
        try:
            nxt = next(tail)
        except StopIteration:
            return iter([])
        yield head, nxt
        yield from make_pair(nxt, tail)

    return make_pair(next(iterator), iterator)


def pairs(iterator: Iterator):
    head = next(iterator)
    for nxt in iterator:
        yield head, nxt
        head = nxt


Point = Tuple[float, float]


def haversine(p1: Point, p2: Point) -> float:
    lat1, lon1 = p1
    lat2, lon2 = p2
    delta_lat = radians(lat2 - lat1)
    delta_lon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = me_sqrt(sin(delta_lat/2)**2 + cos(lat1)*cos(lat2)*sin(delta_lon/2)**2)
    c = 2*asin(a)
    return 3440 * c


iterator = ('100', '200', '300', '500', '600.7', '-100', '-240')

point_pairs = pairs_recursive(pairs_recursive(map(lambda x: float(x), iterator)))

start_end_distance = map(lambda p: (p[0], p[1], haversine(p[0], p[1])), point_pairs)

for x in start_end_distance:
    print(f"start point={x[0]}, end point={x[1]}, distance={x[2]}")
