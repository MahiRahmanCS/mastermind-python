import customtkinter 

import tkinter


root = tkinter.Tk()

label = tkinter.Label(root, text="Hello World")
label.config(width=100, height=100)
label.pack()
root.mainloop()