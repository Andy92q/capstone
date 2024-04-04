import json
import pairing
import tkinter as tk


def getTable(classNum, placement):
    """This function reads 2D array in databases/<classNum>.txt

    Args:
        classNum (str) : eg. "1"
        placement (str) : eg. "database"

    Returns:
        boolean[][] : 2d array
    """

    f = open("./databases/" + placement + classNum + ".txt", "r")
    line = f.readline()
    table = json.loads(line)
    f.close()
    return table


def readStudentName(classNum):  # readName
    """This function reads array in class<classNum>.txt

    Args:
        classNum (str): eg. "1"

    Returns:
        string []: 1d array

    """
    f = open("./classes/class" + classNum + ".txt", "r")
    name = [line.strip() + "\n" for line in f.readlines() if line.strip()]
    return name


def refreshPairingLabel(label, window, newText):  # refresh
    """This funciton refreshes the label

    Args:
        label (tk.Label):
        window (tk.Tk()):
        newText (String):
    """

    label.config(text=newText)
    window.update_idletasks()


def resetMiddle(classNum):  # newSet
    """This function resets the 2D array in database

    Args:
        classNum (str): eg. "1"

    Returns:
        overwrite a new (empty, without anyone being paired) 2D array
    """
    numPeople = len(readStudentName(classNum))
    ini = pairing.initializeTable(numPeople)
    f = open("./databases/middle" + classNum + ".txt", "w")
    f.write(json.dumps(ini))
    f.close()


def saveStudentList(fileName, theWidget):  # saveFile
    """This function saves the studentList from app to class<classNum>.txt

    Args:
        fileName (str): eg. class<classNum>.txt
        theWidget (tk.Text):

    Returns:
        saves text from theWidget to class<classNum>.txt
    """
    content = theWidget.get("1.0", tk.END)  # from (0,0) --> (line 10000,char10000)
    name = [line.strip() + "\n" for line in content.splitlines() if line.strip()]
    content = "".join(name)
    f = open(fileName, "w")
    f.write(content)


def resetDatabase(classNum):  # reset
    """This functions initializes the database and returns the initial number of turns left until automatic reset

    Args:
        classNum (str): eg. "1"

    Returns:
        int: how many turns can be perfectly executed

    """

    size = len(readStudentName(classNum))
    ini = pairing.initializeTable(size)
    f = open("./databases/database" + classNum + ".txt", "w")
    f.write(json.dumps(ini))
    f.close()

    with open("./databases/refreshCount.json", "r") as f:
        data = json.load(f)
        data[classNum] = size - 1
    with open("./databases/refreshCount.json", "w") as g:
        json.dump(data, g)
    return data[classNum]


def MiddleToDatabase(classNum):  # RecordFinalPair
    """This function records the new pairs stored in middle to database

    Args:
        classNum (str): eg. "1"

    Returns:
        add new pairings as True values to database
    """

    middleTable = getTable(classNum, "middle")
    databaseTable = getTable(classNum, "database")
    for i in range(len(middleTable)):
        for j in range(len(middleTable)):
            if middleTable[i][j] == True and databaseTable[i][j] == False:
                databaseTable[i][j] = middleTable[i][j]
            elif (
                middleTable[i][j] == True and databaseTable[i][j] == True
            ):  # change: if already paired before
                databaseTable[i][j] = middleTable[i][j]

    f = open("./databases/database" + classNum + ".txt", "w")
    f.write(json.dumps(databaseTable))
    f.close()
