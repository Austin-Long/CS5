# hw8pr4.py
# Example user-interaction looping program
#  (a variant of the one done in class)
# Austin Long
import math

def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Input a new list")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the minimum and its day")
    print("(5) Find the maximum and its day")
    print("(6) Yout TT investment plan")
    print("(9) Quit")

def predict(L):
    """Predict ignores its argument and returns
       what the next element should have been.
    """
    return 42

def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:
            result = x
    return result

def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    minval = L[0]
    minloc = 0

    for i in list(range(len(L))):
        if L[i] < minval:  # a smaller one was found!
            minval = L[i]
            minloc = i

    return minval, minloc

def main():
    """The main user-interaction loop"""
    secret_value = 4.2

    L = [30, 10, 20]  # an initial list

    while True:     # the user-interaction loop
        menu()
        choice = input("Enter your choice: ")
        print()

        #
        # "Clean and check" the user's input
        #
        try:
            choice = int(choice)   # make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        # run the appropriate menu option
        #
        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 0:  # We want to enter a new List
            newL = input("Enter a new list of prices: ")    # enter _something

            #
            # "Clean and check" the user's input
            #
            try:
                newL = eval(newL)   # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]):
                    print("That didn't seem like a list. Not changing L.")
                else:
                    L = newL  # Here, things were OK, so let's set our list, L
            except:
                print("I didn't understand your input. Not changing L.")

        elif choice == 1:
            print("{0: >4}  {1: >6}".format("Day", "Price"))
            print("{0: >4}  {1: >6}".format("---", "-----"))
            for i in range(len(L)):
                print("{0: >4}   ${1: >2}".format(i, L[i]))

        elif choice == 2:  # Find the average stock price
            print('The average price is $', ave(L))


        elif choice == 3:  # Find the standard deviation
            print('The st. deviation is ', std(L))

        elif choice == 4:  # The minimum and its day
            m = find_min_loc(L)
            print("The minimum value in L is", m[0], ',occurs on day #', m[1])

        elif choice == 5:  # The maximum and its day
            maxval, maxloc = find_max_loc(L)
            print("The maximum value in L is", maxval, "occurs on day #", maxloc)

        elif choice == 6:  # My TTS investment plan
            x, y, z = plan(L)
            print("Your TTS investment strategy is to: ")
            print()
            print(' Buy on day', x, 'at price $', L[x])
            print(' Sell on day', y, 'at price $',L[y])
            print(' For a total profit of $',z)

        else:
            print(choice, "Thats a baaaad choice, its not on the menu!")

    print()
    print("See you yesterday! We are going to be rich!")



def ave(L):
    """returns the average of a list"""
    sum = 0
    for i in range(len(L)):
        sum += L[i]
    return sum/len(L)

def std(L):
    """calculates the standard deviation of a List"""
    sumdif = 0
    avg = ave(L)
    for x in L:
        sumdif += (x - avg)**2
    return math.sqrt(sumdif/len(L))

def find_max_loc(L):
    """find max loc uses a loop to return the maximum of L
            and the location (index or day) of that maximum.
        Argument L: a nonempty list of numbers.
        Results:  the largest value in L, its location (index)
    """
    maxval = L[0]
    maxloc = 0

    for i in list(range(len(L))):
        if L[i] > maxval:  # a smaller one was found!
            maxval = L[i]
            maxloc = i

    return maxval, maxloc

def plan(L):
    """returns the best days to buy and sell in order to maximize profit"""
    ans = []
    profit = -(2**30)
    for i in range(len(L)):
        for j in range(1, len(L)):
            if L[j] - L[i] > profit:
                profit = L[j] - L[i]
                ans = [i, j, profit]
    return ans
