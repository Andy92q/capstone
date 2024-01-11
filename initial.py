import json
def inTable(size):
    table = [[False for i in range (size)] for j in range (size)]
    for i in range(len(table)):
        for j in range(len(table)):
            if i == j: table[i][j] = True
    return table    

f = open("database.txt", "w")
f.write(json.dumps(inTable(6)))
f.close()
g = open("middle.txt", "w")
g.write(json.dumps(inTable(6)))
g.close()