# CS5 Gold, hw1pr1
# Filename: hw1pr1.py
# Name: Austin Long
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]
print(answer0)
print()

answer1 = e[1:]
print(answer1)
print()

answer2 = pi[5:6] + pi[1:4:2]
print(answer2)
print()

answer3 = pi[1:6]
print(answer3)
print()

answer4 = e[::-2] + pi[::2]
print(answer4)
print()

# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:  'hey'
answer5 = h[0] + h[4:6]
print(answer5)
print()

answer6 = c[0:4] + m[1:3] + h[4:5]
print(answer6)
print()

answer7 = h[1:] + m
print(answer7)
print()

answer8 = h[0:3] + m[2:3] + c[4:5] + 3*h[0:3]
print(answer8)
print()

answer9 = c[3:6] + c[1:2] + m[0:1] + h[5:6] + c[4:6] + c[1:2]
print(answer9)
print()

answer10 = c[0:5:2] + h[1:3] + c[0:1] + h[1:2] + c[2:4]
print(answer10)
print()
