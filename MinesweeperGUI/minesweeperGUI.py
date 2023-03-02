'''
While I have gotten practice from the TicTacToe tkinter project, there are some commands here that I still needed to look up, and do not claim credit for.
A great help for me was Vakus on stack overflow, as they used button commands that I didn't know about. (Stuff like sticky, lambda, and using a button list instead of making
the buttons manually.)
'''
from tkinter import *
from tkinter import messagebox
import random
import tkinter

root = Tk()
root.title("Minesweeper GUI")
size = 4
bombs = 3
board = []
buttons = []
count = 0
movesMade = []
colors = ['dodgerblue','forestgreen','red','purple3','salmon2','cyan','darkorange','gray']
root.resizable(True,True)
buttonState = True #Defaults by allowing normal presses, if button state is false, then an F is placed on that spot as a flag

#I can add pictures for the numbers and bombs if I want, and if I add flag functionality, I will have an image for that too.
#Need to check place before flagging, if the spot is already in moves made, then you can't place a flag there

def makeBombBoard():
    #Make the field
    global size,bombs,board
    board = []
    for x in range(0,size):
        board.append([])
        for y in range(0,size):
            board[x].append(0)
    #Distribute bombs
    for _ in range(0,bombs):
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        while board[x][y] == 'X':
            x = random.randint(0,size-1)
            y = random.randint(0,size-1)            
        board[x][y] == 'X'
        if(board[y][x] != 'X'):
                board[y][x] = 'X'
                if(y >= 0 and y <= size-2):
                    if board[y+1][x] != 'X':
                        board[y+1][x] += 1 # bottom center
                if (x >=0 and x <= size-2) and (y >= 0 and y <= size-2):
                    if board[y+1][x+1] != 'X':
                        board[y+1][x+1] += 1 # bottom right
                if (x >= 1 and x <= size-1) and (y >= 0 and y <= size-2):
                    if board[y+1][x-1] != 'X':
                        board[y+1][x-1] += 1 # bottom left
                #Check top next:
                if (x >= 0 and x <= size-1) and (y >= 1 and y <= size-1):
                    if board[y-1][x] != 'X':
                        board[y-1][x] += 1 # top center
                if (x >= 0 and x <= size-2) and (y >= 1 and y <= size-1):
                    if board[y-1][x+1] != 'X':
                        board[y-1][x+1] += 1 # top right
                if (x >= 1 and x <= size-1) and (y >= 1 and y <= size-1):
                    if board[y-1][x-1] != 'X':
                        board[y-1][x-1] += 1 # top left
                #Check sides:
                if (x >= 1 and x <= size-1):
                    if board[y][x-1] != 'X':
                        board[y][x-1] += 1
                if (x >= 0 and x <= size-2):
                    if board[y][x+1] != 'X':
                        board[y][x+1] += 1
    return board

def medMode():
    global size, bombs, root
    size = 6
    bombs = 9
    for x in root.winfo_children():
        x.destroy()
    makePopup()
    makeBombBoard()

def hardMode():
    global size, bombs, root
    size = 10
    bombs = 25
    for x in root.winfo_children():
        x.destroy()
    makePopup()
    makeBombBoard()

def toggleMode():
    global buttonState
    if buttonState == True:
        buttonState = False
    else:
        buttonState = True

def makePopup():
    global size, buttons
    Button(root, text="Restart", command=restartGame).grid(row=0, column=0, columnspan=size, sticky=N+W+S+E)
    Button(root, text="Flag",command=toggleMode).grid(row=1, column=0, columnspan=size, sticky=N+W+S+E)
    Button(root,text="Easy", fg='limegreen', command=restartGame).grid(row=size+2,column=0,columnspan=size,sticky=N+W+S+E)
    Button(root,text="Medium", fg='orange', command=medMode).grid(row=size+3,column=0,columnspan=size,sticky=N+W+S+E)
    Button(root,text="Hard", fg='darkred', command=hardMode).grid(row=size+4,column=0,columnspan=size,sticky=N+W+S+E)
    buttons = []
    for x in range(0,size):
        buttons.append([])
        for y in range(0,size):
            button = Button(root,text=" ", width=2,command=lambda x=x,y=y:press(x,y))
            button.grid(row=x+2,column=y,sticky=N+S+W+E)
            buttons[x].append(button)

def restartGame(): #This function literally just remakes the bomb board and the popup. Will be used in a restart button available on screen.
    global root, count, board, size, bombs, movesMade, buttonState
    for x in root.winfo_children():
        x.destroy()
    board = []
    size = 4
    bombs = 3
    count = 0
    movesMade = []
    buttonState = True
    makePopup()
    makeBombBoard()
    

def press(row,col):
    global size, board, buttons, count, buttonState
    if buttonState == True:
        buttons[row][col]["text"]=str(board[row][col])
        if board[row][col] == 'X':
            buttons[row][col]["text"] = "X"
            buttons[row][col].config(background='red', disabledforeground='black')
            messagebox.showinfo(message="Game over, you lose!")
            for x in range(0,size):
                for y in range(0,size):
                    if board[x][y] == 'X':
                        buttons[x][y]["text"] = "X"
        else:
            if ([row,col]) in movesMade:
                count -= 1
            else:
                movesMade.append([row,col])
                buttons[row][col].config(disabledforeground=colors[board[row][col]])
            count += 1
        if board[row][col] == 0:
            buttons[row][col]["text"] = " "
            autoFill(row,col)
        buttons[row][col]["state"] = "disabled"
        buttons[row][col].config(relief=SUNKEN)
        checkWin()
    if buttonState == False:
        if buttons[row][col]["text"] == "F":
            buttons[row][col]["text"] = " "
        else:    
            buttons[row][col]["text"] = "F"


'''
Note: I found this auto fill function on stack overflow for filling in Minesweeper 0s
Made by Vakus
'''
def autoFill(x,y):
    global board, buttons, colors, size, count
    if buttons[x][y]["state"] == "disabled":
        return
    if board[x][y] != 0:
        buttons[x][y]["text"] = str(board[x][y])
        count += 1
    else:
        buttons[x][y]["text"] = " "
    buttons[x][y].config(disabledforeground=colors[board[x][y]])
    buttons[x][y].config(relief=tkinter.SUNKEN)
    buttons[x][y]['state'] = 'disabled'
    count += 1
    if board[x][y] == 0:
        if x != 0 and y != 0:
            autoFill(x-1,y-1)
        if x != 0:
            autoFill(x-1,y)
        if x != 0 and y != size-1:
            autoFill(x-1,y+1)
        if y != 0:
            autoFill(x,y-1)
        if y != size-1:
            autoFill(x,y+1)
        if x != size-1 and y != 0:
            autoFill(x+1,y-1)
        if x != size-1:
            autoFill(x+1,y)
        if x != size-1 and y != size-1:
            autoFill(x+1,y+1)

def checkWin():
    # global count,bombs,size
    # moves = (size * size) - bombs
    # if count == moves:
    #     messagebox.showinfo(message="You win! Congrats!")
    global buttons, board, size
    done = True
    for x in range(0, size):
        for y in range(0,size):
            if board[x][y] != 'X' and buttons[x][y]["state"] != "disabled":
                done = False
    if done:
        messagebox.showinfo(message="You win! Congrats!")



def play():
    #Set a default size for when the game is launched, and it is able to be changed by hitting the difficulty buttons
    global size, bombs, board, buttonState
    size = 4
    bombs = 3
    buttonState = True
    makeBombBoard()
    makePopup()


play()
root.mainloop()