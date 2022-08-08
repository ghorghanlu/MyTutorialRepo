# Random password generator

"""
To create a program that takes a number and generate a random password length of that number.

Topics: random module, joining strings, taking input

Hint: Create a string with all characters, then take random characters from it and concatenate each char to make a big string.

import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p =  "".join(random.sample(s,passlen ))
print (p)
"""

import random
X = "0123456789abchdefghijklmnopqrstuvwxyzABCHDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+[]{}\|;:‘“,./<>?"
Y = int(input("Enter the length of the password you want: "))
Pass = ""
while len(Pass) < Y:
    R = (random.choice(X))
    Pass += R
print(Pass)
