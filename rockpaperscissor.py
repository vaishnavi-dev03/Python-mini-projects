import random
choices=["rock","paper","scissor"]
print("----ROCK PAPER SCISSOR----")
print("Choose any one level")
print("1.Easy")
print("2.Medium")
print("3.Hard")
option=int(input("Enter your level: "))
if option==1:
    chances=10
elif option==2:
    chances=7
elif option==3:
    chances=5
else:
    print("Invalid option")
    exit()
print("OKEY!!")
print("You have",chances,"chances")
print("Choose")
print("1.rock\n2.paper\n3.scissor")
user_score=0
comp_score=0
for i in range(chances):
    user=input("Enter user choice: ")
    if user not in choices:
       print("Invalid choice")
       continue
    computer=random.choice(choices)
    print("User choice: ",user)
    print("Computer choice: ",computer)
    if user==computer:
        print("DRAW")
    elif user=="rock" and computer=="scissor":
        print("ROCK WINS")
        user_score+=1
    elif user=="paper" and computer=="rock":
        print("PAPER WINS")
        user_score+=1
    elif user=="scissor" and computer=="paper":
        print("SCISSOR WINS")
        user_score+=1
    else:
        print("COMPUTER WINS")
        comp_score+=1

print("user_score",user_score)
print("comp_score",comp_score)
if user_score>comp_score:
    print("hurrah!!, YOU WIN ")
elif comp_score>user_score:
    print("COMPUTER WIN!!")
else:
    print("MATCH DRAW")

print("------GAME OVER------")