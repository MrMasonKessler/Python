from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

root = Tk()
root.geometry(f'{700}x{300}')
frame = ttk.Frame(root,padding=10)
frame.grid()
ttk.Label(frame,text="Hello, World!").grid(column=0,row=0)
ttk.Button(frame,text="Quit",command=root.destroy).grid(column=1,row=0)
root.mainloop()