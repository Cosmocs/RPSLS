import random

player = False

while player == False:
#set player to True
    print("Let's Play Rock, Paper, Scissors, Lizard, Spock!")
    player = input("Enter a choice (rock, paper, scissors, lizzard, spock): ")
    choices = ["rock", "paper", "scissors", "lizzard", "spock"]
    computer_action = random.choice(choices)
    print(f"\nYou chose {user_choice}, computer chose {computer_action}.\n")

    if player == computer_action:
        print("It's a tie!")
    elif player == "Rock":
        if computer_action == "Paper":
            print("You lose!", computer_action, "covers", player)
        else:
            print("You win!", player, "smashes", computer_action)
    elif player == "Paper":
        if computer_action == "Scissors":
            print("You lose!", computer_action, "cut", player)
        else:
            print("You win!", player, "covers", computer_action)
    elif player == "Scissors":
        if computer_action == "Rock":
            print("You lose!", computer_action, "smashes", player)
        else:
            print("You win!", player, "cut", computer_action)
    elif player == "lizzard":
        if computer_action == "spock":
            print("You win!", player, "poisons", computer_action)
        else:
            print("You lose!", computuer_action, "poisons", player)
    elif player == "spock"
        if computer_action == "rock"
            print("You win!", player, "crushes", computer_action)
        else:
             print("You loose!", computer_action, "crushes", player)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    

