
from tkinter import *
import tkinter.messagebox as tmsg

window= Tk()
window.config(bg="green")
tmsg.showinfo("Acess", "Now you can Access The email Archee2801@gmail.com")

tmsg.showwarning("Denied"," you cannot acess the email blocked  by Google ! ")

question = tmsg.askyesno("Is it? ","Did you know Archee Singh?")

if question:
    print("Message Aru! ")
    tmsg.showinfo("Okay","Message Aru! ")
else:
    print("Add her in your life")
    tmsg.showinfo("Okay"," Donot Message Aru! ")
