from tkinter import *

root = Tk()

# Creating label widget
myLabel01 = Label(root, text="Hello World!")
myLabel02 = Label(root, text="Next World!")
# Shoving onto the screen
myLabel01.grid(row=0, column=0)
myLabel02.grid(row=1, column=0)

# Event loop
root.mainloop()