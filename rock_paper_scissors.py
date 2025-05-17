import random

options = ["rock", "paper", "scissors"]

def check_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    print("\nRock, Paper, or Scissors? (type 'exit' to quit)")
    player = input("Your choice: ").lower()
    if player == "exit":
        break
    if player not in options:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    print(f"Computer chose: {computer}")
    print(check_winner(player, computer))
