#
# hw11pr1.py
#
# name:Austin Long
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date(object):
    """A user-defined data structure that
       stores and manipulates dates.
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """Construct a Date with the given month, day, and year."""
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """This method returns a string representation for the
           object of type Date that calls it (named self).

           ** Note that this function _can_ be called explicitly, but
              it more often is used implicitly via the print statement
              or simply by expressing self's value.
        """
        s = "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
        return s


    # Here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew
    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
           whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==.  This way , we don't need to use the awkward
            d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False

    def isBefore(self, d2):
        """returns True if the calling object is a calendar date before the argument named ds"""
        if self.year < d2.year:
            return True
        elif self.month < d2.month and self.year == d2.year:
            return True
        elif self.day < d2.day and self.year == d2.year \
            and self.month == d2.month:
            return True
        else:
            return False

    def isAfter(self, d2):
        """returns true if the calling object is a calendar date after the
           argument named d2
        """
        if self.year > d2.year:
            return True
        elif self.month > d2.month and self.year == d2.year:
            return True
        elif self.day > d2.day and self.year == d2.year \
            and self.month == d2.month:
            return True
        else:
            return False

    def tomorrow(self):
        """changes the calling object so that it represents one calendar day after the date
           it originally represented.
        """
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28
        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day += 1

        if self.day > DIM[self.month]:
            self.month += 1
            self.day = 1
            if self.month > 12:
                self.year += 1
                self.month = 1

    def yesterday(self):
        """changes the calling object so that it represents one calendar day before the
           date it originally represented
        """
        if self.isLeapYear():
            fdays = 29
        else:
            fdays = 28
        DIM = [31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.day -= 1

        if self.day < 1:
            self.month -= 1
            self.day = DIM[self.month-1]
            if self.month < 1:
                self.year -= 1
                self.month = 12

    def addNDays(self, N):
        """changes the calling object so that it represents N calendar days after
           the date it orifinally represented
        """
        for x in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        """changes the calling object so that it represents N Calendar days
           before the date it originally represented
        """
        for x in range(N):
            self.yesterday()
            print(self)

    def diff(self, d2):
        """returns an integer representing the number of days between
           self and d2
        """
        self_copy = self.copy()
        d2_copy = d2.copy()
        day1 = self_copy.day
        day2 = d2_copy.day

        count = 0

        if self_copy == d2_copy:
            return 0

        while self_copy.isBefore(d2):
            self_copy.tomorrow()
            count-=1
        while self_copy.isAfter(d2):
            self_copy.yesterday()
            count+=1
        return count

    def dow(self):
        """returns a string that indicates the day of the week of the object that calls it
        """
        a = self.diff(Date(10,10,10))
        b = abs(a)
        if b%7 == 0:
            return "Sunday"
        elif b%7 == 1:
            return "Monday"
        elif b%7 == 2:
            return "Tuesday"
        elif b%7 == 3:
            return "Wednesday"
        elif b%7 == 4:
            return "Thursday"
        elif b%7 == 5:
            return "Friday"
        elif b%7 == 6:
            return "Saturday"



#
# be sure to add code for the Date class ABOVE--inside the class definition
#





#
# lots of dates to work with...
#
# The nice this about putting them here is that they get redefined with each run
#   of the software (and this is needed for testing!)
#

d = Date(11, 13, 2018)    # Today?
d2 = Date(12, 21, 2018)   # winter break
ny = Date(1, 1, 2018)   # new year
nd = Date(1, 1, 2020)   # new decade
nc = Date(1, 1, 2100)   # new century
graduation = Date(5, 15, 2022)   # alter to suit!
vacation = Date(5, 17, 2019)     # ditto ~ summer break!
sm1 = Date(10, 28, 1929)    # stock market crash
sn2 = Date(10, 19, 1987)    # another s.m. crash: Mondays in Oct. are risky...
