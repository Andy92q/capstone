import tkinter as tk
import json
import pandas as pd

#extra classes
import pairing
import initial
import openEx



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

def newSet(classNum): #reset database    
    numPeople = len(readName(classNum))
    ini = initial.inTable(numPeople)
    f = open("./databases/middle"+classNum[-1]+".txt", "w")
    f.write(json.dumps(ini))
    f.close()






def producePair(classNum): #random pair
    nameList = readName(classNum)
    out = ""
    numPeople = len(nameList)
    comb = pairing.pairNow(numPeople) # comb = [[4,1],[7,10]....]

    changeCount(classNum)
    while(pairing.isValid(comb,getTable(classNum,"database")) == False or pairing.isValid(comb,getTable(classNum,"middle")) == False):
        comb = pairing.pairNow(numPeople)
        print("try again")  
    for i in range (len(comb)):
        k = nameList[comb[i][0]].strip()+"-"+nameList[comb[i][1]].strip() #remove extra lines
        out+=k+"\n"

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

    with open("./databases/refreshCount.json",'r') as f:
        data=json.load(f)
        data[databaseNum] = size-1
    with open("./databases/refreshCount.json",'w') as g:  
        json.dump(data,g)
    return data[databaseNum]

def recordFinalPair(classNum): #Record middle to database without repeat
    databaseNum = classNum[-1]
    middleTable = getTable(classNum, "middle")
    databaseTable = getTable(classNum, "database")
    for i in range(len(middleTable)):
        for j in range(len(middleTable)):
            if (middleTable[i][j] == True and databaseTable[i][j] == False):     
                databaseTable[i][j] = middleTable[i][j]
            elif(middleTable[i][j] == True and databaseTable[i][j] == True): #change: if already paired before
                databaseTable[i][j] = middleTable[i][j]

    f = open("./databases/database"+databaseNum+".txt", "w")
    f.write(json.dumps(databaseTable))
    f.close()
  
    

def readCount(classNum): #read how many turns until refresh
    databaseNum = classNum[-1]
    with open("./databases/refreshCount.json",'r') as f:
        data=json.load(f)
    return data[databaseNum]

def changeCount(classNum): #countdown the turns
    databaseNum = classNum[-1]
    
    if checkAllPaired(classNum) == True or readCount(classNum) == 0:
        reset(classNum)
        newSet(classNum)
        num = reset(classNum)-1
    else:
        num = readCount(classNum)-1

    with open("./databases/refreshCount.json",'r') as f:
        data=json.load(f)
        data[databaseNum] = num
    with open("./databases/refreshCount.json",'w') as g:  
        json.dump(data,g)
    
    return num
    
    
def checkAllPaired(classNum): #check if certain person has been paired for everyone
    numPeople = len(readName(classNum))
    count = 0
    for i in range (numPeople):
        for j in range (numPeople):
            if (getTable(classNum,"database")[i][j] == True or getTable(classNum,"middle")[i][j] == True):
                count+=1
        if count == numPeople: return True
        count = 0  
    return False


#Excel Functions
def readEx(classNum):
    numPeople = len(readName(classNum))
    excel_file = "./excel/"+classNum+".xlsx"
    skip_cols=[0]#Skip column A
    keep_cols = [i for i in range(numPeople+1) if i not in skip_cols]
    df = pd.read_excel(excel_file, skiprows=0, usecols=keep_cols)
    finalArray = [row.tolist() for _, row in df.iterrows()]
    return finalArray

# display name to row 1 and colA (reade classes2-<#>.txt)
def toExcel(classNum,placement): #跟middle相关的button连接
    databaseNum=classNum[-1]
    f = open("./classes/class"+classNum+".txt", "r")
    stuName = [line.strip() for line in f.readlines() if line.strip()]
    f.close()
    g = open("./databases/"+placement+databaseNum+".txt", "r")    
    line = g.readline()
    table = json.loads(line)
    print(table)
    g.close()

    data=table
    df = pd.DataFrame(data, index=stuName, columns=stuName)
    print(df)
    excel_file = "./excel/"+classNum+".xlsx"
    df.to_excel(excel_file, index=True)

    # Display the path to the saved Excel file
    print(f"DataFrame saved to {excel_file}")
    # fill true/false from middle.txt


def ExcelToMiddle(classNum,placement):
    databaseNum=classNum[-1]
    modified_array=readEx(classNum)
    # Overwrite the middle.txt file with the updated array
    with open("./databases/"+placement+databaseNum+".txt", "w") as f:
        json.dump(modified_array, f)




#Window Functions
def openClass(classNum): #Open class 2-x
    winClass = tk.Tk()
    winClass.geometry("600x850")
    winClass.title("class"+ classNum)

    
    openListButton = tk.Button(
        winClass,
        text = "classList",
        command = lambda:openList(classNum),
        height = 3,
        width = 7
        )
    
    pairButton = tk.Button(
        winClass,
        text = "New Pair",
        command =lambda:[
            refresh(pairText, winClass, producePair(classNum)),
            toExcel(classNum,"middle"),   
            resetDatabase.config(text = readCount(classNum))        
        ],
        height = 3,
        width = 7,
    )

    resetButton = tk.Button(
        winClass,
        text = "Reset\nMainDrive",
        command = lambda:[
            reset(classNum),
            pairText.config(text=""),
            resetDatabase.config(text=reset(classNum))],
        height = 3,
        width = 7,
    )

    #record excel to middle and database
    recordButton = tk.Button(
        winClass,
        text = "Record\nCurrent",
        command = lambda:[ExcelToMiddle(classNum,"middle"),recordFinalPair(classNum)],
        height = 3,
        width = 7
    )

    newSetButton = tk.Button(
        winClass,
        text = "New Set",
        command = lambda:[newSet(classNum),toExcel(classNum,"middle")],
        height = 3,
        width = 7
    )

    openExcelButton = tk.Button(
        winClass,
        text = "Open Excel",
        command = lambda:openEx.openExcelFile(classNum),
        height = 3,
        width = 7    
    )

    saveExcelButton = tk.Button(
        winClass,
        text = "Save Excel",
        command = lambda:ExcelToMiddle(classNum,"middle"),
        height = 3,
        width = 7

    )
    pairText = tk.Label(
        winClass,
        height = 37,
        width = 50,
        relief = tk.SOLID,
    )
    
    resetDatabase = tk.Label(
        winClass,
        height = 3,
        width = 10,   
        relief = tk.SOLID,    
        text = readCount(classNum)
    )


    openListButton.pack()
    openListButton.place(x=100,y=10)
     
    pairText.pack()
    pairText.place(x=72,y=80)

    pairButton.pack()
    pairButton.place(x=250,y=700)

    recordButton.pack()
    recordButton.place(x=430,y=700)

    newSetButton.pack()
    newSetButton.place(x=70,y=700)

    resetButton.pack()
    resetButton.place(x=70,y=775)

    resetDatabase.pack()
    resetDatabase.place(x=400,y=13)

    openExcelButton.pack()
    openExcelButton.place(x=250, y=775)

    saveExcelButton.pack()
    saveExcelButton.place(x=430, y=775)
    





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