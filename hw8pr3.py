# Austin Long
# hw8pr3

#
#
import random
import math

def throDart():
    """A helper function, returns true if the "dart" falls in the circle,
       false if the dart misses the circle
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    #circle equation: (x-h)^2 + (y-k)^2 = r^2
    if x**2 + y**2 <= 1:
        return True
    return False

def forPi(n):
    """prints the number of darts thrown so far, the # of darts thrown so far
       that have hit the circle, and the resulting estimate of pi for each throw
       returns the final estimate of pi
       accepts a postitve integer n
    """
    num = 0
    for x in range(n):
        if throDart():
            num += 1
        print('hits out of ', x + 1, 'throws so that pi is ', num/(x + 1)*4)
    return num/n * 4

def whilePi(error):
    """throws darts at the dartboard until the absolute difference between
       the functions estimate of pi and the real value of pi is less than
       error
       accepts: a positive floating-point value, error
    """
    hits = 0
    count = 0
    while count == 0 or abs(hits/count*4 - math.pi) > error:
        if throDart():
            hits += 1
            count += 1
        else:
            count += 1
        print('hits out of ',count, 'throws so that pi is ', hits/(count)*4)
    return count
