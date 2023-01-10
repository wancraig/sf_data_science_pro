"Game Guess a Number"

import numpy as np

number = np.random.randint(1,101) # generating random number

# amount of attempts
count = 0

while True:
    count+=1
    predict_number = int(input("Guess a number from 1 to 100:"))
    
    if predict_number > number:
        print("Number must be lower!")
        
    elif predict_number < number:
        print("Number has to be higher!")
        
    else:
        print(f"You guessed right! The number is = {number}, for {count} amount of guesses")
        break