

import random

def winner(player_choice, computer_choice):
    if player == computer:
        return "It's a tie!"
    elif (player == "stone" and computer == "scissors") or \
         (player == "paper" and computer == "stone") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

choices = ["stone", "paper", "scissors"]

# print("Welcome to the Stone-Paper-Scissors game!")
while True:
    player = input("stone, paper, or scissors (or 'quit' to quit): ").lower()

    if player == 'quit':
        break

    if player not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chooses: {computer}")

    result = winner(player, computer)
    print(result)

print("Thanks for playing!")
