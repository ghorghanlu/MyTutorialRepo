import random


list = [1, 2, 3, 4, 5, 6]
while True:
    
    userInput = int(input(" 1. roll the dice     2. exit     "))
    if userInput == 1:
        x = random.choice(list) # random.randint(1,6)
        print(x)
    else:
        break
