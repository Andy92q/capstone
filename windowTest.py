import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

def add(a,b):
    print(int(a)+int(b))
    l3.config(text=str(int(a)+int(b)))
    return int(a)+int(b)


style=ttk.Style()
style.configure('MyButton.TButton',background="#ff0000", font=('Helvetica',30))



b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS,  style="MyButton.TButton",command = lambda:add(l1.cget('text'),l2.cget("text")))
b1.pack(side=LEFT, padx=5, pady=10)



l1 = ttk.Label(root, text = "456", bootstyle = SUCCESS,)
l1.pack(side = LEFT, padx = 5, pady = 10)

l2 = ttk.Label(root, text = "123", bootstyle = SUCCESS)
l2.pack(side = LEFT, padx = 5, pady = 10)

l3 = ttk.Label(root, text = "", bootstyle = SUCCESS)
l3.pack(side = LEFT, padx = 5, pady = 10)
root.mainloop()
