import json
import pairing
import initial
import random
import pandas as pd
import os
import platform

# f = open("database.txt", "r")
# line = f.readline()
# arr = json.loads(line)

# print(arr)
# def pairNow(numOfStudent): #random pairs (a,b)
#     people = [[False for i in range(numOfStudent)] for j in range (numOfStudent)]
#     selected = [False for i in range (len(people))]
#     comb = []
#     for i in range (len(people)//2):
#         x = random.randint(0, len(people)-1)
#         y = random.randint(0, len(people)-1)     
#         while (x == y or (selected[x]) or (selected[y])):
#             x = random.randint(0, len(people)-1)
#             y = random.randint(0, len(people)-1)
#         comb.append([x,y])
#         selected[x] = True
#         selected[y] = True
#     return comb

# def isValid(todayCombo, table): 
#     for i in range (len(todayCombo)):
#         r = todayCombo[i][0]
#         c = todayCombo[i][1]
#         if ((table[r][c] == True) or (table[c][r] == True)):
#             return False
#     return True


# table = [[True, True, False, False, True, True], [True, True, True, True, False, False], [False, True, True, False, True, True], [False, True, False, True, True, True], [True, False, True, True, True, False], [True, False, True, True, False, True]]
# print(table)
# pair = pairing.pairNow(6)

# # while (isValid(pair,table) == False):
# #     pair = pairing.pairNow(6)
# # print(pair)
# # print(isValid(pair, table))
# # pairing.record(pair,table)
# # print(table)


# num = ["hello"+"\n" for i in range (10)]
# # str ---> list (split by \n)
# message = "hello i am jayme\n i am not andy \n i am not johnson"
# messageList = message.splitlines()
# print(messageList)

# def recordFinalPair(classNum,validCombo,placement):
#     databaseNum = classNum[-1]
#     f = open("./databases/"+placement+databaseNum+".txt", "r")
#     line = f.readline()
#     arrBegin = json.loads(line)
#     print(arrBegin)
    


# # f = open("./databases/"+"database1"+".txt", "r")
# # line = f.readline()
# # arrBegin = json.loads(line)
# # print(type(arrBegin))


# to excel
# f = open("middle.txt", "r")
# line = f.readline()
# table = json.loads(line)
# f.close()
# array = table
# print(table)
# df = pd.DataFrame(array).T
# df.to_excel(excel_writer = "test.xlsx")

# Specify the path to your Excel file
excel_file_path = 'test.xlsx'

# Use pandas to read the Excel file
dp = pd.read_excel(excel_file_path)

# Display the DataFrame (optional)
print(dp)

# Open the Excel file in the default application
system_name = platform.system().lower()

if system_name == 'darwin':  # macOS
    os.system(f'open "{excel_file_path}"')
elif system_name == 'linux':  # Linux
    # Try xdg-open first, then gnome-open
    os.system(f'xdg-open "{excel_file_path}"') or os.system(f'gnome-open "{excel_file_path}"')
elif system_name == 'windows':
    # On Windows, the original start command should work
    os.system(f'start excel "{excel_file_path}"')
else:
    print(f"Unsupported operating system: {system_name}")