# read middle.txt covert to excel sheet
import pandas as pd
import json

# display name to row 1 and colA (reade classes2-<#>.txt)
def toExcel(classNum,placement):
    databaseNum=classNum[-1]
    f = open("./classes/class"+classNum+".txt", "r")
    stuName = [line.strip() for line in f.readlines() if line.strip()]
    f.close()
    g = open("./databases/"+placement+databaseNum+".txt", "r")    
    line = g.readline()
    table = json.loads(line)
    g.close()

    data=table
    df = pd.DataFrame(data, index=stuName, columns=stuName)
    print(df)
    excel_file = 'test.xlsx'
    df.to_excel(excel_file, index=True)

    # Display the path to the saved Excel file
    print(f"DataFrame saved to {excel_file}")
    # fill true/false from middle.txt

toExcel("2-2","middle")