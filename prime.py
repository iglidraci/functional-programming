from functional_programming.sqrt import *


def is_prime(n):
    return not any(n % p == 0 for p in range(2, int(me_sqrt(n)) + 1))


def is_prime_rec(n):
    def is_primer(k, co_prime):
        if k < co_prime ** 2:
            return True
        if k % co_prime == 0:
            return False
        return is_primer(k, co_prime + 2)
    if n < 2:
        return True
    if n % 2 == 0:
        return False
    return is_primer(n, 3)


print(is_prime(11556))
print(is_prime_rec(11556))
