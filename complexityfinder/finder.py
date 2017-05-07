import time
import logging
from multiprocessing import Pool, TimeoutError, cpu_count

import numpy as np
from scipy.optimize import curve_fit
from functools import wraps

from complexityfinder.complexity import Complexity
from complexityfinder.complexityFunctions import funs

log = False


def log_setter(val):
    global log
    log = val


class FunctionFailure(Exception):
    pass


def arr_generator(n):
    return np.random.randint(100, size=n)


def simple_cleaner(arg):
    del arg


def simple_setup(arg):
    return arg


# decorator for logging
def log_single_test(func):
    @wraps(func)
    def fun_wrapper(f, n, setup, clean):
        res = func(f, n, setup, clean)
        if log:
            logging.info("Testing result for " + str(n) + " :" + str(res) + "s")
        return res

    return fun_wrapper


def log_finding(func):
    @wraps(func)
    def fun_wrapper(*args):
        logging.info("Starting testing function's complexity")
        res = func(*args)
        if log:
            logging.info("Complexity finding ended successfully")
        return res

    return fun_wrapper


@log_single_test
def test_it(f, n, setup, clean):
    arr = setup(n)
    now = time.time()
    try:
        res = f(arr)
        later = time.time()
        clean(res)
        return later - now
    except:
        if log:
            logging.ERROR("Function Failure")
        raise FunctionFailure("Provided function has failed, try providing another one")


def probing_generator():
    def probing_fun(y):
        return max(int(0.1 * y ** 2), 1)

    x = 1
    while True:
        yield probing_fun(x)
        x += 1


@log_finding
def tester_fun(f, timeout, *args):
    start = time.time()
    i = probing_generator()
    tmp = []
    pool = Pool(processes=cpu_count())

    while (time.time() - start) < timeout and len(tmp) < 1000:
        val = next(i)
        sizes = [val for _ in range(cpu_count())]
        multiple_results = [pool.apply_async(test_it, (f, j, *args)) for j in sizes]
        try:
            times = []
            for j in multiple_results:
                t = j.get(timeout=2)
                times.append(t)
            tmp.append((val, np.median(times)))

        except TimeoutError:
            pass
    return tmp


def complexity_finder(f, setup=simple_setup, clean=simple_cleaner, timeout=30):
    tmp = tester_fun(f, timeout, setup, clean, )
    x1 = np.array([x[0] for x in tmp])
    y1 = np.array([x[1] for x in tmp])
    res = []
    for fun in funs:
        popt, pcov = curve_fit(fun[0], x1, y1, bounds=(0, np.inf))
        y2 = [fun[0](x, *popt) for x in x1]
        err = np.mean(((y1 - y2) ** 2))
        res.append((err, popt, fun))
    winner = min(res, key=lambda x: x[0])
    complexity = Complexity(winner[2][0], winner[1], winner[2][1])
    if log:
        logging.info(complexity.get_info())
    return complexity
