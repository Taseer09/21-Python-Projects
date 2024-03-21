
import random

def roll():
    min_value = 1
    max_value = 6
    
    roll = random.randint(min_value, max_value)
    return roll


while True:
    num_of_player = input("Enter the Number of Players between 2-4: ")
    if num_of_player.isdigit():
        num_of_player = int(num_of_player)
        if 2 <=  num_of_player <= 4:
            break
        else:
            print("Must be between 2 to 4 Players")
    else:
        print("Invalid Try again")

max_score = 25
current_score = 0
player_score = [0 for _ in range(num_of_player)]

while True:

    for players_idx in range(num_of_player):
        print("Player number", players_idx + 1 , "Roll has started")
        while True:
            wanna_roll = input("Want to roll (y) ").lower()
            if wanna_roll != "y":
                break
            
            value = roll()
            if value == 6:
                print("You rolled 6 Turn done")
            else:
                current_score += value
                print("You Rolled: ", value)
            
            print("Your Current score is: ", current_score)
    


