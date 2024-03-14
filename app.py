import tkinter as tk
from tkinter import ttk
from tkinter import *

#extra classes
import window


win = tk.Tk()
win.configure(bg = "white")
win.title("Classes")
win.geometry("800x800")


style = ttk.Style()
style.theme_use('clam')  
style.configure("classButton.TButton", 
                foreground = "#3140FE",
                background = "#82D5FF", 
                padding=(60,60), 
                borderwidth=5, 
                font=("Times New Roman", 25))


b1 = ttk.Button(
    text = "1",
    style = "classButton.TButton",
    command = lambda:window.openClass("1")
)


b2 = ttk.Button(
    text = "2",
    style = "classButton.TButton",
    command = lambda:window.openClass("2")
)

            
b3 = ttk.Button(
    text = "3",
    style = "classButton.TButton",
    command = lambda:window.openClass("3")
)
b4 = ttk.Button(
    text = "4",
     style = "classButton.TButton",
    command = lambda:window.openClass("4")
)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b1.place(x=200, y=200,anchor=CENTER)
b2.place(x=600, y=200,anchor=CENTER)
b3.place(x=200, y=600,anchor=CENTER)
b4.place(x=600, y=600,anchor=CENTER)



win.mainloop()