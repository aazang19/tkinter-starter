# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="Hello")

# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)
spin = Spinbox(window, from_=0, to=100)
spin = Spinbox(window, from_=0, to=100, width=5)
from tkinter import *
 
window = Tk()
 
window.title("Welcome to class")
 
window.geometry('350x200')
 
spin = Spinbox(window, from_=0, to=100, width=5)
 
spin.grid(column=0,row=0)
 
window.mainloop()
spin = Spinbox(window, values=(3, 8, 11), width=5)
var =IntVar()
 
var.set(36)
 
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
from tkinter.ttk import Progressbar
 
bar = Progressbar(window, length=200)
bar['value'] = 70





window.mainloop()     # Keep the window open
