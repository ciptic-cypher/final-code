#by harshit agrawal 2 


from tkinter import *


root = Tk()
root.title("Hello World")
root.config(bg="red")
imp = Label(root, text="Hello World",bg="red",fg="white",font=("Roboto",20),cursor="dot")
imp.pack(side=BOTTOM)

root.mainloop()