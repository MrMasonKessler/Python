import random
import os
import time


def minesweeper(n):
    clear_term()
    #size = int(input("Please enter the length of the board: "))
    print()
    print("Generating board . . .")
    time.sleep(1.5)
    print()
    clear_term()
    print("MINESWEEPER CLI GAME\n")


    array = [[0 for row in range(n)] for col in range(n)] #Makes the array used in generating the board
    x = random.randint(0,4) #Picks an x variable in the board to be a bomb
    y = random.randint(0,4) #Picks a y variable in the board to be a bomb
    array[y][x] = 'X' #Sets that selected spot to be a bomb

    #This next section makes it so that the spaces around the bomb are filled to be a 1, showing there is 1 bomb touching that spot

    #Adds the bombs for the x-axis for columns that aren't to the far left or right
    if (x <= 3 and x >= 1):
       array[y][x+1] += 1
       array[y][x-1] += 1
    
    #If the bomb is on far left, then the right is a bomb
    if (x == 0):
        array[y][x+1] += 1

    #If the bomb is on the far right, then the left is a bomb
    if (x == 4):
        array[y][x-1] += 1

    #Checks top left of the bomb
    if (x >= 1 and x <= 4) and (y <= 4 and y >= 1):
        array[y-1][x-1] += 1

    #Checks top right of the bomb
    if (x >= 0 and x <= 3) and (y <= 4 and y >= 1):
        array[y-1][x+1] += 1

    #Checks the top and the bottom of the bomb
    if (y <= 3 and y >= 1):
        array[y-1][x] += 1
        array[y+1][x] += 1
    
    #Checks the bottom of the bomb
    if (y == 0):
        array[y+1][x] += 1
    
    #Checks the top of the bomb
    if (y == 4):
        array[y-1][x] += 1

    #Checks the bottom right of the bomb
    if (x >= 0 and x <= 3) and (y <= 3 and y >= 0):
        array[y+1][x+1] += 1

    #Checks the bottom left of the bomb
    if (x >= 1 and x <= 4) and (y <= 3 and y >= 0):
        array[y+1][x-1] += 1






    for row in array:
        print(" ".join(str(cell) for cell in row))
        print("")


def clear_term(): #This function is to clear the terminal every time the game is started.
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def main():
    minesweeper(5)


if __name__ == "__main__":
    main()