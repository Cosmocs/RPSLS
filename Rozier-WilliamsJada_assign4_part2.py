import random
player_points = 0
comp_points = 0
rounds = int(input("How many rounds would you like? "))
for i in range(1, rounds):
    print("Let's Play Rock, Paper, Scissors, Lizard, Spock!")
   
    player = input("Enter a choice (rock, paper, scissors, lizzard, spock): ")
    choices = ["rock", "paper", "scissors", "lizzard", "spock"]
    computer_action = random.choice(choices)
    print(f"\nYou chose {player}, computer chose {computer_action}.\n")

    if player == computer_action:
        print("It's a tie!")
    elif player == "Rock":
        if computer_action == "Paper":
            print("You lose!", computer_action, "covers", player)
            comp_points += 1
        else:
            print("You win!", player, "smashes", computer_action)
            player_points += 1
    elif player == "Paper":
        if computer_action == "Scissors":
            print("You lose!", computer_action, "cut", player)
            comp_points += 1
        elif computer_action == "rock":
            print("You win!", player, "cuts", computer_action)
            player_points += 1
    elif player == "Scissors":
        if computer_action == "Rock":
            print("You lose!", computer_action, "smashes", player)
            comp_points += 1
        elif computer_action == "paper":
            print("You win!", player, "cut", computer_action)
            player_points += 1
    elif player == "lizzard":
        if computer_action == "spock":
            print("You win!", player, "poisons", computer_action)
            player_points += 1
        else:
            print("You lose!", computuer_action, "poisons", player)
            comp_points += 1
    elif player == "spock":
        if computer_action == "rock":
            print("You win!", player, "crushes", computer_action)
            player_points += 1
        else:
             print("You lose!", computer_action, "crushes", player)
             comp_points += 1
    else:
        print("That's not a valid play. Check your spelling!")
  
    

