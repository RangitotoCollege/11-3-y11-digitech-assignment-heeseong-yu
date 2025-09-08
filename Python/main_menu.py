"""11DGT Python games compendium assessment. Contains text-based games which include speed typing, Wordle and paper, scissors, rock. 
Each game has a leaderboard system that can be seen."""
import speed_typing
import wordle
import paper_scissors_rock
import utils

action = 0   #Placeholder variables and word lists that are used later in the code
fastest_time_record = (999999, "No one")
highest_wordle_streak = (0, "No one")
highest_paper_scissors_rock_streak = (0, "No one")
#Different functions for different games

name = input("What is your name? ")
print(f"Welcome to Games Conpendium, {name}!")
while action != "exit": #Keep taking inputs and allow the user to take the following action. The user can keep playing as much as they want.
    try:
        action = int(input("What do you wish to do? \n 1 : speed typing \n 2 : wordle \n 3 : paper scissors rock \n 4 : leaderboard, \n 5 : exit \n"))
    
        if action == 1:
            speed_typing.play()
        elif action == 2:
            wordle.play()
        elif action == 3:
            paper_scissors_rock.play()
        elif action == 4:
            print("show leaderboard")
        elif action == 5:
            print("Thank you for playing!")
            break
        else:
            raise ValueError
    except ValueError: #If action is not any of the options, it asks the user to try again.
        print("Please try again.")
        continue
