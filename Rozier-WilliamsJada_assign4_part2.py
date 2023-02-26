import random

while True:
    user_choice = input("Enter a choice (rock, paper, scissors, lizzard, spock): ")

    choices = ["rock", "paper", "scissors", "lzzard", "spock"]
    computer_action = random.choice(choices)
    print(f"\nYou chose {user_choice}, computer chose {computer_action}.\n")

    if user_choice == computer_action:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

