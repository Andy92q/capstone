
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import window




root = ttk.Window()
root.configure(bg = "white")
root.title("Classes")
root.geometry("800x800")

my_style = ttk.Style()
my_style.configure("success.Outline.TButton", font = ("Helvetica", 40))

b1 = ttk.Button(
    root, 
    text="1", 
    bootstyle="success",
    command = lambda:window.openClass("1"),
    width = 5,
    style = "success.Outline.TButton"
)
b1.pack(side=LEFT, padx=5, pady=10)

root.mainloop()



