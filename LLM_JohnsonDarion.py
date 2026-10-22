# Cti-110
# LLMLab1
# Darion J
# 10/22/2026

# Create a simple python project using a Largely used AI model

import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    player = input("\nRock, paper, or scissors? (q to quit): ").lower()

    if player == "q":
        break
    if player not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("Tie!")
    elif (player, computer) in [("rock", "scissors"),
                                ("paper", "rock"),
                                ("scissors", "paper")]:
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score - You: {player_score} | Computer: {computer_score}")

print("\nFinal score:")
print(f"You: {player_score} | Computer: {computer_score}")