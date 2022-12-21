
# This game will use the free currency api to get the current exchange rate from USD to ILS,
# will generate a new random number between 1-100
# and wiil ask the user what he thinks is the value of the generated number from USD to ILS,
# depending on the user's difficulty his answer will be correct
# if the guessed value is between the interval surrounding the correct answer

def get_money_interval():
    # Will get the current currency rate from USD to ILS and will generate an interval as follows:
    # a. for given difficulty d, and value of money t the interval will be: (t- (5-d), t+ (5-d))
    return 0

def get_guess_from_user():
    # A method to prompt a guess from the user to enter a guess of value to a given amount of USD
    return 0

def paly():
    # Will call the functions above and play the game. Will return True/False if the user lost or won.
    return 0
