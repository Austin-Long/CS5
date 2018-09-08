# coding: utf-8
#
# hw0pr2a.py
#

import random          # imports the library named random

def rps():
   """ this plays a game of rock-paper-scissors
       (or a variant of that game)
       arguments: no arguments    (prompted text doesn't count as an argument)
       results: no results        (printing doesn't count as a result)
   """
   user = input("Choose your weapon: ")
   comp = random.choice(['rock','paper','scissors'])
   print()

   print('The user (you)   chose', user)
   print('The computer (I) chose', comp)
   print()

   if user == 'rock' and comp == 'paper':
       print('I WIN! HAHAHAHAHA, you can not defeat the machine!')
       print('Better luck next time...')
   elif user == 'rock' and comp == 'rock':
       print('Wow, it looks like we tied! Let\'s go again')
       rps()
   else:
      print('It looks like you have bested me... :( It will not happen again')
