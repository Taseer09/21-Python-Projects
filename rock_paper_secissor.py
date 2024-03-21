import random #for generating random numbers

options = ["rock","paper","scissor"]

computer_score = 0
user_score = 0

while True:
    user_input = input("Please type Rock/Paper/Scissor or Q to Quit ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    
    computer_input = random.randint(0,2)
    # 0 = rock, 1 = paper, 2 = scissor

    comp_pick = options[computer_input]
    print("Computer Pick is ",comp_pick)
    

    if user_input == 'rock' and comp_pick == 'scissor':
        print("You won")
        user_score +=1
    
    elif user_input == 'scissor' and comp_pick == 'paper':
        print("You Won")
        user_score +=1

    elif user_input == 'paper' and comp_pick == 'rock':
        print("You Won")
        user_score +=1

    else:
        print("Computer Won")
        computer_score +=1

print("Your Score is: ", user_score)
print("Computer Score is: ", computer_score)

print("Good Bye")
