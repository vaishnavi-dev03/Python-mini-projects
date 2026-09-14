print("-----EXPENSE TRACKER-----")
expenses=[]
while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Highest Expense")
    print("5. Exit")
    option=int(input("Enter your choice: "))

    if option==1:

        print("----ADD EXPENSE---")
        while True:
            expense_name=input("Enter expense name: ")
            expense_amount=int(input("Enter expense amount: "))
            expense={
            "name":expense_name,
            "amount":expense_amount,
            }
            expenses.append(expense)
            ques=input("Do you want to add more: ")
            if ques == "no":
                break
            elif ques == "yes":
                continue
            else:
                print("Please enter only yes or no")
        print(expenses)

    elif option==2:

        print("-----VIEW EXPENSE-----")
        for expense in expenses:
            print(expense["name"] ,"->",expense["amount"])

    elif option==3:

        print("----TOTAL EXPENSE----")
        total=0
        for expense in expenses:
            total+=expense["amount"]
        print("Total expense: ",total)

    elif option==4:

        print("----HIGHEST EXPENSE----")
        highest=0
        highest_name=""
        for expense in expenses:
            if expense["amount"]>highest:
                highest=expense["amount"]
                highest_name=expense["name"]

        print("Highest Expense",highest_name,"->",highest)

    elif option==5:

        print("Thank you for using Expense Tracker 😊")
        break 
    else:
        print("Invalid option")