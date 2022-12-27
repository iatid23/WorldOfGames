from GuessGame import play as guess_play
from MemoryGame import play as memory_play
from CurrencyRouletteGame import play as money_play
from Utils import Screen_cleaner
from time import sleep
from Score import add_score

choice_dictionary_content = {1: 'a sequence of numbers will appear for 1 second and you have to  guess it back',
                             2: 'guess a number and see if you chose like the computer',
                             3: 'Currency Roulette - try and guess the value of a random amount of USD in ILS'}
choice_dictionary = {1: 'Memory Game', 2: 'Guess Game', 3: 'Currency Roulette'}
difficulty_dictionary = {1: 'Super Easy', 2: 'Easy', 3: 'Medium', 4: 'Hard', 5: 'Extreme'}

def input_and_check_num(num, str):
    while True:
        try:
            choice = input(f'Enter Your {str} : \n')
            c = int(choice)
        except ValueError:
            print("You didn't enter a number please choose again")
            sleep(0.1)
            continue
        if 1 <= c <= num:
            sleep(0.1)
            return c
        else:
            print(f"You didn't enter a number between 1 or {num}, please enter again")
            sleep(0.1)
            continue
        sleep(0.1)

def input_and_check_hello():
    while True:
        name = input(f'Please Enter Your name : \n')
        typ = type(name)
        if typ != str:
            print("You didn't entered string name, please enter your name again")
            sleep(0.1)
        try:
            int(name)
            print("You entered a number not your name, please enter your name again")
            sleep(0.1)
            continue
        except ValueError:
            if name == '' or name == ' ':
                print("You didn't enter chars please enter your name again")
                sleep(0.1)
                continue
            else:
                sleep(0.1)
                return name
        sleep(0.1)



def welcome(name):
    ret_str = f''' Hello {name} and welcome to the world of games
Here you can find many cool games to play
__________________________________________________'''
    sleep(2)
    Screen_cleaner()


    return ret_str


def load_game():
    index_of_play = 0
    if index_of_play == 1:
        x = input('Please enter "exit" if you wish to end the game')
        if x == 'exit' or x == 'Exit' or x == 'EXIT':
            index_of_play = 0
            exit(0)
    Screen_cleaner()
    name = input_and_check_hello()
    print(welcome(name))

    boo = True
    while boo:
        global choice_dictionary, difficulty_dictionary, choice_dictionary_content
        y = 1
        print(f'Please choose a game to play:')
        while y <= len(choice_dictionary) :
            print(f'{y}. {choice_dictionary[y]} - {choice_dictionary_content[y]}')
            y = y + 1
        # check error input
        choice = input_and_check_num(len(choice_dictionary), 'choice')

        sleep(1)
        Screen_cleaner()
        sleep(0.1)

        print(f'Please choose game difficulty level:')
        y = 1
        while y <= len(difficulty_dictionary):
            print(f'{y}. {difficulty_dictionary[y]}')
            y = y + 1

        # check error input
        difficulty = input_and_check_num(len(difficulty_dictionary), 'difficulty')
        diff = int(difficulty)

        print(f'You chose to play {choice_dictionary[choice]} in {difficulty_dictionary[difficulty]} level')
        sleep(3)
        Screen_cleaner()
        sleep(0.1)

        if choice == 1:
            if memory_play(diff):
                add_score(diff, name)
        elif choice == 2:
            if guess_play(diff):
                add_score(diff, name)
        elif choice == 3:
            if money_play(diff):
                add_score(diff, name)
        inpboo = 2
        sleep(0.1)
        while inpboo > 1:
            inp = input('do you want to play again Enter Yes to play again or No to exit \n')
            if inp == 'Yes' or inp == 'yes' or inp == 'YES':
                Screen_cleaner()
                inpboo = 0
            elif inp == 'NO' or inp == 'No' or inp == 'no':
                print ('Thank you for playing :) Have a nice day !!!')
                sleep(3)
                Screen_cleaner()
                inpboo = 1
            else:
                print('Please enter Only "Yes" Or "No"')
                inpboo = 2
            sleep(0.1)
        if inpboo == 0:
            boo == True
        else:
            boo = False
            index_of_play = 1
            load_game()
            # exit(0)


