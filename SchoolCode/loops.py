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

def print_range():
    seq = range(11) #0-10
    print("\nFirst range: 0 - 10")
    for element in seq:
        print(element,end=" ")
    print()

    seq = range(0,21,2) #0-20, steps up by 2s
    print("\nSecond range: 0 - 20, goes up by 2")
    for element in seq:
        print(element,end= " ")
    print()

    seq = range(5,16,2)
    index = 0
    print("\nThird range, shows how to use indexes instead of iteration")
    while index < len(seq):
        print(seq[index],end=" ")
        index+=1
    print()

    seq = range(10,-1,-1)
    index = 0
    print("\nFourth range, shows that you can go backwards through iteration")
    while index < len(seq):
        print(seq[index], end=" ")
        index+=1
    print()

def reverse_string():
    userIn = str(input("Please enter a string you wish to reverse: "))
    reversed = ""
    for i in range(len(userIn)-1,-1,-1):
        reversed = reversed + userIn[i]
    print(reversed)

def split():
    string = "ABC DE FGHI"
    tokens = string.split(" ")
    for token in tokens:
        print(token)



def main():
    #countdown(10)
    #count_up(10)
    #print_chars()
    #loop_control()
    #print_range()
    #reverse_string()
    split()


if __name__ == "__main__":
    main()