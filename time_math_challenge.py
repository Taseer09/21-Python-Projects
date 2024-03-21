import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression,answer

TOTAL_PROBLEMS = 5
start_time = time.time()


wrong = 0


while True:
    playing = input("Do you want to play more press <q> to quit and <p> to play ").lower()
    if playing == "q":
        quit()
    for i in range(TOTAL_PROBLEMS):
        expression, answer = generate_problem()

        while True:
            guess = input("Problem #" + str(i+1) + ": " + expression + " = ")
            if guess == str(answer):
                break
            wrong += 1 
    end_time = time.time()

    total_time = end_time - start_time
    print("Your Finished it in :", total_time)