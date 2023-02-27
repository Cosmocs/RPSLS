import random
player_points = 0
comp_points = 0
rounds = int(input("How many rounds would you like? "))
for i in range(1, rounds):
    print("Let's Play Rock, Paper, Scissors, Lizard, Spock!")
   
    player = input("Enter a choice (rock, paper, scissors, lizzard, spock): ")
    choices = ["rock", "paper", "scissors", "lizzard", "spock"]
    comp = random.choice(choices)
    print(f"\nYou chose {player}, computer chose {computer_action}.\n")

    if player == comp:
        print("It's a tie!")
    elif player == "spock":
        if comp == "lizzard":
            print("You Lose!", comp, "poisons", player)
            comp_points += 1
    elif comp == "spock":
        if player == "lizzard":
            print("You Win!", player, "poisons", comp)
            player_points += 1
    elif comp == "lizzard":
        if player == "rock":
            print("You Win!", player, "crushes", comp)
            player_points += 1
    elif player == "lizzard":
        if comp == "rock":
            print("You Lose!", comp, "crushes", player)
            comp_points +=
    elif comp == "spock"
        if player == "paper":
            print("You Win!", player, "disapproves", comp)
            player_points += 1
    elif player == "spock"
        if comp == "paper":
            print("You Lose!", comp, "disapproves", player)
            comp_points += 1
    elif player == "rock"
        if comp == "paper":
            print("You Lose!", comp, "covers", player)
            comp_points += 1
    elif comp == "rock"
        if player == "paper":
            print("You Win!", player, "covers", comp)
            comp_points += 1    
    
        
    else:
        print("That's not a valid play. Check your spelling!")
  
    

