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
    print('|' + ('_' * (start - low)) + 'S' + ('_'* (hi - start) + '|'))
    if start == low or start == hi:
        return 0
    else:
        return 1 + rwsteps(start + rs(), low, hi)


def rwposPlain(start, nsteps):
    """this function returns the random walker's position.
       Argument start: an integer representing the starting position
       Argument nsteps: a nonnegative integer represetning the number of random steps
       to take from the starting position
    """
    if nsteps == 0:
        return start
    return rwposPlain(start + rs(), nsteps - 1)

def ave_signed_displacement(numtrials):
    """returns the signed displacement from the starting position
       Argument nums: the number of trials
    """
    LC = [rwposPlain(0, 100) for x in range(numtrials)]
    return  float(sum(LC))/ numtrials

def ave_squared_displacement(numtrials):
    """returns the average of the squares
       Argument numtrials: the number of trials
    """
    LC = [rwposPlain(0, 100)**2 for x in range(numtrials)]
    return  float(sum(LC))/ numtrials

print(ave_signed_displacement(100))
print(ave_squared_displacement(100))

"""
    To compute the average sighned displacement for a random walker
    after 100 random steps, I created a function named rwposPlain
    that returns an integer of the random walker's position. Next,
    I created ave_signed_displacement and ave_squared_displacement.
    These functions create lists of random walkers who start from 0
    and move 100 spaces randomly. It then bootstraps that calculation
    for the number of trials prefered. Finally, I calculated the average
    by summing those calculations and dividing by the numbewr of trials.

    ave_signed_displacement = -0.82
    ave_squared_displacement = 74.36
"""
