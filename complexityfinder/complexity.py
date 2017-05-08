from scipy.optimize import fmin


class BadArgument(Exception):
    pass


# Objects of this class should only be created by complexity_finder
class Complexity:
    def __init__(self, fun, popt, desc):
        self.fun = fun
        self.fun_popt = popt
        self.desc = desc

    def estimate_time(self, n):
        if n <= 0:
            raise BadArgument("N must be greater than 0")
        return self.fun(n, *self.fun_popt)

    def estimate_size(self, time):
        if time <= 0:
            raise BadArgument("Time must be greater than 0")

        # TODO decorator
        f = self.fun

        def fun(x):
            return abs((time - f(x, *self.fun_popt)) / time)

        minimun = fmin(fun, x0=1, disp=False)
        return int(minimun.__getitem__(0))

    def get_desc(self):
        return self.desc

    def get_info(self):
        return ("The complexity of the given function is: " + self.get_desc() + "\n" +
                "The function will run: " + str(self.estimate_time(1000)) + "s for n=1000\n" +
                "In one second function can solve problem with n up to:" + str(self.estimate_size(1)) + "\n")

    def print_some_info(self):
        print("*******************************************************************************")
        print(self.get_info())
        print("*******************************************************************************")
