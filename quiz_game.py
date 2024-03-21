print("Welcome to the compute based quiz")

# Taking input that whether the user want to play or not

playing = input("Do you want to play? ")

# Now using if statements so if the user says yes the progoram will continue other wise quits
if playing.lower() != 'yes':
    quit()
print("Okay lets start..")

# Now lets give some questions to the user

print("What does the CPU stand for ")
score = 0
answer = input()
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 1
else: #if the user answer is incorrect it will print incorrect as we are using else statement
    print("Incorrect")

print("What does the GPU stand for ")
answer = input()
if answer.lower() == 'graphic processing unit':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("What does the PSU stand for ")
answer = input()
if answer.lower() == 'power supply unit':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("What does the RAM stand for ")
answer = input()
if answer.lower() == 'random acess memory':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("What does the ROM stand for ")
answer = input()
if answer.lower() == 'read only memory':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print('Your total score is ' + str(score))
print("You got " , (score/5) * 100 , "%") 