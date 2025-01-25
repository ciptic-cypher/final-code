from tkinter import *

def run():
    print("clicked")

root= Tk()
root.config(bg="yellow")

Button(root, text="Click me", font="Algerian 17" , activebackground="#292929" , activeforeground="#fff",cursor="circle" , command=run ).pack(padx=10,pady=10)
root.mainloop()