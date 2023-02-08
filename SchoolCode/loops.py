#This file is just testing out different loops. I could include some error checking and limits on the loops so the user
#input doesn't break it, but I won't be doing that here. 

def countdown(number):
    sum = 0
    while number >= 0:
        print(number)
        sum += number
        number -= 1
    return sum

def count_up(number):
    current = 0
    sum = 0
    while current < number:
        print(current)
        sum += current
        current += 1
    return sum

def print_chars():
    choice = int(input("Would you like the string forwards [1] or backwards [2]: "))
    string = str(input("Please enter a string: "))
    if choice==1:
        index = 0
        while index < len(string):
            print(string[index])
            index+=1
    if choice==2:
        index = len(string)-1
        while index >= 0:
            print(string[index])
            index-=1

def loop_control():
    sum = 0

    while True:
        number = int(input("Enter a number, or 0 to break>> "))
        if number == 0:
            break
        elif number%2  == 0:
            continue
        else:
            sum += number
    print("Sum =", sum)




def main():
    #countdown(10)
    #count_up(10)
    #print_chars()
    loop_control()


if __name__ == "__main__":
    main()