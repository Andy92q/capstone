import random
import json


def pairNow(numOfStudent): #random pairs (a,b)

    people = [[False for i in range(numOfStudent)] for j in range (numOfStudent)]
    selected = [False for i in range (len(people))]
    comb = []
    for i in range (len(people)//2):
        x = random.randint(0, len(people)-1)
        y = random.randint(0, len(people)-1)     
        while (x == y or (selected[x]) or (selected[y])):
            x = random.randint(0, len(people)-1)
            y = random.randint(0, len(people)-1)
        comb.append([x,y])
        selected[x] = True
        selected[y] = True
    return comb



def record(validCombo,table): #set true for picked pairs in array (0,1)(1,0)
    for i in range (len(validCombo)):
        x = validCombo[i][0]
        y = validCombo[i][1]
        table[x][y] = True
        table[y][x] = True
    return table



def isValid(todayCombo, table): 
    for i in range (len(todayCombo)):
        r = todayCombo[i][0]
        c = todayCombo[i][1]
        if ((table[r][c] == True) or (table[c][r] == True)):
            return False
    return True
    


def inTable(size):
    table = [[False for i in range (size)] for j in range (size)]
    for i in range(len(table)):
        for j in range(len(table)):
            if i == j: table[i][j] = True
    return table    




""""
today=pairNow()
if (any pairs duplicate):
    today = pairNow()

else:
    print(today)
    record today ---> table(2D TABLE) 
    covert table to string
    overwrite
     


"""



# f = open("database.txt", "r")
# line = f.readline()

# table = json.loads(line) #2D Array
# todayComb = pairNow()

# while(isValid(todayComb, table) != True): 
#     todayComb = pairNow()
# table = record(todayComb, table)
# final = json.dumps(table)
# #print(todayComb)
# #print(table)
# #print(final)
# g = open("database.txt", "w")
# g.write(final)
# f.close()
# g.close()








