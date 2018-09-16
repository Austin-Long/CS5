
# CS5 Gold, Lab1 part 2
# Filename: hw1pr2.py
# Name:
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
    """Return value: sq returns the square of its Argument
       argument x: a number (int or float)
    """
    return x*x

def interp(low, hi, fraction):
    """Return value: the floating-point value that is fraction of the way between low and hi.
       Argument: three numbers, low, hi, fraction
    """
    return low + ((hi-low)*fraction)

def checkends(s):
    """Return value: True if first character in s is the same as last character
       Argument s: a string s
    """
    return s[0] == s[len(s)-1]

def flipside(s):
    """Return value: a string whose first half is s's second half and whose second half is s's second half.
       Argument s: a string s
    """
    round = len(s)//2
    return s[round:len(s)] + s[0:round]

def convertFromSeconds(s):
    """Return value: a list of four nonnegative
       integers that represents that number of seconds in a more conventional unit of time:
       Number of days, number of hours, number of minutes, number of seconds.
       Argument s: a nonnegative integer number of seconds s
    """
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // 60
    seconds = s % 60
    return [days, hours, minutes, seconds]
