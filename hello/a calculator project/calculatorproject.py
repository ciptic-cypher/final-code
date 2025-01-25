from tkinter import *
global cal 
cal=0

window= Tk()
window.title("Calculator")
window.geometry("550x600+700+100")
window.config(bg="#292929")

#functions
def fun1():
    b.set(str(c.get())+"1")
def fun2():
    b.set(str(c.get())+"2")
def fun3():
    b.set(str(c.get())+"3")
def fun4():
    b.set(str(c.get())+"4")
def fun5():
    b.set(str(c.get())+"5")
def fun6():
    b.set(str(c.get())+"6")
def fun7():
    b.set(str(c.get())+"7")
def fun8():
    b.set(str(c.get())+"8")
def fun9():
    b.set(str(c.get())+"9")
def fun0():
    b.set(str(c.get())+"0")
def oper1():
    d.set(d.get()+int(c.get()))
    b.set("")
def oper2():
    d.set(d.get()-int(c.get()))
    b.set("")
def oper3():
    d.set(d.get()*int(c.get()))
    b.set("")
def opere():
    b.set(d.get())
def oper5():
    d.set(0)
    b.set("")
d=IntVar()
d.set(0)
b=StringVar()
# Entry box
c=Entry(window,width=30, borderwidth=2,relief=FLAT, bg="#393937", fg="#fff", font="Roboto 18",textvariable=b,state=DISABLED)
c.grid(column=0,row=0,columnspan=5)
# Number buttons
Button(window,text=1,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun1).grid(row=1,column=0)
Button(window,text=2,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun2).grid(row=1,column=1)
Button(window,text=3,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun3).grid(row=1,column=2)
Button(window,text=4,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun4).grid(row=2,column=0)
Button(window,text=5,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun5).grid(row=2,column=1)
Button(window,text=6,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun6).grid(row=2,column=2)
Button(window,text=7,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun7).grid(row=3,column=0)
Button(window,text=8,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun8).grid(row=3,column=1)
Button(window,text=9,padx=60,pady=60,relief=GROOVE,activeforeground="blue",activebackground="purple",fg="#fff",bg="#292929",command=fun9).grid(row=3,column=2)
# creating operatings
Button(window,text="+",padx=60,pady=60,relief=GROOVE,activebackground="purple",activeforeground="blue",fg="#fff",bg="#292929",command=oper1).grid(row=1,column=4)
Button(window,text="-",padx=60,pady=60,relief=GROOVE,activebackground="purple",activeforeground="blue",fg="#fff",bg="#292929",command=oper2).grid(row=2,column=4)
Button(window,text="*",padx=60,pady=60,relief=GROOVE,activebackground="purple",activeforeground="blue",fg="#fff",bg="#292929",command=oper3).grid(row=3,column=4)
Button(window,text="=",padx=60,pady=60,relief=GROOVE,activebackground="purple",activeforeground="blue",fg="#fff",bg="#292929",command=opere).grid(row=4,column=4)
Button(window,text="0",padx=60,pady=60,relief=GROOVE,activebackground="purple",activeforeground="blue",fg="#fff",bg="#292929",command=fun0).grid(row=4,column=2)
Button(window,text="D",padx=60,pady=60,relief=GROOVE,activebackground="purple",activeforeground="blue",fg="#fff",bg="#292929",command=oper5).grid(row=4,column=1)
Button(window,text="<",padx=60,pady=60,relief=GROOVE,activebackground="purple",activeforeground="blue",fg="#fff",bg="#292929",command=exit).grid(row=4,column=0)

window.mainloop()