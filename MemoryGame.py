from time import sleep
import random
from Utils import Screen_cleaner
def show_fast(items):
    count = [5, 4, 3, 2, 1, 0]
    i = 0
    for item in count:
        sleep(1)
        bar = ':)' * i
        print(f'\r{item} {bar}', end=' \r')
        i = i + 1
        sleep(0.1)
    print(f'{items}', end='                       \r')
    sleep(0.7)
    print('    ', end='\r')

# The purpose of memory game is to display an amount of random numbers to the users for 0.7 seconds
# and then prompt them from the user for the numbers that he remember.
# If he was right with all the numbers the user will win, otherwise he will lose

def generate_sequence(diff):
    # Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
    list = []
    i = 0
    for i in range(int(diff)):
        list.append(random.randint(1, 101))
    print('in 5 second the list will appear for 0.7 seconds - get ready \n')
    x = input('are you ready... ? if so please press enter to start')
    show_fast(list)
    #print(f'random list is -  {list}')
    return list

def get_list_from_user(diff):
    # Will return a list of numbers prompted from the user. The list length will be in the size of difficulty.
    list = []
    print('Ok.... Now your turn \n')
    print(f'Please enter {diff} numbers as you remember press enter whrn you are ready \n')

    i = 0
    for items in range(0, diff):
        while True:
            x = input(f'{i+1}) ')
            try:
                list.append(int(x))
                i += 1
                break
            except:
                print('You did not entered a number, please try again')
                continue
   #print(f'your list is -  {list}')
    return list

def is_list_equal(list1, list2):
    # A function to compare two lists if they are equal. The function will return True/False.
    list1.sort()
    #print(list1)
    list2.sort()
    #print(list2)
    if list1 == list2:
        print("Great you Won!!")
        sleep(3)
        oScreen_cleaner()
        return True
    else:
        print("Oh .. never mind . you could try again another time")
        sleep(3)
        Screen_cleaner()
        return False

def play(diff):
    # Will call the functions above and play the game. Will return True/False if the user lost or won.
    list1 = generate_sequence(diff)
    list2 = get_list_from_user(diff)
    boo = is_list_equal(list1, list2)
    #print(boo)
    return boo
