import random

print("Let's Play Rock, Paper, Scissors, Lizard, Spock!")
player = input("Enter a choice (rock, paper, scissors, lizzard, spock): ")
choices = ["rock", "paper", "scissors", "lizzard", "spock"]

game_map = {0:"rock", 1:"paper", 2:"scissors", 3:"lizard", 4:"Spock"}
rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]


print(f"\nYou chose {user_choice}, computer chose {computer_action}.\n")

player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
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
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

