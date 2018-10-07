# CS5 Gold/Black, hw4pr1
# Filename: hw4pr1.py
# Name: Austin Long
# Problem description: Binary <-> decimal conversions

def isOdd(n):
    """Returns true if n is odd and False if n is even
    """
    return n%2 == 1

assert not isOdd(42)
assert isOdd(43)

def numToBinary(N):
    """converting decimal to binary
    """
    if N == 0:
        return ''
    else:
        return numToBinary(N//2) + str(N%2)


assert numToBinary(0) == ''
assert numToBinary(1) == '1'
assert numToBinary(4) == '100'
assert numToBinary(10) == '1010'
assert numToBinary(42) == '101010'
assert numToBinary(100) == '1100100'

def binaryToNum(S):
    """converting from base 2 to base 10
    """
    if S == '':
        return 0
    else:
        return   2 * binaryToNum(S[:-1])+ int(S[-1])


assert binaryToNum('') == 0
assert binaryToNum('101010') == 42

def increment(S):
    """returns the next largest number in Base 2
       accepts an 8-character string of 0's and 1's
    """
    if S == '':
        return 0
    elif S == '11111111':
        return '00000000'

    x = binaryToNum(S)
    x = x + 1
    y = numToBinary(x)
    return '0'* (len(S)- len(str(y)))+ y

assert increment('00000000') == '00000001'
assert increment('00000001') == '00000010'
assert increment('00000111') == '00001000'
assert increment('11111111') == '00000000'

def count(S, n):
    """counts n times upward from s, printing as it goes
    """
    if n == 0:
        print(S)
    else:
        print(S)
        count(increment(S), n - 1)

count("00000000", 4)
print()
count("11111110", 5)

# The ternary value for 59 is 2012 becuase evaluated from right to left. 2*27, 0*9,
# 1*3, and 2*1 adds up tp 59.

def numToTernary(N):
    """converts decimal to ternary(base3)
    """
    if N == 0:
        return ''
    else:
        return numToTernary(N//3) + str(N%3)

def ternaryToNum(S):
    """converts ternary(base3) to decimal
    """
    if S == '':
        return 0

    # if the last digit is a '2'...
    elif S[-1] == '2':
        return 3*ternaryToNum(S[:-1]) + 2

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return 3*ternaryToNum(S[:-1]) + 1

    else: # last digit must be '0'
        return 3*ternaryToNum(S[:-1]) + 0

assert numToTernary(42) == '1120'
assert numToTernary(4242) == '12211010'
assert ternaryToNum('1120') == 42
assert ternaryToNum('12211010') == 4242

def numToBalancedTernary(N):
    """converts decimal into a balanced ternary string
    """
    if N == 0:
        return ''
    elif N%3 == 1:
        return numToBalancedTernary((N-1)/3) + '+'
    elif N%3 == 0:
        return numToBalancedTernary(N/3) + '0'
    elif N%3 == 2:
        return numToBalancedTernary((N+1)/3) + '-'

def balancedTernaryToNum(S):
    """converts balanced ternary to decimal
    """
    if S == '':
        return 0

    # if the last digit is a '-'...
    elif S[-1] == '-':
        return 3*balancedTernaryToNum(S[:-1]) - 1

    # if the last digit is a '+'...
    elif S[-1] ==  '+':
        return 3*balancedTernaryToNum(S[:-1]) + 1

    else: # last digit must be '0'
        return 3*balancedTernaryToNum(S[:-1]) + 0

assert balancedTernaryToNum('+---0') == 42
assert balancedTernaryToNum('++-0+') == 100
assert numToBalancedTernary(42) == '+---0'
assert numToBalancedTernary(100) == '++-0+'
