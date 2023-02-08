import random
import os


def minesweeper():
    clear_term()
    size = int(input("Please enter the length of the board: "))
    print()
    array = [["-" for row in range(size)] for col in range(size)]
    for row in array:
        print(" ".join(str(cell) for cell in row))
        print("")



def clear_term(): #This function is to clear the terminal every time the game is started.
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def main():
    minesweeper()


if __name__ == "__main__":
    main()