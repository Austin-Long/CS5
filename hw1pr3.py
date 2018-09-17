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
       Argument let: single-character string
    """
    if let in 'qz':
        return 10
    elif let in 'aeilnorstu':
        return 1
    elif let in 'dg':
        return 2
    elif let in 'bcmp':
        return 3
    elif let in 'fhvwy':
        return 4
    elif let in 'k':
        return 5
    elif let in 'jx':
        return 8
    elif let in 'qz':
        return 10
    else:
        return 0

#
# Tests
#
assert letterScore('j') == 8
assert letterScore('w') == 4
assert letterScore('%') == 0


def scrabbleScore(S):
    """returns the scrabble score of a string
       Argument S: a string of only lowercase letters
    """
    if S == '':
        return 0
    else:
        return letterScore(S[0:1]) + scrabbleScore(S[1:])

#
# Tests
#
assert scrabbleScore('quetzal')                    == 25
assert scrabbleScore('jonquil')                    == 23
assert scrabbleScore('syzygy')                     == 25
assert scrabbleScore('abcdefghijklmnopqrstuvwxyz') == 87
assert scrabbleScore('?!@#$%^&*()')                == 0
assert scrabbleScore('')                           == 0



def one_dna_to_rna(c):
        """Converts a single-character c from DNA
           nucleotide to complementary RNA nucleotide """
        if c == 'A':
            return 'U'
        elif c == 'C':
            return 'G'
        elif c == 'G':
            return 'C'
        elif c == 'T':
            return 'A'
        else:
            return ''


def transcribe(S):
    """Returns the messenger RNA that would be produced from the string S.
       Argument S: string S, containing DNA nucleotides(AS, CS, GS, TS)
    """

    if len(S) == 0:
        return ''
    else:
        return one_dna_to_rna(S[0]) + transcribe(S[1:])


#
# Tests
#
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU' # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that the other characters disappear
assert transcribe('')         == ''
