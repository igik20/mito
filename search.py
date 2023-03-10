"""
Minimal Iterative Optimizer by Yvette Dimitrova and Igor Trujnara. MIT license.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

# hard iteration limit, do not change unless strongly justified
ABSMAX = 10**6

class Midpoint_Search:
    """
    Utility class with functions used for equal interval optimization and result plotting.
    """

    # for testing only
    def f(x):
        return 1 / x


    def midpoint_search(func, lower, upper, limtype, limval, target):
        """
        The main optimization function.
        """
        mid = (upper + lower) / 2
        i = 0
        generations = {}
        # optimization loop
        while True:
            # calculations
            eps = (upper - lower) / 10

            m_plus = mid + eps
            m_minus = mid - eps

            f_plus = func(m_plus)
            f_minus = func(m_minus)
            if target == "Maximum":
                if f_plus > f_minus:
                    lower = mid
                else:
                    upper = mid
            else:
                if f_plus < f_minus:
                    lower = mid
                else:
                    upper = mid
            mid = (upper + lower) / 2

            # exit conditions
            if limtype == "Number of Iterations" and i >= limval:
                break
            elif limtype == "Absolute Tolerance" and upper - lower <= limval:
                break
            elif limtype == "Relative Tolerance" and (upper - lower) / mid <= limval:
                break
            elif i >= ABSMAX:
                break

            # save the generation
            generations[i] = (lower, mid, upper)

            # count iterations for iteration limits
            i += 1

        return mid, func(mid), generations

    @staticmethod
    def plot_generation(func, lower, mid, upper):
        """
        Plots bounds and midpoint for a given generation.
        """
        x = np.linspace(lower, upper, 100)
        y = [func(i) for i in x]
        plt.plot(x, y)
        plt.axvline(x = lower, color = "blue")
        plt.axvline(x = upper, color = "blue")
        plt.axvline(x = mid, color = "red")
        plt.show()

    @staticmethod
    def plot_result(func, lower, upper, coord, val):
        """
        Plots optimization results from equal interval search.
        """
        x = np.linspace(lower, upper, 100)
        y = [func(i) for i in x]
        plt.plot(x, y)
        plt.axvline(x = coord, color = "red")
        plt.axhline(y = val, color = "red")
        plt.show()
