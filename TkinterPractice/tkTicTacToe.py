'''
For this file, I was following a follow-along coding video made by Web Dev Tutorials in order to learn tkinter better. None of this code is mine, and it will be useful for me to
reference as I try to make my own projects with tkinter.
The video I watched: https://www.youtube.com/watch?v=FrkofcY9whY&t=0s&ab_channel=WebDevTutorials
'''
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.iconbitmap("tictactoe-ico.ico") #This should make the icon in the top left of the tkinter popup into the icon tictactoe-ico.ico, but it doesn't for some reason
root.resizable(width=False,height=False) #Don't need the width= or height=, it is implied

click = True
count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xPhoto = PhotoImage(file="tic-x.png")
oPhoto = PhotoImage(file="tic-o.png")

def play():
    button1 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#47d147',textvariable=btn1,command=lambda:press(1,0,0))
    button1.grid(row=0,column=0)

    button2 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#47d147',textvariable=btn2,command=lambda:press(2,0,0))
    button2.grid(row=0,column=1)

    button3 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#47d147',textvariable=btn3,command=lambda:press(3,0,0))
    button3.grid(row=0,column=2)

    button4 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#248f24',textvariable=btn4,command=lambda:press(4,0,0))
    button4.grid(row=1,column=0)

    button5 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#248f24',textvariable=btn5,command=lambda:press(5,0,0))
    button5.grid(row=1,column=1)

    button6 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#248f24',textvariable=btn6,command=lambda:press(6,0,0))
    button6.grid(row=1,column=2)

    button7 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#ebfaeb',textvariable=btn7,command=lambda:press(7,0,0))
    button7.grid(row=2,column=0)

    button8 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#ebfaeb',textvariable=btn8,command=lambda:press(8,0,0))
    button8.grid(row=2,column=1)

    button9 = Button(root,height=9,width=19,relief='ridge',borderwidth=.5,background='#ebfaeb',textvariable=btn9,command=lambda:press(9,0,0))
    button9.grid(row=2,column=2)




def press(num,row,col):

    pass

#def checkWin():

#def clear():


root.mainloop()