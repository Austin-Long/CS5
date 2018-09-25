# CS 5 Gold, hw2pr3
# filename: hw2pr3.py
# Name: Austin Long and Charlie Mangum
# problem description: List comprehensions

# this gives us functions like sin and cos...
from math import *

# two more functions (not in the math library above)

def dbl(x):
    """Argument: a number x (int or float)
       Return value: twice the arguments
    """
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2

# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [float(x//2) for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs(N):
    """Returns a list of evenly-spaced left-hand endpoints in [0,1)
       Argument N: a list
    """
    return [x/N for x in range(N)]

assert unitfracs(2) == [0.0, 0.5]
assert unitfracs(4) == [0.0, 0.25, 0.5, 0.75]
assert unitfracs(5) == [0.0, 0.2, 0.4, 0.6, 0.8]
assert unitfracs(3) == [0.0, 0.3333333333333333, 0.6666666666666666]
assert unitfracs(10) == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

def scaledfracs(low, hi, N):
    """Returns N left endpoints uniformly through the interval [low, hi)
    """
    return [round(low + (x/N * ((hi-low)*N)), 3) for x in unitfracs(N)]

assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
assert scaledfracs(41, 43, 8) == [41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5]

def sqfracs(low, hi, N):
    """Returns the N left endpoints uniformly throught the interval [low, hi), squared!
    """
    return [x**2 for x in scaledfracs(low, hi, N)]

assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert sqfracs(0, 10, 5) == [0.0, 4.0, 16.0, 36.0, 64.0]
assert sqfracs(0, 10, 2) == [0.0, 25.0]

def f_of_fracs(f, low , hi, N):
    """Takes a function as its first argument, f
       Then returns a list that has function f applied to it uniformly
    """
    return [round(f(x), 3) for x in scaledfracs(low, hi, N)]

assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert f_of_fracs(sin, 0, pi, 4)  ==  [0.0, 0.707, 1.0, 0.707]

def integrate(f, low, hi, N):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where N steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of N uniform steps
       from low to hi
    """
    return sum(f_of_fracs(f, low, hi, N)) * (hi - low)/N


assert integrate(dbl, 0, 10, 4) == 75
assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

assert round(integrate(c, 0, 2, 2), 3) == 3.732                    # rounded...
assert round(integrate(c, 0, 2, 20), 3) == 3.228

round(integrate(c, 0, 2, 200), 3)
round(integrate(c, 0, 2, 2000), 3)

"""
    1. Integrate() will always underestimate the correct value of this particular integral because of
    we are not accounting for small amount of area between the fitted rectangles and the true function.

    A function that would always be overestimated on the interval 0 to 10, is x^2 because the
    rectangles would account for area above the function.

    2. This function should converge to pi as N goes to infinity. We get 3.151 and 3.143, it appears to be converging on 3.1415...
    This checks out because the area of a circle with radius 2 is 4*pi
    As a result, 0.25 times that area is just pi, 3.1415...

"""
