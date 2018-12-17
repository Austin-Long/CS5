# hw8pr1.py
# Lab 8
#
# Name: Austin Long
#

# keep this import line...
from cs5png3 import *


#
# a test function...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300,200)  # creates an image of width=300, height = 200

    # Nested loops!
    for r in range(200):  # loops over the rows with runner-variable r
        for c in range(300):  # loops over the cols with c
            if  c == r:
                im.plotPoint( c, r, (255,0,0))
            #else:
            #    im.plotPoint( c, r, (255,0,0))

    im.saveFile()

#
# start your Lab 8 functions here:
#

def mult(c, n):
    """returns a product c times n
       accepts an integer c and n
    """
    result = 0
    for i in range(n):
        result += c
    return result

assert mult(3, 5) == 15
assert mult(6, 7) == 42
assert mult(1.5, 28) == 42.0

def update(c, n):
    """returns an updated z value using z = z**2 + c a total of n times
       accepts values c and n
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

assert update(1, 3) == 5
assert update(-1, 3) == -1
assert update(-1, 10) == 0

def inMSet(c, n):
    """inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
       Then, it returns
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0 + 0j
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True


def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0  or  row % 10 == 0:
        return True
    else:
        return False

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file
    # the image would change to a grid if the and was changed to an or
    # because the function would return true more often

    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    """scale accepts
           pix, the CURRENT pixel column (or row)
           pixMax, the total # of pixel columns
           floatMin, the min floating-point value
           floatMax, the max floating-point value
       scale returns the floating-point value that
           corresponds to pix
    """
    return floatMin + pix/pixMax * (floatMax - floatMin)

assert scale(100, 200, -2.0, 1.0) == -0.5
assert scale(100, 200, -1.5, 1.5) == 0.0
assert scale(100, 300, -2.0, 1.0) == -1.0
assert scale(25, 300, -2.0, 1.0) == -1.75
assert round(scale(299, 300, -2.0, 1.0), 2) == 0.99

def mset():
    """Creates a 300x200 image of the Mandelbrot set
    """
    NUMITER = 25   # of updates
    XMIN = -2.0   # the smallest real coordinate value
    XMAX =  1.0  # the largest real coordinate value
    YMIN = -1.0  # the smallest imag coordinate value
    YMAX = 1.0   # the largest imag coordinate value
    width = 600
    height = 400
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            # Use scale twice:
            #   once to create the real part of c (x)
            x = scale(col, width, XMIN, XMAX)
            #   once to create the imaginary part of c (y)
            y = scale(row, height, YMIN, YMAX)
            # THEN, create c, choose n, and test:
            c = x + y*1j
            if inMSet(c, NUMITER):
                image.plotPoint(col, row, (255, 0, 10))
            else:
                image.plotPoint(col, row, (0, 0, 0))

    # we looped through every image pixel; we now write the file
    image.saveFile()


def example():
    """Shows how to access the pixels of an image.
       inputPixels is a list of rows, each of which is a list of columns,
           each of which is a list [r,g,b]
    """
    NUMITER = 25   # of updates
    XMIN = -2.0   # the smallest real coordinate value
    XMAX =  1.0  # the largest real coordinate value
    YMIN = -1.0  # the smallest imag coordinate value
    YMAX = 1.0   # the largest imag coordinate value
    inputPixels = getRGB("./pngs/alien.png")
    inputPixels = inputPixels[::-1] # the rows are reversed

    height = len(inputPixels)
    width = len(inputPixels[0])
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            # Use scale twice:
            #   once to create the real part of c (x)
            x = scale(col, width, XMIN, XMAX)
            #   once to create the imaginary part of c (y)
            y = scale(row, height, YMIN, YMAX)
            # THEN, create c, choose n, and test:
            c = x + y*1j
            if inMSet(c, NUMITER):
                image.plotPoint(col, row, inputPixels[row][col])
            else:
                image.plotPoint(col, row, (0, 0, 0))

    # we looped through every image pixel; we now write the file
    image.saveFile()
