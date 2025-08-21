"""11DGT Python games compendium assessment. Contains text based games which includes speed typing, wordle and paper scissors rock. 
Each game has a leaderboard system that can be seen."""
action = 0
print("Welcome to Games Conpendium!")
name = input("What is your name? ")
while action != "exit":
    action = input("What do you wish to do? (speed typing, wordle, paper scissors rock, leaderboard, exit): ").strip().lower()
    if action == "speed typing":
        print("play speed typing")
        continue
    elif action == "wordle":
        print("play wordle")
        continue
    elif action == "paper scissors rock":
        print("play paper scissors rock")
        continue
    elif action == "leaderboard":
        print("show leaderboard")
        continue
    elif action == "exit":
        print("Thank you for playing!")
        break
    else:
        print("Please try again.")
