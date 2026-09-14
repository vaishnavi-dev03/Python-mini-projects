password=input("Enter your password: ")
length=len(password)
print("Password length: ",length)
if length>=8:
    print("Password at least 8 characters")
else:
    print("Password must contain 8 characters")

uppercase_found=False
lowercase_found=False
digits_found=False
special_found=False
for i in password:
    if i.isupper():
        uppercase_found=True
#i.isupper() says that i is uppercase or not and in this we dont compare with isupper because isupper is not a value its a string method thats why we not use i==isupper() and use i.isupper()

#upper() → character ko UPPERCASE me convert karta hai
#isupper() → check karta hai ki character/string UPPERCASE hai ya nahi

    if i.isdigit():
        digits_found=True
    if i.islower():
        lowercase_found=True
    if not i.isalnum():
        special_found=True
print("Uppercase found",uppercase_found)
print("Lowercase found",lowercase_found)
print("Special characters found",special_found)
print("Digits found",digits_found)

if length >= 8 and uppercase_found and lowercase_found and digits_found and special_found:
    print("Password Strength: STRONG 💪")
elif length >= 8 and uppercase_found and lowercase_found and digits_found:
    print("Password Strength: MEDIUM 🟡")
else:
    print("Password Strength: WEAK 🔴")
