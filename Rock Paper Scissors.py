import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock":
            if computer_pick == "rock":
                print("Tie!")
            elif computer_pick == "scissors":
                print("You win!")
                user_wins+=1
            else:
                print("You Lost!")
                computer_wins+=1

    elif user_input == "paper":
        if computer_pick == "paper":
            print("Tie!")
        elif computer_pick == "rock":
            print("You win!")
            user_wins += 1
        else:
            print("You lost!")
            computer_wins+=1

    elif user_input == "scissors":
        if computer_pick == "scissors":
            print("Tie")
        elif computer_pick == "paper":
            print("You Win!")
            user_wins+=1
        else:
            print("You Lost!")
            computer_wins+=1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
