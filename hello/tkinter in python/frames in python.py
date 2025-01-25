# to create frames and Buttons  in python 


from tkinter import *

root= Tk()
root.title("Creating Frames ")
root.config(bg="yellow")

Frame1 = Frame(root, height=300,width=500, bg="red",cursor="spider")
# Frame1.pack(side=LEFT)
Frame2 = Frame(root, height=300,width=500, bg="blue",cursor="spider")
# Frame2.pack(side=RIGHT)

Button1= Button(Frame1,text="Sign up",bg="red",fg="white",activebackground="white",activeforeground="black")
# Button1.pack(padx=20,pady=20)
Button2= Button(Frame1,text="Sign in",bg="red",fg="white",activebackground="white",activeforeground="black")
# Button2.pack(padx=20,pady=20)

Button3= Button(Frame2,text="LogOut",bg="red",fg="white",activebackground="white",activeforeground="black")
# Button3.pack()

Label(root,text="Name ::" ).grid(row=1 , column=1)
Label(root,text="Class ::" ).grid(row=2 , column=1)

name = StringVar()
class1 = IntVar()
e1= Entry(root,textvariable=name, width=40, borderwidth=5) 
e1.grid(row=1,column=2)
e2=Entry(root,textvariable=class1 , width=40, borderwidth=5)
e2.grid(row=2,column=2)

root.mainloop()