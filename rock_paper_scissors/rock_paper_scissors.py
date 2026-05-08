"""
Rock Paper Scissors - A simple CLI game.

Player plays against the computer. Best of 3 with score tracking.
Input is validated and normalised (lowercase + trimmed whitespace).
"""

import random

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while user_score < 2 and computer_score < 2:

    user_choice = input("Choose rock/paper/scissors: ").strip().lower()

    while user_choice not in options:
        print("Invalid choice. Please type rock, paper, or scissors.")
        user_choice = input("Choose rock/paper/scissors: ").strip().lower()
    computer_choice = random.choice(options)

    print(f"You chose: {user_choice}")  
    print(f"Computer chose: {computer_choice}")  

    if user_choice == computer_choice:
        print("Tie!")
    elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1


    print(f"Score → You: {user_score}, Computer: {computer_score}")
print()

if user_score >= 2:
    print("You won the match!")
else:
    print("Computer won the match!")
