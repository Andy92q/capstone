import random
import json
import GUI
import countDown


def initializeTable(size):
    """This function initialize the 2D array to false

    Args:
        size (int): eg. 30

    Returns:
        boolean[][]: True/False
    """
    table = [[False for i in range(size)] for j in range(size)]
    for i in range(len(table)):
        for j in range(len(table)):
            if i == j:
                table[i][j] = True
    return table


def producePair(classNum):  # random pair
    """This function creates random pairs of people that haven't been previously paired

    Args:
        classNum (str): eg. "1"

    Returns:
        String: paired names in string

    1. Create new pair
    2. if pairing did not satisfy, try again
    3. record the array of satisfied combos to middle.txt
    4. return the string of paired names
    """
    nameList = GUI.readStudentName(classNum)
    out = ""
    numPeople = len(nameList)
    comb = pairNow(numPeople)  # comb = [[4,1],[7,10]....]

    countDown.changeCountdownNumber(classNum)  # countdown -1
    while (
        isValid(comb, GUI.getTable(classNum, "database")) == False
        or isValid(comb, GUI.getTable(classNum, "middle")) == False
    ):
        comb = pairNow(numPeople)
        print("try again")
    for i in range(len(comb)):
        k = (
            nameList[comb[i][0]].strip() + "-" + nameList[comb[i][1]].strip()
        )  # remove extra lines
        out += k + "\n"

    recordValidCombo(classNum, comb, "middle")

    return out


def checkValid(classNum, combo):
    """This function checks if current combo has any repetition from previous pairs

    Args:
        classNum (str): eg. "1"
        combo (2D array): eg. [[4,1],[7,10]....]

    Returns:
        boolean: true/false
    """

    size = len(GUI.readStudentName(classNum))
    print(size)
    if isValid(combo, initializeTable(size)) == True:
        return True
    return False


def recordValidCombo(classNum, validCombo, placement):
    """This function records combo into database<classNum>.txt or middle<classNum>.txt

    Args:
        classNum (str): eg. "1"
        validCombo (2D array): eg. [[4,1],[7,10]....]
        placement (str): eg. "database", "middle"

    Returns:
        add new pairings as True values
    """

    f = open("./databases/" + placement + classNum + ".txt", "r")
    line = f.readline()
    arrBegin = json.loads(line)
    todayRecord = record(validCombo, arrBegin)
    arrEnd = json.dumps(todayRecord)
    g = open("./databases/" + placement + classNum + ".txt", "w")
    g.write(arrEnd)
    f.close()
    g.close()


def pairNow(numOfStudent):  # random pairs (a,b)
    people = [[False for i in range(numOfStudent)] for j in range(numOfStudent)]
    selected = [False for i in range(len(people))]
    comb = []
    for i in range(len(people) // 2):
        x = random.randint(0, len(people) - 1)
        y = random.randint(0, len(people) - 1)
        while x == y or (selected[x]) or (selected[y]):
            x = random.randint(0, len(people) - 1)
            y = random.randint(0, len(people) - 1)
        comb.append([x, y])
        selected[x] = True
        selected[y] = True
    return comb


def record(validCombo, table):  # set true for picked pairs in array (0,1)(1,0)
    for i in range(len(validCombo)):
        x = validCombo[i][0]
        y = validCombo[i][1]
        table[x][y] = True
        table[y][x] = True
    return table


def isValid(todayCombo, table):
    for i in range(len(todayCombo)):
        r = todayCombo[i][0]
        c = todayCombo[i][1]
        if (table[r][c] == True) or (table[c][r] == True):
            return False
    return True
