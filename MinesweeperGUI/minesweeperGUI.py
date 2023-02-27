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
size = 6
bombs = 6
board = []
buttons = []
count = 0
movesMade = []
root.resizable(True,True)

#I can add pictures for the numbers and bombs if I want, and if I add flag functionality, I will have an image for that too.

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

def makePopup():
    global size, buttons
    Button(root, text="Restart", command=restartGame).grid(row=0, column=0, columnspan=size, sticky=N+W+S+E)
    buttons = []
    for x in range(0,size):
        buttons.append([])
        for y in range(0,size):
            button = Button(root,text=" ", width=2,command=lambda x=x,y=y:press(x,y))
            button.grid(row=x+1,column=y,sticky=N+S+W+E)
            buttons[x].append(button)


def restartGame(): #This function literally just remakes the bomb board and the popup. Will be used in a restart button available on screen.
    makePopup()
    makeBombBoard()

def press(row,col): #STILL NEED TO FINISH THIS FUNCTION
    global size, board, buttons, count
    buttons[row][col]["text"]=str(board[row][col])
    if board[row][col] == 'X':
        buttons[row][col]["text"] = "X"
        messagebox.showinfo(message="Game over, you lose!")
        for x in range(0,size):
            for y in range(0,size):
                buttons[x][y]["text"] = "X"
    else:
        if ([row,col]) in movesMade:
            count -= 1
        else:
            movesMade.append([row,col])
        count += 1
    checkWin()



def checkWin():
    global count,bombs,size
    moves = (size * size) - bombs
    if count == moves:
        messagebox.showinfo(message="You win! Congrats!")


def play():
    makePopup()
    makeBombBoard()

play()
root.mainloop()
