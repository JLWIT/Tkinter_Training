from tkinter import *

root = Tk()

myButton =  Button(root, text="Click Me", state=DISABLED, padx=50)

myButton.pack()

# Event loop
root.mainloop()