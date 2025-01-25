from tkinter import*

root= Tk()

menu = Menu(root)

file = Menu(menu,tearoff=1)
file.add_command(label="hello1")
file.add_command(label="hello2")
file.add_command(label="hello3")
file.add_separator()
file.add_command(label="exit",command=exit)
menu.add_cascade(menu=file)
root.config(menu=menu)

root.mainloop()