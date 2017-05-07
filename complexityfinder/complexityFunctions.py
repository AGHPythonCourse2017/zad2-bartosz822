import numpy as np


def const(x, a):
    return a


def logn(x, a):
    return a * np.log2(x)


def n(x, a):
    return a * x


def nlogn(x, a):
    return a * x * np.log2(x)


def n2(x, a):
    return a * x ** 2


def n3(x, a):
    return a * x ** 3


def exp(x, a):
    return a*np.power(2, x)

funs = [(const, "O(1)"), (logn, "O(log(n))"), (n, "O(n)"), (nlogn, "O(n*log(n))"), (n2, "O(n^2)"), (n3, "O(n^3)"),
        (exp, "O(2^n)")]
