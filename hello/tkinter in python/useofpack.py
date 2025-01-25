# the use of pack function 
# pack takes three arguments 1) fill, 2)side , 3)expand 

from tkinter import *


root= Tk()

Label1= Label(root, text="Label1", bg="red", fg="white")
Label2= Label(root, text="Label2", bg="blue", fg="white")
Label3= Label(root, text="Label3", bg="green", fg="white")



Label1.pack(side="top",fill=X,expand="False")
Label2.pack(side="left",fill=Y,expand="False")
Label3.pack(side="right",fill=BOTH,expand="True")

root.mainloop()