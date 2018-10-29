import time
from turtle import *
from random import *

def btc(trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    width(10)
    clr = (1, 0.84, 0)
    color(clr)
    if levels == 0:
        return
    else:
        dot(10)
        left(90)
        forward(trunklength)
        right(180)
        btc(trunklength/4, levels - 1)
        left(90)
        forward(trunklength/6)
        right(90)
        forward(trunklength/8)
        right(90)
        forward(trunklength/6)
        left(90)
        forward(trunklength/4)
    
        backward(trunklength)
