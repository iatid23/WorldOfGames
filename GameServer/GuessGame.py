import random
from time import sleep
from Utils import Screen_cleaner
# The purpose of the guess game is to start a new game,
# cast a random number between 1 to a variable called difficulty.

def generate_number(diff):
    # generates number between 1 to diffculty and save it to secret_number
    secret_number = random.randint(1, int(diff))
    return int(secret_number)

def get_geuss_from_user(diff):
    # will prompt the user for a number between 1 to difficulty and return the number.
    con = True
    while con:
        guess = input(f'Please choose a number between 1 and {diff} as your guess \n')
        if guess.isnumeric():
            if not (1 <= int(guess) <= 5):
                print("You have entered a number not in range please try again")
                sleep(0.1)
                continue
            else:
                sleep(0.1)
                return gss
        else:
            print("Its not a number please try again")
            sleep(0.1)
            continue
        sleep(0.1)

def compare_results(secret_number, guess):
    # will compare the secret generated number to the one prompted by the get_geuss_from_user.
    boo = False
    if guess == secret_number:

        boo = True
        return boo
    else:
        return boo

def play(diff):
    # Will call the functions above and play the game. Will return True/False if the user lost or won.
    # First - lets get new secret number
    more = True
    secret_num = generate_number(diff)
    while more:
        # lets get a guess
        guess = get_geuss_from_user(diff)
        # lets play
        compare = compare_results(secret_num, guess)
        if compare :
            print("Correct!!! - Congratulations you did it ")
            sleep(2)
            Screen_cleaner()
            sleep(0.1)
            more = False
            return True
        else:
            print("nice try - better luck next time")
            print("You are most welcome to try again")
            x = input("Please Press 'Enter' to try again or any other key to exit \n")
            if x == '':
                sleep(2)
                Screen_cleaner()
                sleep(0.1)
                continue
            else:
                print("Thank you - Hope to see you soon - Bye Bye :) ")
                sleep(2)
                Screen_cleaner()
                more = False
                sleep(0.1)
        sleep(0.1)
        return False



