from tkinter import *
def func1():
    a= hello.get()
    ok.set(a)


window = Tk()

# message=  Message(window="hello")
# message.pack()

hello= StringVar()
b= Entry(window, textvariable=hello)
b.pack()
ok= StringVar()
message=  Message(window,textvariable=ok,relief=RAISED,padx=10,pady=10)
message.pack()

Button(window,text="Submit",command=func1).pack()
mainloop()
