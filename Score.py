########################################################################################################################
# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:

# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he won will be added to his current amount of point saved in a file.

#Methods
# 1. add_score - The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to sav the current score.
diff = 0
file_name = "Scores.txt"

def check_file():
    try:
        file = open(file_name)
        return file
    except Exception as e:
        print("Error - the file isn't exits - system error - ", e)
        x = input('Do you want to make a new score file file? if not so please enter "No" ')
        file = open(file_name, "w+")
        return file
def add_score(difficulty, name):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    #print("this func will make new file -  Scores.txt ")
    file = check_file()
    lines = {}
    ind = 0
    len_index = len
    check = False
    for line in file:
        if ind == 0:
            ind += 1
            continue
        last = len(line.split())
        i = 0
        tmp = ''
        laststr = ''
        for u in line.split():
            if i == last-1:
                laststr = u
                break
            tmp += u + ' '
            i += 1
        (key, value) = (tmp, laststr)
        lines[key] = int(value)
        ind += 1
    file.close()


    if ind == 1:
        lines[name] = int(POINTS_OF_WINNING)
    else:
        i = 0
        for key, value in lines.items():
            if key.rstrip() == name.rstrip():
                check = True
                add = int(lines[key]) + int(POINTS_OF_WINNING)
                lines[key] = add
                break
            else:
                check = False

        if not check:
            lines[name] = POINTS_OF_WINNING
        lines = dict(sorted(lines.items(), key=lambda x: x[1], reverse=True))

    file = open(file_name, "a+")
    file.truncate(0)
    file.write('$$$$$$$$$$$$$$$$$$$ Score Board $$$$$$$$$$$$$$$$$$$\n')
    #print(f'len lines - {len(lines.items())}')
    len_index = 0
    for key, value in lines.items():

        str = f'{key} {value}'
        if len_index == len(lines.items()):
            file.write(f'{str}')
        else:
            file.write(f'{str}\n')
        len_index += 1

    file.close()
    return True

