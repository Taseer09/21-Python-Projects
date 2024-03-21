print('Welcome to The Number guessing Game')

#creating a variable for storing in how much range the user wants to guess
guess = int(input("In How Much Range you want to do Guessing "))

import random #here we will used random function to generate random numbers
number = random.randint(0,guess)

number_of_guesses = 0

while True:
    number_of_guesses += 1
    user_guess = int(input("Make a Guess "))

    if user_guess == number:
        print("You got it Correct ")
        break
    elif user_guess > number:
        print("You are above the Number")
    else:
        print("You are below the Number")
        continue
    
print("You got it in", number_of_guesses, "Guesses")