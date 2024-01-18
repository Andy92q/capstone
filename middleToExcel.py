# read middle.txt covert to excel sheet
import pandas as pd
import json

# display name to row 1 and colA (reade classes2-<#>.txt)
f = open("./classes/class2-1.txt", "r")
stuName = [line.strip() for line in f.readlines() if line.strip()]

g = open("./databases/middle1.txt", "r")    
line = g.readline()
table = json.loads(line)
g.close()


data=table
df = pd.DataFrame(data, index=stuName, columns=stuName)
print(df)
# fill true/false from middle.txt