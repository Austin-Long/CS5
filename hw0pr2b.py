# coding: utf-8
#
# hw0pr2b.py
#

"""
Title for your adventure:   The Dodd Quest 1.0.

Notes on how to "win" or "lose" this adventure:
  To win, choose the .
  To lose, choose the door.

"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 0.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    username = input("Who goes there? ")

    print()
    print("Welcome,", username, " to the world of Dodd, a galaxy filled with hidden wonders")
    print("and scary monsters! If you seek fame and fortune, conquer Dodd")
    print()
    print("There are three keys you will need in order to find the chest")
    print("Key 1: The poptart key")
    print("Key 2: The cookie key")
    print("Key 3: The ice cream key")
    print()

    print("Your quest: Find all three keys on the world of Dodd, so that you can open the chest!")
    print("To earn the poptart key you must answer just one question correctly...")
    print()
    pop()

    print("You are now entering the cookie monsters office!! The cookie key is near.\n\n")
    print("The office is dark and hazy, a large green figure approaches from the corner")
    print("it carries a huge plate of cookies in one hand and a large laptop in the other")
    print("the monster hisses and asks - Do you prefer chocolate chip or peanut butter?.")
    time.sleep(delay)
    print()

    key2 = input("Do you want a chocolate chip or peanut butter cookie? ")
    print()

    if key2 == "chocolate chip":
        print("The cookie monster leans over...")
        time.sleep(delay)
        print("...and pours you a glass of milk to eat with your chocolate chip cookie!")
        print("You pass the second challenge and gain the cookie key!")
        print("You have done very well, but now you must enter the land of snow", username, "!")
        choice()
    else:
        print("The cookie monster is incredibly angry!")
        print("he makes you watch as he eats every last cookie on the plate")
        time.sleep(delay)
        print("...when he finishes his plate he turns around")
        print("Huge and furry, it towers over you, it starts to sit down and the whole room goes dark")
        print("under the crushing weight of the monster, you are smashed into the office carpet")
        print("The monster laughs...You have failed,", username, ".")

def choice():
    choice = input("Welcome to the land of the snow! A crazy old woman lives in these hills, would you like to enter? (y/n) ")
    if choice == 'y':
        print("You are a brave traveler...Great riches are abound.")
        snow()

def pop():
    key1 = input("If you had to eat one poptart for the rest of your life, what flavor would you choose? ")
    if key1 == "brown sugar":
        print("You show deep poptart experience! You have earned the poptart key and may continue on.")
        print()
    elif key1 == "s'mores":
        print("Wrong wrong wrong! Try again! ")
        pop()
    elif key1 == "strawberry":
        print("Not a bad choice, but still lame! Go again!")
        pop()
    else:
        print("Not even close...guess again!")
        pop()

def snow():
    print("A large ice cream truck with loud music approaches...")
    print("A woman wearing a bright pink gown gets out of the truck")
    print("\"Would you like to try some ice cream?\" she says.")
    print()
    print("Careful! You have heard stories about people eating too much ice cream")
    key3 = input("How many scoops would you like? (3,4 or 5 scoops) ")
    if key3 == '3':
        print("\"OH HONEY, you look like you could really use more!\" ")
        choice2 = input("Are you sure you only want 3? (y/n)")
        if choice2 == 'n':
            print("Very good, five scoops of vanilla should do it.")
            end()
        elif choice2 =='y':
            print("How could you be so disrespectul! She scoops you three scoops and you begin to eat...")
            print("Funny, everything is becoming blurry and you fall into a large pile of yellow snow!")
            print("HAHAHA,", username, "next time you should accept my hospitality!")

    elif key3 == '4':
        print("That was a smart decision, she makes you a great big dish of vanilla,")
        print("chocolate, strawberry, and cookie dough ice cream")
        end()
    else:
        end()

def end():
    print("The ice cream key is now yours!")
    print("You have earned all three keys!!! You may now open the hidden chest...")
    print("You open the chest, eyes gleaming, the chest is filled to the brim with poptarts!")
    print("Every flavor you can imagine, but you are not hungry! It must have been all that ice cream you ate")
    print("No matter, you have enough poptarts to make it through the semester. Enjoy!")
