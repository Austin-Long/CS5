# Austin Long
# hw3pr2.py


#encipher
def encipher(S, n):
    """Returns a new string in which the letters in S have been rotated by n
       characters forward
       Arguments: a string S, a non-negative integer between 0 and 25 n
    """
    if len(S) == 0:
        return ''
    else:
        return rot(S[0], n) + encipher(S[1:], n)


def rot(c, n):
    """rotates c, a single character, forward by n spots in the alphabet
    """
    if 'a' <= c <= 'z':
        if ord(c) + n <= ord('z'):
            return chr(ord(c) + n)
        else:
            return chr(ord(c) + n - 26)

    elif 'A' <= c <= 'Z':
        if ord(c) + n <= ord('Z'):
            return chr(ord(c) + n)
        else:
            return chr(ord(c) + n - 26)
    else:
        return c

assert encipher('xyza', 1) == 'yzab'
assert encipher('Z A', 1) == 'A B'
assert encipher('*ab?', 1) == '*bc?'
assert encipher('This is a string!', 1) == 'Uijt jt b tusjoh!'
assert encipher('Caesar cipher? I prefer Caesar salad.', 25) == 'Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'



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



def scrabbleScore(S):
    """returns the scrabble score of a string
       Argument S: a string of only lowercase letters
    """
    if S == '':
        return 0
    else:
        return letterScore(S[0:1]) + scrabbleScore(S[1:])

# Use scrabbleScore to determine Englishness of string
# This works by assigning strings with common letters such as vowels
# low scores as a result, the min scrabble score will provide a good
# approximation of the englishness of a string

def decipher(S):
    """Given a String S, shifted by a certain integer
       Returns the most english string using scrabbleScore to rotate the string
    """
    L = [encipher(S, n) for n in range(26)]
    LOL = [[scrabbleScore(x), x] for x in L]
    best = min(LOL)
    return best[1]

assert decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.') == 'Caesar cipher? I prefer Caesar salad.'
assert decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla '\
              'lclyfaopun dl ohcl slhyulk.') == 'An education is what remains after we forget everything we have learned.'
print('This is the printed output of the call, decipher(\'Onyx balks\')')
print(decipher('Onyx balks'))


def count(e, L):
    """Takes a list L and returns the number of e's in L
    """
    LC = [1 for x in L if x == e]
    return sum(LC)

def blsort(L):
    """takes in a list of 0's and 1's
       returns the list sorted from smallest to largest
    """
    x = 0
    y = 0
    if len(L) == 0:
        return L

    x = count(0, L)
    y = count(1, L)
    return x * [0] + y * [1]


assert blsort([1, 0, 1]) == [0, 1, 1]
assert blsort([1, 0, 1, 0, 1, 0, 1]) == [0, 0, 0, 1, 1, 1, 1]



def remOne(e, L):
    """returns a list L with one e removed
    """
    if len(L) == 0:
        return L
    elif L[0] != e:
        return L[0:1] + remOne(e, L[1:])
    else:
        return L[1:]


def gensort(L):
    """A general purpose sorting function, accepts a list L
       Returns: a list with the same elements as L, but in ascending order
    """
    if len(L) == 0:
        return L
    else:
        m = min(L)
        L = remOne(m, L)
        return [m] + gensort(L)

assert gensort([42, 1, 3.14]) == [1, 3.14, 42]
assert gensort([7, 9, 4, 3, 0, 5, 2, 6, 1, 8]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def jscore(S, T):
    """Returns the "jotto score" of two strings S and T
       jotto score: the number of characters in S that are shared by T,
       repeated letters are counted multiple times
    """
    if len(S) == 0 or len(T) == 0:
        return 0
    if S[0] in T:
        return count(S[0], T)
    else:
        return jscore(S[1:], T)


assert jscore('diner', 'syrup') == 1
assert jscore('geese', 'elate') == 2
assert jscore('gattaca', 'aggtccaggcgc') == 5
assert jscore('gattaca', '') == 0



def exact_change(target_amount, L):
    """Returns True or False, depending on whether its possible to create the
       target_amount by adding up all or some of the values in L
       Arguments: non-negative integer, target_amount and a list L pf positive integers
    """
    if len(L) == 0 and target_amount > 0:
        return False
    elif target_amount < 0:
        return False
    elif target_amount == 0:
        return True
    elif len(L) == 1:
        if L[0] == target_amount:
            return True
        else:
            return False

    x = exact_change(target_amount - L[0], L[1:])
    y = exact_change(target_amount, L[1:])
    if x == True or y == True:
        return True
    else:
        return False

assert exact_change(42, [25, 1, 25, 10, 5, 1]) == True
assert exact_change(42, [25, 1, 25, 10, 5]) == False
assert exact_change(42, [23, 1, 23, 100]) == False
assert exact_change(42, [23, 17, 2, 100]) == True
assert exact_change(42, [25, 16, 2, 15]) == True
assert exact_change(0, [4, 5, 6]) == True
assert exact_change(-47, [4, 5, 6]) == False
assert exact_change(0, []) == True
assert exact_change(42, []) == False

def LCS(S, T):
    """ returns the longest common subsequence that S and T share
        arguments: accepts two strings, S and T
    """
    if S == '' or T == '':
        return ''
    elif S[0] == T[0]:
        return S[0:1] + LCS(S[1:],T[1:])

    result1 = LCS(S[1:], T)
    result2 = LCS(S, T[1:])
    if S[0] != T[0]:
        if len(result1) > len(result2):
            return result1
        else:
            return result2

assert LCS('human', 'chimp') == 'hm'
assert LCS('gattaca', 'tacgaacta') == 'gaaca'
assert LCS('wow', 'whew') == 'ww'
assert LCS('', 'whew') == ''
assert LCS('abcdefgh', 'efghabcd') == 'abcd'
