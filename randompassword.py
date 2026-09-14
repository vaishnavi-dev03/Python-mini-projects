import random
import string
"""val=random.choice([1,2,3,4,5,6,7])
print(val)
print(string.ascii_letters)
print(string.punctuation)
print(string.digits)
"""
pass_length=12
password=""
for i in range(pass_length):
   val=string.ascii_letters+string.digits+string.punctuation
   password+=random.choice(val)
print("Your random password: ",password)
val1=string.ascii_letters+string.digits+string.punctuation
#list chomprehension[function for i in range(n)]
password1="".join([random.choice(val1) for i in range(pass_length)])
print("Your random password is: ",password1)
