import tkinter as tk

#extra classes
import window


win = tk.Tk()
win.configure(bg = "white")
win.title("Classes")
win.geometry("800x800")


b1 = tk.Button(
    text = "1",
    command = lambda:window.openClass("1")
)
b2 = tk.Button(
    text = "2",
    command = lambda:window.openClass("2")
)
b3 = tk.Button(
    text = "3",
    command = lambda:window.openClass("3")
)
b4 = tk.Button(
    text = "4",
    command = lambda:window.openClass("4")
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
