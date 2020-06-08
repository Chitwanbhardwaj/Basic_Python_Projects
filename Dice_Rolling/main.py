import random
def Dice_Rolling():
    min_value = 1
    max_value = 6

    roll = True

    while roll:
        print(random.randint(min_value,max_value))

        roll_again = input("Do you want to roll the dice again? ")

        if roll_again == "yes" or roll_again =="y":
            roll = True
        else:
            roll = False     

Dice_Rolling()            
