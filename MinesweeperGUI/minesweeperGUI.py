from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Minesweeper GUI")
root.resizable(True,True)

#click = True
count = 0


#START BY HAVING MINESWEEPER WORK AS A 4X4 GRID


btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()
btn10 = StringVar()
btn11 = StringVar()
btn12 = StringVar()
btn13 = StringVar()
btn14 = StringVar()
btn15 = StringVar()
btn16 = StringVar()

#I can add pictures for the numbers and bombs if I want, and if I add flag functionality, I will have an image for that too.

def play():
    #I can probably make a button factory function, but I will do that after confirming that I can hard code it first.
    button1 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(1,0,0))
    button1.grid(row=0,column=0)

    button2 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn2,command=lambda:press(2,0,1))
    button2.grid(row=0,column=1)

    button3 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(3,0,2))
    button3.grid(row=0,column=2)

    button4 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(4,0,3))
    button4.grid(row=0,column=3)

    button5 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(5,1,0))
    button5.grid(row=1,column=0)

    button6 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(6,1,1))
    button6.grid(row=1,column=1)

    button7 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(7,1,2))
    button7.grid(row=1,column=2)

    button8 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(8,1,3))
    button8.grid(row=1,column=3)

    button9 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(9,2,0))
    button9.grid(row=2,column=0)

    button10 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(10,2,1))
    button10.grid(row=2,column=1)

    button11 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(11,2,2))
    button11.grid(row=2,column=2)

    button12 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(12,2,3))
    button12.grid(row=2,column=3)

    button13 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(13,3,0))
    button13.grid(row=3,column=0)

    button14 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(14,3,1))
    button14.grid(row=3,column=1)

    button15 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(15,3,2))
    button15.grid(row=3,column=2)

    button16 = Button(root,height=2,width=1,relief='ridge',borderwidth=.5,textvariable=btn1,command=lambda:press(16,3,3))
    button16.grid(row=3,column=3)

def makeBombBoard():
    size = 4
    bombs = 3

    array = [[0 for row in range(size)] for col in range(size)] #Makes the array used in generating the board
    for bomb in range(bombs):
        x = random.randint(0,size-1) #Picks an x variable in the board to be a bomb
        y = random.randint(0,size-1) #Picks a y variable in the board to be a bomb
        array[y][x] = 'X' #Sets that selected spot to be a bomb

        #This next section makes it so that the spaces around the bomb are filled to be a 1, showing there is 1 bomb touching that spot

        #Check bottom first:
        if(y >= 0 and y <= size-2):
            if array[y+1][x] != 'X':
                array[y+1][x] += 1 # bottom center
        if (x >=0 and x <= size-2) and (y >= 0 and y <= size-2):
            if array[y+1][x+1] != 'X':
                array[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= size-1) and (y >= 0 and y <= size-2):
            if array[y+1][x-1] != 'X':
                array[y+1][x-1] += 1 # bottom left

        #Check top next:
        if (x >= 0 and x <= size-1) and (y >= 1 and y <= size-1):
            if array[y-1][x] != 'X':
                array[y-1][x] += 1 # top center
        if (x >= 0 and x <= size-2) and (y >= 1 and y <= size-1):
            if array[y-1][x+1] != 'X':
                array[y-1][x+1] += 1 # top right
        if (x >= 1 and x <= size-1) and (y >= 1 and y <= size-1):
            if array[y-1][x-1] != 'X':
                array[y-1][x-1] += 1 # top left

        #Check sides:
        if (x >= 1 and x <= size-1):
            if array[y][x-1] != 'X':
                array[y][x-1] += 1
        if (x >= 0 and x <= size-2):
            if array[y][x+1] != 'X':
                array[y][x+1] += 1
    return array
    #In print(makeBombBoard()), the return is something like [['X', 1, 1, 1], [1, 1, 1, 'X'], [0, 0, 2, 2], [0, 0, 1, 'X']]. This means that for tkinter, I ca check the row and column that the X would be in

def press(num,row,col):
    global count
    labelPhoto = Label(root,text='0')
    labelPhoto.grid(row=row,column=col)
    if num == 1:
        btn1.set('X')
    elif num == 2:
        btn2.set('X')
    elif num == 3:
        btn3.set('X')
    elif num == 4:
        btn4.set('X')
    elif num == 5:
        btn5.set('X')
    elif num == 6:
        btn6.set('X')
    elif num == 7:
        btn7.set('X')
    elif num == 8:
        btn8.set('X')
    elif num == 9:
        btn9.set('X')
    elif num == 10:
        btn10.set('X')
    elif num == 11:
        btn11.set('X')
    elif num == 12:
        btn12.set('X')
    elif num == 13:
        btn13.set('X')
    elif num == 14:
        btn14.set('X')
    elif num == 15:
        btn15.set('X')
    else:
        btn16.set('X')
    count += 1
    checkWin()

def checkWin():
    pass

def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')
    btn10.set('')
    btn11.set('')
    btn12.set('')
    btn13.set('')
    btn14.set('')
    btn15.set('')
    btn16.set('')

play()
root.mainloop()
