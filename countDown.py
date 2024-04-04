import json
import GUI
import os

current_dir = os.path.dirname(__file__)


def readCountdownNumber(classNum):  # readCount
    """This function reads how many turns of pairing are avaliable until automatic refresh

    Args:
        classNum (str): eg. "1"

    Returns:
        int: how many turns remain to be executed theoretically
    """

    with open(current_dir + "/databases/refreshCount.json", "r") as f:
        data = json.load(f)
    return data[classNum]


def changeCountdownNumber(classNum):  # changeCount
    """This function checks for how many turns can be done after current pair

    Args:
        classNum (str): eg. "1"

    Returns:
        int: how many turns remain to be executed theoretically
    """
    if checkAllPaired(classNum) == True or readCountdownNumber(classNum) == 0:
        GUI.resetDatabase(classNum)
        GUI.resetMiddle(classNum)
        num = GUI.resetDatabase(classNum) - 1
    else:
        num = readCountdownNumber(classNum) - 1

    with open(current_dir + "/databases/refreshCount.json", "r") as f:
        data = json.load(f)
        data[classNum] = num
    with open(current_dir + "/databases/refreshCount.json", "w") as g:
        json.dump(data, g)

    return num


def checkAllPaired(classNum):  # check if certain person has been paired for everyone
    """This function checks if certain person has been paired for everyone

    Args:
        classNum (str): eg. "1"

    Returns:
        boolean: True/False
    """
    numPeople = len(GUI.readStudentName(classNum))
    count = 0
    for i in range(numPeople):
        for j in range(numPeople):
            if (
                GUI.getTable(classNum, "database")[i][j] == True
                or GUI.getTable(classNum, "middle")[i][j] == True
            ):
                count += 1
        if count == numPeople:
            return True
        count = 0
    return False
