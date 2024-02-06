#! /usr/bin/python
from tkinter import Tk, Label

window  = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configurre(bg="steelblue")
label = label(window, text="welcome!", font=("Arial Black" , 78 , "bold") , bg = "steelblue")

window.mainloop()
