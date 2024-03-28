import ttkbootstrap as tb
from ttkbootstrap.constants import *

#extra classes
import george

win = tb.Window()
win.configure(bg = "white")
win.title("Classes")
win.geometry("600x600")

my_style1 = tb.Style()
my_style1.configure("dark.Outline.TButton", font = ("Helvetica", 40))

my_style2 = tb.Style()
my_style1.configure("primary.Outline.TButton", font = ("Helvetica", 40))

b1 = tb.Button(
    win, 
    text="1", 
    bootstyle="primary",
    command = lambda:george.openClass("1"),
    width = 5,
    style = "primary.Outline.TButton"
)

b2 = tb.Button(
    win, 
    text="2", 
    bootstyle="dark",
    command = lambda:george.openClass("2"),
    width = 5,
    style = "dark.Outline.TButton"
)
          
b3 = tb.Button(
    win, 
    text="3", 
    bootstyle="dark",
    command = lambda:george.openClass("3"),
    width = 5,
    style = "dark.Outline.TButton"
)

b4 = tb.Button(
    win, 
    text="4", 
    bootstyle="dark",
    command = lambda:george.openClass("4"),
    width = 5,
    style = "dark.Outline.TButton"
)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b1.place(x=150, y=150,anchor=CENTER)
b2.place(x=450, y=150,anchor=CENTER)
b3.place(x=150, y=450,anchor=CENTER)
b4.place(x=450, y=450,anchor=CENTER)



win.mainloop()

