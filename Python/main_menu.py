"""11DGT Python games compendium assessment. Contains text-based games which include speed typing, Wordle and paper, scissors, rock. 
Each game has a leaderboard system that can be seen."""
import speed_typing
import wordle
import paper_scissors_rock
import utils


def main_menu():
    action = 0  
    util.set_name(input("What is your name? "))
    print(f"Welcome to Games Conpendium, {utils.name}!")
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
if __name__ == "__main__":
    main_menu()
