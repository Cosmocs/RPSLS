import random

while True:
    user_choice = input("Enter a choice (rock, paper, scissors, lizzard, spock): ")

    choices = ["rock", "paper", "scissors", "lzzard", "spock"]
    computer_action = random.choice(choices)
