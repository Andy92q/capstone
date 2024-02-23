#Read excel and display as 2D Array

import pandas as pd
import json

def readEx():
    excel_file = 'test.xlsx'
    skip_cols=[0]#Skip column A
    keep_cols = [i for i in range(9) if i not in skip_cols]
    df = pd.read_excel(excel_file, skiprows=0, usecols=keep_cols)
    finalArray = [row.tolist() for _, row in df.iterrows()]
    print(df) # table format 
    print(finalArray) # array format
    print(type(finalArray))
    return finalArray
    
#Display the updated array (optional)
readEx()

