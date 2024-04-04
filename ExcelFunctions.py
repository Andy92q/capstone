import pandas as pd
import os
import platform
import json
import GUI
import os

current_dir = os.path.dirname(__file__)

def readExcel(classNum):  # readEx
    """This function reads the excel spreadsheet True/False section

    Args:
        classNum (str): eg. "1"

    Returns:
        boolean[][]: true/false
    """

    numPeople = len(GUI.readStudentName(classNum))
    excel_file = current_dir+"/excel/" + classNum + ".xlsx"
    skip_cols = [0]  # Skip column A
    keep_cols = [i for i in range(numPeople + 1) if i not in skip_cols]
    df = pd.read_excel(excel_file, skiprows=0, usecols=keep_cols)
    finalArray = [row.tolist() for _, row in df.iterrows()]
    return finalArray


def openExcelFile(classNum):
    """This function opens the excel file from python

    Args:
        classNum (str): eg. "1"

    Returns:
        excel opened
    """
    # Specify the path to your Excel file
    excel_file = current_dir+"/excel/" + classNum + ".xlsx"
    # Use pandas to read the Excel file
    dp = pd.read_excel(excel_file)
    # Display the DataFrame (optional)
    print(dp)

    # Open the Excel file in the default application
    system_name = platform.system().lower()

    if system_name == "darwin":  # macOS
        os.system(f'open "{excel_file}"')
    elif system_name == "linux":  # Linux
        # Try xdg-open first, then gnome-open
        os.system(f'xdg-open "{excel_file}"') or os.system(f'gnome-open "{excel_file}"')
    elif system_name == "windows":
        # On Windows, the original start command should work
        os.system(f'start excel "{excel_file}"')
    else:
        print(f"Unsupported operating system: {system_name}")


def MiddletoExcel(classNum, placement):  # toExcel
    """This function overwrites middle<classNum>.txt file and student names to excel to create a table

    Args:
        classNum (str): eg. "1"
        placement (str): eg. "database", "middle"

    Returns:
        excel spreadsheet is filled with studnet names and true/false data
        display name to row 1 and colA (reade classes2-<#>.txt)
    """

    f = open(current_dir+"/classes/class" + classNum + ".txt", "r")
    stuName = [line.strip() for line in f.readlines() if line.strip()]
    f.close()
    g = open(current_dir+"/databases/" + placement + classNum + ".txt", "r")
    line = g.readline()
    table = json.loads(line)
    print(table)
    g.close()

    data = table
    df = pd.DataFrame(data, index=stuName, columns=stuName)
    print(df)
    excel_file = current_dir+"/excel/" + classNum + ".xlsx"
    df.to_excel(excel_file, index=True)

    # Display the path to the saved Excel file
    print(f"DataFrame saved to {excel_file}")
    # fill true/false from middle.txt


def ExcelToMiddle(classNum, placement):
    """This function overwrites the middle.txt file with the updated array

    Args:
        classNum (str): eg. "1"
        placement (str): eg. "database", "middle"

    Returns:
        middle<classNum>.txt have new data from excel
    """

    modified_array = readExcel(classNum)
    with open(current_dir+"/databases/" + placement + classNum + ".txt", "w") as f:
        json.dump(modified_array, f)
