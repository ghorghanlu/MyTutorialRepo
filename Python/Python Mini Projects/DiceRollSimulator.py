# Dice roll simulator
"""
The goal is to create a program that will simulate the roll of dice.

Topics: random module, looping, and if-else

Hint: Using a random module generate a random number between 
the range from 1 to 6 when the user wants.
"""

import random

list = [1, 2, 3, 4, 5, 6]

while True:
    userInput = int(input(" 1. roll the dice     2. exit     "))
    if userInput == 1:
        x = random.choice(list) # random.randint(1,6)
        print(x)
    else:
        break
