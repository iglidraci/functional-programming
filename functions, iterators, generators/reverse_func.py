def digits(x: int, b: int):
    if x == 0: return
    yield x % b
    for digit in digits(x//b, b):
        yield digit


if __name__ == '__main__':
    print(''.join(map(lambda x: str(x), reversed(list(digits(10, 2))))))
