########################################################################################################################
# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:

# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he won will be added to his current amount of point saved in a file.

#Methods
# 1. add_score - The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to sav the current score.
diff = 0;


def add_score(difficulty, name):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    print("this func will make new file -  Scores.txt ")
    #print("The file will be cleared and filled by my the name of the creator as input")
    file = open("Scores.txt")
    lines = {}
    ind = 0

    #print(name)
    check = False
    for line in file:
        print(line)
        if ind == 0:
            ind += 1
            continue
        (key, value) = line.split()
        lines[key] = int(value)
        ind += 1
    file.close()
    #print(ind)
    if ind == 1:
        print(ind)
        lines[name] = int(POINTS_OF_WINNING)
    else:
        print(lines)

        for key, value in lines.items():
            print('key #### - ', key)
            if key == name:
                print(f'key == name = {key} lines[key] = {lines[key]} POINTS OF WINING = {POINTS_OF_WINNING}')
                check = True
                add = int(lines[key]) + int(POINTS_OF_WINNING)
                print('add' ,add)
                print(lines[key])
                lines[key] = add
                print(lines[key])
                break
            else:
                check = False
                #print('false')

        if not check:
            lines[name] = POINTS_OF_WINNING

        lines = dict(sorted(lines.items(), key=lambda x: x[1], reverse=True))
        print(lines)

    file = open("Scores.txt", "a+")
    file.truncate(0)
    file.write('$$$$$$$$$$$$$$$$$$$ Score Board $$$$$$$$$$$$$$$$$$$\n')
    for key, value in lines.items():

        str = f'{key} {value}'
        print(f'lines items - key == name = {key} value = {value} str = {str}')
        file.write(f'{str}\n')




    # for index, line in enumerate(lines):
    #     if name in line:
    #         print('string found in file')
    #         print('line number: ', index)
    #         score += int(line.split()[1])
    #         print('score: ', score)
    #         print(score)
    #         lines[0] = f'{name} {score + 123}'
    #         file2 = open("Scores.txt", 'w+', encoding='utf-8')
    #         file2.writelines(lines)
    #     else:
    #         print(lines)
    #         file2 = open("Scores.txt", 'a+', encoding='utf-8')
    #         str = f'{name} {5}'
    #         print('lines : ', lines)
    #         print('here len :', len(lines))
    #         lines.append(str)
    #         file2.write('\n')
    #         file2.write(str)
    #
    # if len(lines) == 0:
    #     print(lines)
    #     file2 = open("Scores.txt", 'w+', encoding='utf-8')
    #     str = f'{name} {5}'
    #     lines = str
    #     print(lines)
    #     print('here')
    #     file2.writelines(lines)
    #     # clear file
    #     # file.truncate(0)
    #
    #
    #
    #     # while row in file.readlines():
    #     #     row.line.strip()
    #     #     a = line.split(' ')[0]
    #     #     b = line.split(' ')[1]
    #     #     print(f'a - {a} // b- {b}')
    #
    #     # print(row)
    #     #
    #     # try:
    #     #     file.write(f'{name}  {} \n  ')
    #     # except BaseException as e:
    #     #     print(f"There is an exception in writing file - {e}")
    #     file2.close()
    file.close()


