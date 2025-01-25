from tkinter import *


window= Tk()

c= Canvas(window, width=500, height=500)
c.pack(padx=50,pady=50)
c.create_line(0,0,500,500, width=5 , fill="green")
c.create_line(0,500,500,0, width=5 , fill="blue" , dash =(3,3))
c.create_rectangle(150,150,350,350, fill="red",outline="yellow",width=5)




window.mainloop()