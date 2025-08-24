"""11DGT Python games compendium assessment. Contains text based games which includes speed typing, wordle and paper scissors rock. 
Each game has a leaderboard system that can be seen."""
action = 0
name = input("What is your name? ")
print(f"Welcome to Games Conpendium, {name}!")
while action != "exit": #Keep taking inputs and allows the user to take the following action. The user can keep playing as much as they want.
    try:
        action = int(input("What do you wish to do? \n 1 : speed typing \n 2 : wordle \n 3 : paper scissors rock \n 4 : leaderboard, \n 5 : exit \n"))
    
        if action == 1:
            print("play speed typing")
            continue
        elif action == 2:
            print("play wordle")
            continue
        elif action == 3:
            print("play paper scissors rock")
            continue
        elif action == 4:
            print("show leaderboard")
            continue
        elif action == 5:
            print("Thank you for playing!")
            break
        else:
            raise ValueError
    except ValueError:
        print("Please try again.")
        continue