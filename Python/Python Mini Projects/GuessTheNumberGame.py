# Guess the number game

"""
The main goal of the project is to create a program that randomly
select a number in a range then the user has to guess the number.
user has three chances to guess the number if he guess correct then
a message print saying “you guess right “otherwise a negative message prints.

Topics: random module, for loop, f strings
"""

"""
import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break
if user != number:
    print(f"Your guess is incorrect the number is {number}")

"""

# Here, unlike the problem, this number is not chosen randomly

X = 4      # The number to be guessed
T = 0 # Number of guess times. The user can guess up to three times
W = 0 # The number of times the user guessed correctly (Win)


while T < 3:
    Y = int(input("Enter a number between one and ten: ")) # The number that the user must enter (between one and ten)
    while Y not in range(1, 10):
        Y = int(input("The entered number is not within the range(1, 10), please enter again: ")) 

    if X == Y:
        W += 1
        T += 1
    else:
        T += 1
print(f"You won {W} times")