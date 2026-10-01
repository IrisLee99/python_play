import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (rock, paper, scissors): ")

print("Computer chose:", computer_choice)

if computer_choice == user_choice:
    print("It's a tie!")
elif (computer_choice == "rock" and user_choice == "scissors") or \
     (computer_choice == "scissors" and user_choice == "paper") or \
     (computer_choice == "paper" and user_choice == "rock"):
    print("Computer wins!")
else:
    print("You win!")