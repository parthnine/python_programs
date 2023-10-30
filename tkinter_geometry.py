from tkinter import Tk, mainloop, TOP 
from tkinter.ttk import Button 

root = Tk() 
root.geometry('200x150') 

button = Button(root, text = 'Click me') 
button.pack() 
 
root.mainloop()
