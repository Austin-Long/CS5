# coding: utf-8
#
# the top line, above, is important --
# it ensures that Python will be able to use this file,
# even if you paste in text with Unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
#
# Name: Austin Long
#
#
import random

# function #1
#
def createDictionary(filename):
    """accepts a string(a textfile), returns a discitonary whose keys are words in the
       textfile and whose entries are a list of words that may follow the key word
    """
    d = {}
    f = open(filename)
    text = f.read()
    f.close()
    LoW = text.split()
    start = True

    for i in range(len(LoW)):
        if start:
            d.setdefault("$", []).append(LoW[i])
        else:
            d.setdefault(LoW[i-1], []).append(LoW[i])

        last = LoW[i][-1]
        if last == '.' or last == '?':
            start = True
        else:
            start = False
    return d



# function #2
#
def generateText(d, N):
    """
    accepts a dictionary of word transitions d (generated in your createDictionary
    function, above) and a positive integer, n. Then, generateText should print a
    string of n words
    """
    res = ""
    curr = "$"
    for i in range(N) :
        curr = random.choice(d[curr])
        res += " " + curr
        last = curr[-1]
        if last == '.' or last == '!' or last == '?' :
            curr = "$"
    return res[1:]





#
# Your 500-or-so-word CS essay (paste into these triple-quoted strings below):
#Lose Yourself by Eminem
"""Yo His hoes don't buy diapers And it's getting even harder tryin' to his sweater already, mom's spaghetti He's so hard And its gaping This
 opportunity To formulate a plot fore I was playin' in a snail I've got To formulate a lifetime you better lose yourself in Salem's lot So the moment
 You own daughter But hold your chance to his whole back to blow This world order A normal life and booed off like a lifetime you better never let it
 go You better go You own it, you had One shot Success is all changed I can't provide the moment You only motherfuckin' roof off like two dogs caged
I can't get one opportunity comes once in the music, the moment Would you better You only get one shot, do not miss your chance to Five and barely kn
ows that, but he goes back to reality, oh there goes on his mobile home, that's when he keeps on forgettin' What he knows his mobile home, he's grown
 farther from home, that's when its no movie, there's no movie, there's no Mekhi Phifer This opportunity comes once in the globetrotter Lonely roads,
 God damn food stamps don't matter, he's broke He's so stacked that he choked He's so hard And its gaping This world is my life is my life is my nine
 to Five and barely knows his whole crowd goes Rabbit, he keeps on the soap opera is my nine to say in a lifetime you set your chance to want to blow
 This opportunity that easy? Yo His hoes is borin', but the moment Would you capture this motherfuckin' option, failures not miss your nose dove and
I been chewed up between bein' a plot fore I kept rhymin' and hope it go You only get one shot, do not miss your chance to reality, oh there goes so

stacked that its gaping This opportunity comes once in a plot fore I was playin' in a lifetime you capture it go You own daughter But I can't get one
 moment You better lose yourself in the next cipher Best believe somebody's payin' the pied piper All the mood all over these times up, over, blaow!
Yo His hoes is told and too much For me king, as the right type of Life for the music, the moment You own it, you better lose yourself in Salem's lot
 So the moment and barely knows his own it, you better lose yourself in one shot, do not miss your chance to blow This opportunity comes once in a li
fetime you better You only get one shot, do not miss your chance to coast shows, he's dope, he choked He's so mad, but he goes the music, the music,
the next schmo who flows, he keeps on his mobile home, that's when its Back to go, I kept rhymin' and stepwritin' the surface he won't come out He's
nervous, but super stardom's close to say in Salem's lot

"""
#
#
