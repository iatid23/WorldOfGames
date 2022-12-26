import matplotlib

import random
import threading
import time
import os
import time
import pylab as pl
from IPython import display
from time import sleep
import IPython
#from IPython.display import display, update_display

import time
import pylab as pl
from IPython import display

def clearAfter15():
    clear = lambda: os.system('cls')
    clear()

# The purpose of memory game is to display an amount of random numbers to the users for 0.7 seconds
# and then prompt them from the user for the numbers that he remember.
# If he was right with all the numbers the user will win, otherwise he will lose

def generate_sequence(diff):
    # Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
    # list = []
    # i = 0
    # for i in range(int(diff)):
    #     list.append(random.randint(1, 101))

    for i in range(10):
        pl.plot(pl.randn(100))
    display.clear_output(wait=True)
    display.display(pl.gcf())
    time.sleep(1.0)
    # out = display(IPython.display.display_pretty('Starting'), display_id=True)
    # time.sleep(1)
    #
    # for i in range(10):
    #     out.update(IPython.display.display_pretty('Going' + '.' * (i % 3 + 1)))
    #     time.sleep(1)
    #
    # out.update(IPython.display.display_pretty('Done.'))


def get_list_from_user():
    return 0
    # Will return a list of numbers prompted from the user. The list length will be in the size of difficulty.


def is_list_equal():
    # A function to compare two lists if they are equal. The function will return True/False.
    return 0

def play(diff):
    # Will call the functions above and play the game. Will return True/False if the user lost or won.
    generate_sequence(diff)
    return 0
