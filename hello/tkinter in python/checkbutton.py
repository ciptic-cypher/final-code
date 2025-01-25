from tkinter import *
def func1():
    a= check_box_1.get()
    b=check_box_2.get()
    c= check_box_3.get()

    print("a={},b={},c={}".format(a,b,c))

root= Tk()

check_box_1 = IntVar()
check_box_2 = IntVar()
check_box_3 = IntVar()

Checkbutton(root, text="Check 1 " , onvalue=1, offvalue=0,variable=check_box_1).pack()
Checkbutton(root, text="Check 2 " , onvalue=2, offvalue=0,variable=check_box_2).pack()
Checkbutton(root, text="Check 3 " , onvalue=3, offvalue=0,variable=check_box_3).pack()

Button(root, text="Submit ",command=func1).pack()

root.mainloop()