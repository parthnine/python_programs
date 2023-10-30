from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry('200x100')
top.title("Welcome to Abhi Window")

messagebox.showinfo("Message", "Hello")

lbl = Label(top, text = "HOW ARE FINE?")
lbl.grid()

def clicked():
    lbl.configure(text = "I am FINE! & You?")
 
btn = Button(top, text = "Click me",fg = "red", command=clicked)
btn.grid(column=1, row=0)
 
 

b= Button(top, text="Click Me")
# b.pack()
top.mainloop()