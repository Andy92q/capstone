import tkinter as tk
import pairing
import initial
import json

win = tk.Tk()
win.configure(bg = "white")
win.title("Classes")
win.geometry("800x800")

def getTable(classNum, placement):
    databaseNum = classNum[-1]
    f = open("./databases/"+placement+databaseNum+".txt", "r")
    line = f.readline()
    table = json.loads(line)
    f.close()
    return table

def readName(classNum):
    f = open("./classes/class"+classNum+".txt", "r")
    name = [line.strip()+"\n" for line in f.readlines() if line.strip()]
    return name

def refresh(label,window,newText):
    label.config(text=newText)
    window.update_idletasks()

def newSet(classNum):
    numPeople = len(readName(classNum))
    ini = initial.inTable(numPeople)
    f = open("./databases/middle"+classNum[-1]+".txt", "w")
    f.write(json.dumps(ini))
    f.close()

#问题：当使用pairing的次数到达一定数量会开始有重复的pair
#解决思路：需要一个function告诉你再pair的话会有重复
#解决方式：睡觉 梦里啥都有
def producePair(classNum): #random pair
    nameList = readName(classNum)
    out = ""
    numPeople = len(nameList)

    comb = pairing.pairNow(numPeople) # comb = [[4,1],[7,10]....]
    while(pairing.isValid(comb,getTable(classNum,"database")) == False or pairing.isValid(comb,getTable(classNum,"middle")) == False):
        comb = pairing.pairNow(numPeople)
        print("try again")
    for i in range (len(comb)):
        out += nameList[comb[i][0]]+"-"+nameList[comb[i][1]]+"\n"
    
    recordValidCombo(classNum,comb,"middle")

    return out

def checkValid(classNum, combo):
    size = len(readName(classNum))
    print(size)
    if pairing.isValid(combo,pairing.inTable(size)) == True:
        return True
    return False

#placement = middle,database
def recordValidCombo(classNum, validCombo,placement):
    databaseNum = classNum[-1]
    f = open("./databases/"+placement+databaseNum+".txt", "r")
    line = f.readline()
    arrBegin = json.loads(line)
    todayRecord = pairing.record(validCombo,arrBegin)
    arrEnd = json.dumps(todayRecord)
    g = open("./databases/"+placement+databaseNum+".txt", "w")
    g.write(arrEnd)
    f.close()
    g.close()

# def confirm(classNum, validCombo):
    # recordValidCombo(classNum,validCombo)

def saveFile(fileName,theWidget):
    content = theWidget.get("1.0",tk.END) # from (0,0) --> (line 10000,char10000)
    name = [line.strip()+"\n" for line in content.splitlines() if line.strip()]
    content = ''.join(name)
    f = open(fileName, "w")
    f.write(content)

def reset(classNum):
    size = len(readName(classNum))
    databaseNum = classNum[-1]
    ini = initial.inTable(size)
    f = open("./databases/database"+databaseNum+".txt", "w")
    f.write(json.dumps(ini))
    f.close()

def recordFinalPair(classNum): #Record middle to database without repeat
    databaseNum = classNum[-1]
    middleTable = getTable(classNum, "middle")
    databaseTable = getTable(classNum, "database")
    k=0
    for i in range(len(middleTable)):
        for j in range(len(middleTable)):
            if (middleTable[i][j] == True and databaseTable[i][j] == False):     
                databaseTable[i][j] = middleTable[i][j]

    f = open("./databases/database"+databaseNum+".txt", "w")
    f.write(json.dumps(databaseTable))
    f.close()
    
    # databaseNum = classNum[-1]
    # f = open("./databases/"+"middle"+databaseNum+".txt", "r")
    # g = open("./databases/"+"database"+databaseNum+".txt", "r")
    # firstLine = f.readline()
    # finalLine = g.readline()
    # arrBegin = json.loads(firstLine)
    # arrFinal = json.loads(finalLine)
    # for i in range (len(arrBegin)):
    #     for j in range (len(arrBegin)):
    #         if (arrBegin[i][j] == True): 
    #             arrFinal[i][j] == True
    # f.close()
    # g.close()
    # h = open("./databases/"+"database"+databaseNum+".txt", "w")
    # h.write(json.dumps(arrFinal))
    # h.close()

    
              





def openClass(classNum): #Open class 2-x
    winClass = tk.Tk()
    winClass.geometry("600x850")
    winClass.title("class"+ classNum)

    
    openListButton = tk.Button(
        winClass,
        text = "classList",
        command = lambda:openList(classNum)
        )
    
    refreshButton = tk.Button(
        winClass,
        text = "New Pair",
        command =lambda:refresh(pairText, winClass, producePair(classNum))
    )

    resetButton = tk.Button(
        winClass,
        text = "reset database",
        command = lambda:[reset(classNum),pairText.config(text="")],
        height = 2,
        width = 3,
    )

    recordButton = tk.Button(
        winClass,
        text = "record today",
        command = lambda:recordFinalPair(classNum),
        height = 2,
        width = 3
    )

    newSetButton = tk.Button(
        winClass,
        text = "new set",
        command = lambda:newSet(classNum),
        height = 2,
        width = 3
    )

    # confirmButton = tk.Button(
    #     winClass,
    #     text = "confirm",
    #     command = lambda:confirm(classNum),
    #     height = 2,
    #     width = 3,
    # )

    pairText = tk.Label(
        winClass,
        height = 40,
        width = 30,
        relief = tk.SOLID,
        #text = producePair(classNum)
    )
    

    openListButton.pack()
    pairText.pack()
    refreshButton.pack()
    resetButton.pack()
    recordButton.pack()
    newSetButton.pack()
    # confirmButton.pack()

def openList(classNum): #open studentlist 2-x
    winList = tk.Tk()
    winList.geometry("400x650")
    winList.title("class"+ classNum+"List")

    line = readName(classNum)
    #myfont=tkinter.font.Font(family="Comic Sans MS", size=666)
    textArea=tk.Text(
        winList,
        height=40, #40彳亍
        width=20,  #20字
        bg = "skyblue",
        bd = 2,
        relief=tk.SOLID,

        #font = myfont
    )

    saveButton = tk.Button(
        winList,
        text = "save",
        command = lambda:saveFile("./classes/class"+classNum+".txt", textArea),
        height = 2,
        width = 3
    )
    cancelButton = tk.Button(
        winList,
        text = "cancel",
        command = lambda:winList.destroy(),
        height = 2,
        width = 3
    )
    
    for i in range (len(line)):
        textArea.insert(tk.END, line[i])
    
    
    
    textArea.pack()
    saveButton.pack()
    cancelButton.pack()





b1 = tk.Button(
    text = "1",
    command = lambda:openClass("2-1")
)
b2 = tk.Button(
    text = "2",
    command = lambda:openClass("2-2")
)
b3 = tk.Button(
    text = "3",
    command = lambda:openClass("2-3")
)
b4 = tk.Button(
    text = "4",
    command = lambda:openClass("2-4")
)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b1.place(x=200, y=200)
b2.place(x=600, y=200)
b3.place(x=200, y=600)
b4.place(x=600, y=600)












win.mainloop()