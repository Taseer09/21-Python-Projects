import random

MIN_AMOUNT = 10
MAX_LINES = 3
MIN_BET = 2
MAX_BET = 100
symbols = ['Cherry', 'Banana', 'Apple', 'Orange', 'Grapes']
weights = [0.4, 0.4, 0.1, 0.1, 0.05]

def amount_to_deposit():
    while True:
        amount = input("How much $ you want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount < MIN_AMOUNT:
                print(f"Please Enter amount greater than {MIN_AMOUNT}")
            else:
                return amount
        else:
            print("Invalid Please Type a Number")

def get_lines():
     while True:
        lines = input("Enter the Number of Lines: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Please Enter Lines Between 1-{MAX_LINES}")
        else:
            print("Invalid Please Type a Number")

def how_much():
     while True:
        amount = input("Enter the amount to Bet: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: 
                return amount
            else:
                print(f"Please Enter amount Greater than -{MIN_BET}")
        else:
            print("Invalid Please Type a Number")

def spin_slot_machine():
    return random.choices(symbols, weights=weights, k=3)

def display_result(result):
    # Display the result of the spin
    print("\n=== Slot Machine ===")
    print("  |  ".join(result))
    print("===================")

def calculate_payout(result, bet):
    # Calculate the payout based on the result
    if len(set(result)) == 1:  # All symbols are the same
        payout_multiplier = 10
    elif len(set(result)) == 2:  # Two symbols are the same
        payout_multiplier = 5
    else:
        payout_multiplier = 0

    payout = bet * payout_multiplier
    return payout

def main():
    balance = amount_to_deposit()
    lines = get_lines()
    while True:
        bet = how_much()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You have insufficient funds to bet. Your Total Balance is ${balance}. Spend accordingly.")
        else:
            break

    print(f'You are Betting ${bet} on {lines} Lines. Your total bet is ${total_bet}') 
    result = spin_slot_machine()
    display_result(result)
    payout = calculate_payout(result, bet)
    print(f"Payout: ${payout}")

if __name__ == "__main__":
    main()
