#Read excel and display as 2D Array

import pandas as pd
import json


excel_file_path = 'test.xlsx'


skip_cols=[0]
keep_cols = [i for i in range(7) if i not in skip_cols]
df = pd.read_excel(excel_file_path, skiprows=0, usecols=keep_cols)

finalArray = [row.tolist() for _, row in df.iterrows()]

print(df) # table format 
print(finalArray) # array format
#Display the updated array (optional)