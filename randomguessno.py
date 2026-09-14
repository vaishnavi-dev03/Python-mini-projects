import random
target=random.randint(1,100)
while True:
    userChoice=input("Enter the target or QUIT(Q): ")
    if userChoice=="Q":
       break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success! Correct Guess")
        break
    elif(userChoice>target):
        print("Your number is too big.Please take smaller one")
    else:
        print("Your number is too small.please take bigger one")


print("----GAME OVER----")
