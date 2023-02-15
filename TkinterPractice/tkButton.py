from tkinter import *
from tkinter import ttk

number = 0

def click():
    global number
    number += 1
    number_label.configure(text=f'{number}')

root = Tk()
root.geometry("700x400")
root.title("Button Incrementor")
number_label = Label(root,text="0")
number_label.grid(column=0,row=1)
button = Button(root,command=click,text="Click me!",width=15,height=5).grid(row=2,column=2)
root.mainloop()