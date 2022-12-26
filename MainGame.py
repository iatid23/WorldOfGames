from Live import load_game, welcome, input_and_check_hello

#name = input_and_check_hello()
#print(welcome(name))
#load_game()
#play(5)
#money_play(3)

from time import sleep

def loadbar(iteration, total, length=10):
   filledLength = int(length * iteration // total)
   bar = '.' * filledLength
   print(f'\r{bar}', end='\r')
   if iteration == total:
      print()

items = list(range(0, 10))
l = len(items)

loadbar(0, l, length=l)
for i, item in enumerate(items):
   sleep(0.1)
   loadbar(i + 1, l, length=l)
   sleep(0.1)