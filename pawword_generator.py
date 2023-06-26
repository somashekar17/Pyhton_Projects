import random
import string
import hashlib

lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCEFGHIJKLMNOPQRSTUVWXYZ'
numbers='1234567890'
symbols='!@#$%^&*()_+'

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

string= lower+upper+numbers+symbols
length=16
password="".join(random.sample(string,length))
print("Your Password is",password)

# hashed_password= hash_password(password)
# print("HAshed password:",hashed_password)

with open("passw.txt","a") as file:
    file.write(password+"\n")
