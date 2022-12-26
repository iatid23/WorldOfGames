import requests
import json
import random
from Utils import Screen_cleaner

# This game will use the free currency api to get the current exchange rate from USD to ILS,
# will generate a new random number between 1-100
# and wiil ask the user what he thinks is the value of the generated number from USD to ILS,
# depending on the user's difficulty his answer will be correct
# if the guessed value is between the interval surrounding the correct answer
def currency_rate(number):
    url = f"https://api.apilayer.com/currency_data/convert?to=ils&from=usd&amount={number}"
    payload = {}
    headers = {"apikey": "GtUN8c7rPHjLTS6jf1iJvY83b918PKPQ"}

    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    result = response.text
    class Payload(object):
        def __init__(self, result):
            self.__dict__ = json.loads(result)

    p = Payload(result)
    #print(result)
    return p

def random_dollar():
    dollar = random.randint(1, 100)
    return int(dollar)

def get_money_interval(d, t):
    # Will get the current currency rate from USD to ILS and will generate an interval as follows:
    # a. for given difficulty d, and value of money t the interval will be: (t- (5-d), t+ (5-d))

    lower_bound = t-(5-d)
    upper_bound = t+(5-d)
    # interval  = (lower_bound, upper_bound)
    interval_after_exchange= (currency_rate(lower_bound).result, currency_rate(upper_bound).result)
    #print(interval)
    #print(interval_after_exchange)

    return interval_after_exchange

def get_guess_from_user(t):
    # A method to prompt a guess from the user to enter a guess of value to a given amount of USD
    con = True
    while con:
        money_guess = input(f"Hi,Do you Think You Can Guess how much {t} is in ILS rate ? \n")
        try:
            gss = int(money_guess)
            return money_guess
        except:
            print("Its not a number please try again")
            continue

def play(diff):
    # Will call the functions above and play the game. Will return True/False if the user lost or won.
    money = random_dollar()
    interval = get_money_interval(diff, money)

    more = True
    while more:
        # get a guess
        guess = get_guess_from_user(money)
        if int(interval[0]) <= int(guess) <= int(interval[1]):
            print(f"Wow you are A Genius good guess !!! the exect currency is {currency_rate(money).result}")
            more = False
            return True
        else:
            print("nice try - better luck next time")
            print("You are most welcome to try again")
            x = input("Please Press 'Enter' to try again or any other key to exit \n")
            if x == '':
                continue
            else:
                print("Thank you - Hope to see you soon - Bye Bye :) ")
                more = False
            return False



