#This file is just testing basic conversions.

from json.tool import main


def convert_height():
    height_inch = int(input("Enter your height in inches: "))
    if(height_inch%12==0):
        print("You are ", height_inch//12, "' tall.", sep="")
    else:
        print("You are ", height_inch//12, "' ", height_inch%12, '" tall.', sep="")


def convert_distance():
    kilometers = int(input("Enter a distance in kilometers: "))
    miles = int(kilometers*.621371)
    feet = int(miles)*5280
    inches = int(feet)*12
    print(kilometers, "kilometers is", miles, "miles =", feet, "feet =", inches, "inches.")


def main():
    userIn = int(input("Enter 1 for height, or 2 for distance: "))
    if userIn==1:
        convert_height()
    if userIn==2:
        convert_distance()



if __name__ == '__main__':
    main()
    
