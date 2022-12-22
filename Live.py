from GuessGame import play
from MemoryGame import play as memory_play
from CurrencyRouletteGame import play as money_play
import os
choice_dictionary_content = {1: 'a sequence of numbers will appear for 1 second and you have to  guess it back',
                             2: 'guess a number and see if you chose like the computer',
                             3: 'Roulette - try and guess the value of a random amount of USD in ILS'}
choice_dictionary = {1: 'Memory Game', 2: 'Guess Game', 3: 'Currency Roulette'}
difficulty_dictionary = {1: 'Super Easy', 2: 'Easy', 3: 'Medium', 4: 'Hard', 5: 'Extreme'}
#def clear():
    # check and make call for specific operating system
    #os.system('cls' if os.name == 'nt' else 'clear')
    #print('\n' * 40)



def input_and_check_num(num, str):
    while True:
        try:
            choice = input(f'Enter Your {str} : \n')
            c = int(choice)
        except ValueError:
            print("You didn't enter a number please choose again")
            continue
        if 1 <= c <= num:
            return c
        else:
            print(f"You didn't enter a number between 1 or {num}, please enter again")
            continue

def input_and_check_hello():
    while True:
        name = input(f'Please Enter Your name : \n')
        typ = type(name)
        if typ != str:
            print("You didn't entered string name, please enter your name again")
        try:
            int(name)
            print("You entered a number not your name, please enter your name again")
            continue
        except ValueError:
            if name == '' or name == ' ':
                print("You didn't enter chars please enter your name again")
                continue
            else:
                return name


def welcome(name):
    ret_str = f''' Hello {name} and welcome to the world of games
Here you can find many cool games to play
__________________________________________________'''

    return ret_str


def load_game():
    global choice_dictionary, difficulty_dictionary, choice_dictionary_content
    y = 1
    print(f'Please choose a game to play:')
    while y <= len(choice_dictionary) :
        print(f'{y}. {choice_dictionary[y]} - {choice_dictionary_content[y]}')
        y = y + 1
    # check error input
    choice = input_and_check_num(len(choice_dictionary), 'choice')
    print(choice)

    print(f'Please choose game difficulty level:')
    y = 1
    while y <= len(difficulty_dictionary):
        print(f'{y}. {difficulty_dictionary[y]}')
        y = y + 1

    # check error input
    difficulty = input_and_check_num(len(difficulty_dictionary), 'difficulty')

    print(f'You chose to play {choice_dictionary[choice]} in {difficulty_dictionary[difficulty]} level')
    if choice == 1:
        memory_play(difficulty)
    elif choice == 2:
        play(difficulty)
    elif choice == 3:
        money_play(difficulty)


