print("------CONTACT BOOK------")
contacts=[]
while True:
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Exit")
    option=int(input("choose the option: "))
    if option==1:
        print("---ADD CONTACT---")
        while True:
            
            name=input("Enter your name: ")
            number=int(input("Enter your phone number: "))
            contact={
            "full_name":name,
            "no":number,
            }
            contacts.append(contact)
            ques=input("do you want to add more?: ")
            if ques=="yes":
                continue
            elif ques=="no":
                 break
            else:
                print("please select only yes or no")
    elif  option==2:
        print("---VIEW CONTACT---")    
        for contact in contacts:
            print(contact["full_name"],"->",contact["no"])
    elif option==3:
        print("---SEARCH CONTACT---")
        search=input("Enter the name: ")
        found=False
        for contact in contacts:
            if search==contact["full_name"]:
                print("Contact found")
                print("Contact name",contact["full_name"],"->","Contact number",contact["no"])
                found=True
        if found==False:
            print("This contact is not available")
    elif option==4:
        print("---DELETE CONTACT---")
        found=False
        delete=input("Enter the name: ")
        for contact in contacts:
            if delete==contact["full_name"]:
                contacts.remove(contact)
                found=True
                print("Contact delete successfully")
                break
        if found==False:
            print("This contact is not available")
    elif option==5:
         print("Thankyou for using Contact Book😊")
         break
    else:
        print("Invalid option")


"""andar wala if = individual item ko check karna.
2. Bahar wala if kab?
Ye tab lagta hai jab tumhe poori list check hone ke baad koi decision lena ho"""