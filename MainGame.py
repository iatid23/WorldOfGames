from Live import load_game, welcome, input_and_check_hello
from Utils import Screen_cleaner

Screen_cleaner()
name = input_and_check_hello()
print(welcome(name))
load_game()
#play(5)
#money_play(3)
#memory_play(4)

