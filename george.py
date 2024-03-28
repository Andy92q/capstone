import pairing
import ExcelFunctions
import countDown
import GUI

import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def openClass(classNum): #Open class x
    
    winClass = Toplevel()
    winClass.geometry("600x850")
    winClass.title("class"+ classNum)

    pairing_style = tb.Style()
    pairing_style.configure("primary.Outline.TButton", font = ("Helvetica", 40))
    
    openListButton = tb.Button(
        winClass,
        text = "Classlist",
        style = "primary.Outline.TButton"
        )

    """
    pairButton = ttk.Button(
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
    
    resetButton = ttk.Button(
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
    recordButton = ttk.Button(
        winClass,
        text = "Record\nCurrent",
        command = lambda:[ExcelFunctions.ExcelToMiddle(classNum,"middle"),GUI.MiddleToDatabase(classNum)],
        height = 3,
        width = 7
    )

    newSetButton = ttk.Button(
        winClass,
        text = "New Set",
        command = lambda:[GUI.resetMiddle(classNum),ExcelFunctions.MiddletoExcel(classNum,"middle")],
        height = 3,
        width = 7
    )

    openExcelButton = ttk.Button(
        winClass,
        text = "Open Excel",
        command = lambda:ExcelFunctions.openExcelFile(classNum),
        height = 3,
        width = 7    
    )


    
    pairText = ttk.Label(
        winClass,
        height = 37,
        width = 50,
        relief = ttk.SOLID,
    )
    
    resetDatabase = ttk.Label(
        winClass,
        height = 3,
        width = 10,   
        relief = ttk.SOLID,    
        text = countDown.readCountdownNumber(classNum)
    )


    
     
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
    openListButton.pack()
    openListButton.place(x=100,y=10)





