import tkinter as tk

window = tk.Tk()

menu = tk.Menu(window)

file= tk.Menu(menu, tearoff=1)

file.add_command(label="New File")
file.add_command(label="New Window")
file.add_separator()
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Save As")
file.add_separator()
file.add_command(label="Exit", command= window.destroy)


Hello= tk.Menu(menu, tearoff=0)
Hello.add_command(label="New Hello 1")
Hello.add_command(label="New Window 1")
Hello.add_separator()
Hello.add_command(label="Save 1")
Hello.add_command(label="Save As 1")
Hello.add_command(label="Save As 1")
Hello.add_separator()
Hello.add_command(label="Exit 1", command= window.quit)

menu.add_cascade(menu= Hello)
menu.add_cascade(menu= file)
window.config(menu=menu)

window.mainloop()