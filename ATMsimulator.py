pin=1234
attempt=0
while attempt<3:
    user_pin=int(input("Enter your pin: "))
    if user_pin==pin:
        print("Login Successful")
        break
    else:
        print("Wrong pin")
        attempt+=1
    if attempt>=3:
        print("Too many wrong attempts.Card blocked!")
        exit()
balance=50000
while True:
    print("----ATM MENU----")
    print("1.Check balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Change PIN")
    print("5.Exit")
            
    option=int(input("Enter your choice"))

    def bal():
        print("Your current balance amount: ",balance)

    def deposit():
        global balance
        amount=int(input("enter your deposit amount: "))
        print("Your deposit amount: ",amount)
        balance+=amount
        print("Now your balance amount: ",balance)

    def withdraw():
        global balance
        amount=int(input("Enter your witthdraw amount: "))
        print("Your withdraw amount: ",amount)
        if amount<=balance:
            balance-=amount
            print("Now your current balance:",balance)
        else:
            print("Your amount is not sufficient")

    def change_pin():
        global pin
        old_pin=int(input("Enter your old pin: "))
        if old_pin==pin:
            new_pin=int(input("Enter your new pin: "))
            pin=new_pin
            print("Change successfully")
        else:
            print("Wrong pin")
    
    if option==1:
        bal()
    elif option==2:
        deposit()
    elif option==3:
        withdraw()
    elif option==4:
        change_pin()
    elif option==5:
        print("Thank you for using ATM 😊")
        break
    
    else:
        print("Invalid option")


#baise isme mene function ko while loop ke andar hi define kiya hai lekin esa hota hai ki function ko loop se phele define kroo phir loop ke andar function ko call kro
