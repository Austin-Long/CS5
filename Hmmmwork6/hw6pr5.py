#
# hw6pr5.py -  Python!
#
#  Gold:   this is "Intro to loops"! (starter code below)
# Black:   this is "Nim"!    (add/replace code as needed)
#
# Name:Austin Long
#
import random

def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
assert fac(0) == 1
assert fac(5) == 120


def power(b, p):
    """Loop-Based power function
       Argument: any numeric base b and any nonnegative power p
       Returns: b**p
    """
    result = 1
    for x in range(p):
        result = result * b
    return result

assert power(2, 5) == 32
assert power(5, 2) == 25
assert power(42, 0) == 1
assert power(0, 42) == 0
assert power(0, 0) == 1


def summed(L):
    """Loop-based function to return a numeric list.
       ("sum" is built-in, so we're using a different name.)
       Argument: L, a list of integers.
       Result: the sum of the list L.
    """
    result = 0
    for e in L:
        result = result + e    # or result += e
    return result

# tests!
assert summed([4, 5, 6]) == 15
assert summed(range(3, 10)) == 42

def summedOdds(L):
    """Loop-based function to return a numeric list.
       Argument: L, a list of integers.
       Result: the sum of the odd elements of the list L.
    """
    result = 0
    for e in range(len(L)):
        if L[e] % 2 == 1:
            result += L[e]
        else:
            result += 0
    return result

# tests!
assert summedOdds([4, 5, 6]) == 5
assert summedOdds(range(3, 10)) == 24



def countGuesses(hidden):
    """Uses a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 to 99, inclusive
    numguesses = 1                           # we just made one guess, above
    while guess != hidden:
        guess = random.choice(range(0, 100)) # guess again!
        numguesses += 1                      # add one to our number of guesses
    return numguesses


def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])  # recursion is OK in this function!


def untilARepeat(high):
    """Returns the number of guesses needed until it gets a repeat
       Accepts: an integer, high
    """
    L = []
    count = 0

    while unique(L):
        guess = random.choice(range(0, high))
        L += [guess]
        count += 1
    return count
