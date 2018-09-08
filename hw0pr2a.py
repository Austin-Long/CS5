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
   user = input("Choose your weapon: (rock, paper, or scissors) ")
   comp = random.choice(['rock','paper','scissors'])
   print()

   print('The user (you)   chose', user)
   print('The computer (I) chose', comp)
   print()

   if user != ('rock' or 'paper' or 'scissors'):
       print("Invalid weapon selection! Play again!")
       rps()

   if user == 'rock' and comp == 'paper':
       print('I WIN! HAHAHAHAHA, you can not defeat the machine!')
       print('Better luck next time...')
   elif user == 'rock' and comp == 'rock':
       print('Wow, it looks like we tied! Let\'s go again')
       rps()
   elif user == 'rock' and comp == 'scissors':
      print('Rock crushes scissors! It looks like you have bested me... :( It will not happen again.')


   if user == 'paper' and comp == 'scissors':
       print('I WIN! Scissors cuts paper! HAHAHA, you can not defeat the machine!')
       print('Better luck next time...')
   elif user == 'paper' and comp == 'paper':
       print('Wow, it looks like we tied! Let\'s go again')
       rps()
   elif user == 'paper' and comp == 'rock':
       print('Paper smothers Rock! It looks like you have bested me... :( It will not happen again.')


   if user == 'scissors' and comp == 'rock':
       print('I WIN! Rock crushes scissors! HAHAHAHAHA, you can not defeat the machine!')
       print('Better luck next time...')
   elif user == 'scissors' and comp == 'scissors':
       print('Wow, it looks like we tied! Let\'s go again')
       rps()
   elif user == 'scissors' and comp == 'paper':
       print('Scissors cuts paper! It looks like you have bested me... :( It will not happen again.')
