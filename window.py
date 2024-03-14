import pairing
import ExcelFunctions
import countDown
import GUI

import tkinter as tk

def openClass(classNum): #Open class x
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
            GUI.refreshPairingLabel(pairText, winClass, pairing.producePair(classNum)),
            ExcelFunctions.MiddletoExcel(classNum,"middle"),   
            resetDatabase.config(text = countDown.readCountdownNumber(classNum))        
        ],
        height = 3,
        width = 7,
    )

    resetButton = tk.Button(
        winClass,
        text = "Reset\nMainDrive",
        command = lambda:[
            GUI.resetDatabase(classNum),
            pairText.config(text=""),
            resetDatabase.config(text=GUI.resetDatabase(classNum))],
        height = 3,
        width = 7,
    )

    #record excel to middle and database
    recordButton = tk.Button(
        winClass,
        text = "Record\nCurrent",
        command = lambda:[ExcelFunctions.ExcelToMiddle(classNum,"middle"),GUI.MiddleToDatabase(classNum)],
        height = 3,
        width = 7
    )

    newSetButton = tk.Button(
        winClass,
        text = "New Set",
        command = lambda:[GUI.resetMiddle(classNum),ExcelFunctions.MiddletoExcel(classNum,"middle")],
        height = 3,
        width = 7
    )

    openExcelButton = tk.Button(
        winClass,
        text = "Open Excel",
        command = lambda:ExcelFunctions.openExcelFile(classNum),
        height = 3,
        width = 7    
    )

    """

    saveExcelButton = tk.Button(
        winClass,
        text = "Save Excel",
        command = lambda:ExcelFunctions.ExcelToMiddle(classNum,"middle"),
        height = 3,
        width = 7
    )

    """


    
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
        text = countDown.readCountdownNumber(classNum)
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

"""
    saveExcelButton.pack()
    saveExcelButton.place(x=430, y=775)
    

"""
    





def openList(classNum): #open studentlist x
    winList = tk.Tk()
    winList.geometry("400x650")
    winList.title("class"+ classNum+"List")

    line = GUI.readStudentName(classNum)
    #myfont=tkinter.font.Font(family="Comic Sans MS", size=666)
    textArea=tk.Text(
        winList,
        height=40, 
        width=20,  
        bg = "skyblue",
        bd = 2,
        relief=tk.SOLID,

        #font = myfont
    )

    saveButton = tk.Button(
        winList,
        text = "save",
        command = lambda:GUI.saveStudentList("./classes/class"+classNum+".txt", textArea),
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
