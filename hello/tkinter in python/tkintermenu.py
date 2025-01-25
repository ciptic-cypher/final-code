from tkinter import *

root = Tk()

menu = Menu(root)
file = Menu(menu, tearoff=0)

file.add_command(label= "New")
file.add_command(label= "old")
file.add_separator()
file.add_command(label= "friend")
file.add_command(label= "named")
file.add_separator()
file.add_command(label= "Aru",command=exit)
menu.add_cascade( menu= file, label="menu")
root.config(menu=menu)
root.mainloop()