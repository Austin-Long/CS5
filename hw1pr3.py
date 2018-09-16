# Date: 9/15/18
# Filename: hw1pr3.py
# Name: Austin Long
# Problem description: Function Frenzy!

#
# leng example from class
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + leng(s[1:])

def flipside(s):
  """flipside swaps s's sides
     Argument s: a string
  """
  x = len(s)//2
  return s[x:] + s[:x]

#
# Tests
#
assert flipside('carpets')  == 'petscar'
assert flipside('homework') == 'workhome'
assert flipside('flipside') == 'sideflip'
assert flipside('az')       == 'za'
assert flipside('a')        == 'a'
assert flipside('')         == ''


def mult(n, m):
    """mult calculates n*m via recursion
       Argument: n, an integer
       Argument: m, an integer
    """
    if n == 0 or m == 0:
        return 0
    elif m < 0:
        return -n + mult(n, m + 1)
    else:
        return n + mult(n, m - 1 )

#
# Tests
#
assert mult(6, 7)   ==  42
assert mult(6, -7)  == -42
assert mult(-6, 7)  == -42
assert mult(-6, -7) ==  42
assert mult(6, 0)   ==   0
assert mult(0, 7)   ==   0
assert mult(0, 0)   ==   0


#
# leng example from class
#
def leng(s):
    """leng returns the length of s
        Yes, it's already built in as len(s), but...
        Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + leng(s[1:])

def dot(L, K):
    """dot returns the dot product of two list
       Argument L: a list of integers
       Argument K: a list of integers
    """
    if leng(L) != leng(K):
        return 0.0
    elif L == [] and K == []:
        return 0.0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

#
# Tests
#
assert dot([5, 3], [6, 4])                       == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6])                          == 0.0
assert dot([], [6])                              == 0.0
assert dot([], [])                               == 0.0

def ind(e, L):
    """Returns the index at which e is first found in L.
       Argument e: element of a sequence
       Argument L: a sequence, a string or a list
    """
    if L[0] == e:
        return 0
    elif e not in L:
        return len(L)
    else:
        return 1 + ind(e, L[1:])

#
# Tests
#
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100)))       == 42
assert ind('hi', ['hello', 42, True])     == 3
assert ind('hi', ['well', 'hi', 'there']) == 1
assert ind('i', 'team')                   == 4
assert ind(' ', 'outer exploration')      == 5

def letterScore(let):
    """Returns the value of the character as a Scrabble tile. If not one of the letters, returns 0
       Argument let: single-cahracter string
    """
    
