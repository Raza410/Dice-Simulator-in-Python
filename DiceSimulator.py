import random as rn

def dice():
    x = rn.randrange(1, 6)
    
    if x == 1:
        print(" ----------")
        print("|          |")
        print("|     o    |")
        print("|          |")
        print(" ----------")

    if x == 2:
        print(" ----------")
        print("|          |")
        print("|  o    o  |")
        print("|          |")
        print(" ----------")

    elif x == 3:
        print(" ----------")
        print("|        o |")
        print("|     o    |")
        print("|  o       |")
        print(" ----------")

    elif x == 4:
        print(" ----------")
        print("|  o    o  |")
        print("|          |")
        print("|  o    o  |")
        print(" ----------")

    elif x == 5:
        print(" ----------")
        print("|  o    o  |")
        print("|     o    |")
        print("|  o    o  |")      
        print(" ----------")

    elif x == 6:
        print(" ----------")
        print("|  o    o  |")
        print("|  o    o  |")
        print("|  o    o  |")
        print(" ----------")

a = "y"

while a == "y":
    
    dice()
        
    print("Roll Again:   y/n")
    a = input()



