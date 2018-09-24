# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name:
# Problem description: Sleepwalking student

import random
import sys
sys.setrecursionlimit(50000)

def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """this function returns the random walker's position.
       Argument start: an integer representing the starting position
       Argument nsteps: a nonnegative integer represetning the number of random steps
       to take from the starting position
    """
    if nsteps == 0:
        print("The walker stopped at", start)

    else:
        print("start is", start)
        return rwpos(start + rs(), nsteps - 1)

def rwsteps(start, low, hi):
    """simulates a random walk, prints each step, walker should stop when they hit hi or low
       Argument start: starting postion of walker
       Argument low: nonnegative number representing the smalled value the sleepwalker can wander
       Argument hi: the highest number the sleepwalker can wander
    """
    print('|' + ('_' *((start - low) )) + 'S' + ('_'* ((hi - start)) + '|'))
    newstart = start + rs()
    if newstart <= low or newstart >= hi:
        return 0
    else:
        rest_of_steps = rwsteps(newstart, low, hi)
        return rest_of_steps + 1

def rwposPlain(start, nsteps):
    """this function returns the random walker's position.
       Argument start: an integer representing the starting position
       Argument nsteps: a nonnegative integer represetning the number of random steps
       to take from the starting position
    """
    if nsteps == 0:
        print(start)

    else:
        return rwposPlain(start + rs(), nsteps - 1)

def disp(start, n):
    """returns the signed displacement from the starting position
       Argument start: starting postion
       Argument n: the number of nsteps
    """
    move = rwposPlain(start, n)
    return move - start
