def f(x):
    return x**2


def g(x):
    return x**3


f_x = (f(x) for x in range(100))
g_f_x = (g(fx) for fx in f_x)
