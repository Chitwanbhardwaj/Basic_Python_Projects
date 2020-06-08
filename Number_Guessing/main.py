import random

Num = random.randrange(1,100)
print(Num)

Ans = int(input("Please enter your guess:- "))

if Ans == Num:
    print("You got it Right!!!")
elif Ans < Num:
    print("The number you are trying to guess is greater than your prediction!")
else:
    print("The number you are trying to guess is less than your prediction!") 
