import pairing
import ExcelFunctions
import countDown
import GUI

import tkinter as tk
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *


def openClass(classNum):  # Open class x

    winClass = Toplevel()
    winClass.geometry("600x700")  # 48
    winClass.title("class" + classNum)

    studentList_style = tb.Style()
    studentList_style.configure("warning.Outline.TButton", font=("Helvetica", 20))
    pairing_style = tb.Style()
    pairing_style.configure("primary.Outline.TButton", font=("Helvetica", 20))

    reset_style = tb.Style()
    reset_style.configure("danger.Outline.TButton", font=("Helvetica", 20))

    excel_style = tb.Style()
    excel_style.configure("success.Outline.TButton", font=("Helvetica", 20))

    openListButton = tb.Button(
        winClass,
        text="Classlist",
        command=lambda: openList(classNum),
        style="warning.Outline.TButton",
        width=21,
        padding=10,
    )

    pairButton = tb.Button(
        winClass,
        text="New Pair",
        command=lambda: [
            GUI.refreshPairingLabel(pairText, winClass, pairing.producePair(classNum)),
            ExcelFunctions.MiddletoExcel(classNum, "middle"),
            resetDatabase.config(text=countDown.readCountdownNumber(classNum)),
        ],
        style="primary.Outline.TButton",
        width=21,
        padding=10,
    )

    resetButton = tb.Button(
        winClass,
        text="Reset MainDrive",
        command=lambda: [
            GUI.resetDatabase(classNum),
            pairText.config(text=""),
            resetDatabase.config(text=GUI.resetDatabase(classNum)),
        ],
        style="danger.Outline.TButton",
        width=21,
        padding=10,
    )

    # record excel to middle and database
    recordButton = tb.Button(
        winClass,
        text="Record Current",
        command=lambda: [
            ExcelFunctions.ExcelToMiddle(classNum, "middle"),
            GUI.MiddleToDatabase(classNum),
        ],
        style="primary.Outline.TButton",
        width=21,
        padding=10,
    )

    newSetButton = tb.Button(
        winClass,
        text="New Set",
        command=lambda: [
            GUI.resetMiddle(classNum),
            ExcelFunctions.MiddletoExcel(classNum, "middle"),
        ],
        style="primary.Outline.TButton",
        width=21,
        padding=10,
    )

    openExcelButton = tb.Button(
        winClass,
        text="Open Excel",
        command=lambda: ExcelFunctions.openExcelFile(classNum),
        style="success.Outline.TButton",
        width=21,
        padding=10,
    )

    pairText = tk.Label(
        winClass,
        height=27,
        width=62,
        relief=tk.SOLID,
    )

    resetDatabase = tb.Label(
        winClass,
        relief=tk.SOLID,
        text=countDown.readCountdownNumber(classNum),
        bootstyle="inverse-light",
        padding=[280, 10],
    )

    openListButton.pack()
    openListButton.place(x=443.75, y=660, anchor=CENTER)
    pairButton.pack()
    pairButton.place(x=156.25, y=540, anchor=CENTER)
    resetButton.pack()
    resetButton.place(x=443.75, y=600, anchor=CENTER)
    recordButton.pack()
    recordButton.place(x=156.25, y=600, anchor=CENTER)
    newSetButton.pack()
    newSetButton.place(x=443.75, y=540, anchor=CENTER)
    openExcelButton.pack()
    openExcelButton.place(x=156.25, y=660, anchor=CENTER)

    pairText.pack()
    pairText.place(x=300, y=280, anchor=CENTER)
    resetDatabase.pack()
    resetDatabase.place(x=300, y=30, anchor=CENTER)


def openList(classNum):  # open studentlist x
    winList = Toplevel()
    winList.geometry("400x500")
    winList.title("class" + classNum + "List")

    cancel_style = tb.Style()
    cancel_style.configure("danger.Outline.TButton", font=("Helvetica", 20))

    saving_style = tb.Style()
    saving_style.configure("success.Outline.TButton", font=("Helvetica", 20))

    line = GUI.readStudentName(classNum)
    textArea = tk.Text(
        winList,
        height=25,
        width=38,
        bd=2,
        relief=tk.SOLID,
    )

    saveButton = tb.Button(
        winList,
        text="Save",
        command=lambda: GUI.saveStudentList(
            "./classes/class" + classNum + ".txt", textArea
        ),
        style="success.Outline.TButton",
        width=13,
        padding=10,
    )

    cancelButton = tb.Button(
        winList,
        text="Cancel",
        command=lambda: winList.destroy(),
        style="danger.Outline.TButton",
        width=13,
        padding=10,
    )

    for i in range(len(line)):
        textArea.insert(tk.END, line[i])

    textArea.pack()
    textArea.place(x=200, y=220, anchor=CENTER)
    saveButton.pack()
    saveButton.place(x=106.25, y=460, anchor=CENTER)
    cancelButton.pack()
    cancelButton.place(x=293.75, y=460, anchor=CENTER)
