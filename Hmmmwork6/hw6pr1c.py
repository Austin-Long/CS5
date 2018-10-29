#
# hw6pr1c.py - checking uniqueness  (for the random-number generator in Hmmm)
#    The test(S) function is already here (below).
#
# Name: Austin Long
#
# You'll paste your 100 numbers in this triple-quoted string:
NUMBERS = """
83
44
25
26
47
88
49
30
31
52
93
54
35
36
57
98
59
40
41
62
3
64
45
46
67
8
69
50
51
72
13
74
55
56
77
18
79
60
61
82
23
84
65
66
87
28
89
70
71
92
33
94
75
76
97
38
99
80
81
2
43
4
85
86
7
48
9
90
91
12
53
14
95
96
17
58
19
0
1
22
63
24
5
6
27
68
29
10
11
32
73
34
15
16
37
78
39
20
21
42
"""

def unique( L ):
    """
    input: a list
    ouput: checks if the list is unique, outputs true if no repeated elements
    """
    if len(L) == 0:     # handle base case
        return True
    elif L[0] in L[1:]:     # check whether L[0] re-appears
        return False
    else:
        return unique(L[1:])




def test(S):
    """test accepts a triple-quoted string, S,
       containing one number per line. Then, test
       returns True if those numbers are all unique
       (or if S is empty); otherwise it returns False
    """
    S = S.strip()               # remove all spaces in front & back of S
    ListOfStrings = S.split()   # split S at each space or newline
    # print("ListOfStrings is", ListOfStrings)
    ListOfIntegers = [int(s) for s in ListOfStrings]  # convert each to an int
    # print("ListOfIntegers is", ListOfIntegers)
    return unique(ListOfIntegers)

# Try it!
result = test(NUMBERS)
print("\nUniqueness test:  The result is", result, "\nI used 21 for a and 1 for c to get 100 unique random values.")
