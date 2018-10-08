# CS5 Gold/Black, hw4pr2
# Filename: hw4pr2.py
# Name: Austin Long
# Problem description: Conversions and Compressions

def numToBaseB(N, B):
    """returns a string representing the number N in base B
    """
    if N == 0:
        return ''
    else:
        return numToBaseB(N//B, B) + str(N%B)

assert numToBaseB(3116, 9) == '4242'
assert numToBaseB(141474, 8) == '424242'
assert numToBaseB(0, 4) == ''
assert numToBaseB(42, 5) == '132'

def baseBToNum(S, B):
    """returns an integer in base B representing the same number as S
    """
    if S == '':
        return 0
    else:
        return B * baseBToNum(S[:-1], B) + int(S[-1])


assert baseBToNum('5733', 9) == 4242
assert baseBToNum('1474462', 8) == 424242

def baseToBase(B1, B2, s_in_B1):
    """Returns a string representing the same number as s_in_B1, but in base B2
       Accepts: a base B1, base B2, s_in_B1 a string representing a number in B1
    """
    a = baseBToNum(s_in_B1, B1)
    b = numToBaseB(a, B2)
    return b

assert baseToBase(2, 4, '101010') == '222'
assert baseToBase(2, 5, '1001001010') == '4321'

def add(S, T):
    """Returns the (binary)sum of two binary strings S and T
    """
    a = baseBToNum(S, 2)
    b = baseBToNum(T, 2)
    c = a + b
    return numToBaseB(c, 2)



assert add("11", "1") == '100'
assert add("11", "100") == '111'



def addB(S, T):
    """returns a new string representing the sum of the two argument strings
       Accepts: two string arguments, S and T
    """
    if S == '':
        return T
    elif T == '':
        return S

    # There will be four recursive cases--here is the first one:
    if S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'   # 0 + 0 == 0
    elif S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'
    elif S[-1] == '1' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '1'
    elif S[-1] == '1' and T[-1] == '1':
        return addB(addB('1', S[:-1]), T[:-1]) + '0'

    # three more recursive cases still to specify...


assert addB('11', '100') == '111'
assert addB("11100", "11110") == '111010'



def compress(S):
    """Returns a binary string, run length encoding
       Accepts: a binary string S of length less than or equal to 64
    """
    count = 1
    result = ''

    for x in range(1, len(S)):
        if S[x] != S[x - 1]:
            result += S[x - 1]
            z = numToBaseB(count, 2)
            result += '0' *(7 - len(z)) + z
            count = 1
        else:
            count += 1
    z = numToBaseB(count, 2)
    result += S[len(S) - 1] + '0' * (7 - len(z)) + str(z)
    return result


def binaryToNum(S):
    """converting from base 2 to base 10
    """
    if S == '':
        return 0
    else:
        return   2 * binaryToNum(S[:-1])+ int(S[-1])

def uncompress(C):
    """inverts" or "undoes" the compressing in your compress function. That is,
       uncompress(compress(S)) should give back S
    """
    result = ""
    for x in range(0, len(C), 8):
        result += C[x]*(baseBToNum(C[x+1:x+8], 2))
    return result

assert compress(64*'0') == '01000000'
assert uncompress(compress(64*'0')) == 64*'0'
