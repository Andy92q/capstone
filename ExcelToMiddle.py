import json
import pandas as pd
import readExcel


def ExcelToMiddle():
    modified_array=readExcel.readEx()
    # Overwrite the middle.txt file with the updated array
    with open("middle.txt", "w") as f:
        json.dump(modified_array, f)

ExcelToMiddle()






