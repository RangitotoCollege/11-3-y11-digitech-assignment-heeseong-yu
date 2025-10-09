"""11DGT Python games compendium assessment. Contains text-based games which include speed typing, Wordle and paper, scissors, rock. 
Each game has a leaderboard system that can be seen. This is the main menu."""
import speed_typing
import wordle
import paper_scissors_rock
import utils
def main_menu():
    action = 0 
    print("=== Name setting ===\n")
    while len(utils.name) == 0 or len(utils.name) > 20:   #Until the user inputs a name between 1 to 20 letters it keeps asking for the name.
        print("Name should be between 1 to 20 letters.")
        utils.set_name(input("What is your name? "))
    print(f"Welcome to Games Conpendium, {utils.name}!")
    while action != "exit": #Keep taking inputs and allow the user to take the following action. The user can keep playing as much as they want.
        try:
            action = int(input("\n === Main Menu === \n What do you wish to do? \n 1 : speed typing \n 2 : wordle \n 3 : paper scissors rock \n 4 : leaderboard, \n 5 : exit \n"))
            if action == 1:
                speed_typing.play()
            elif action == 2:
                wordle.play()
            elif action == 3:
                paper_scissors_rock.play()
            elif action == 4:
                print("=== Leaderboard ===")
                for i in range(len(utils.files)): #Loops over all files for all games for each leaderboard viewing.
                    utils.view_leaderboard(utils.files[i],i)
            elif action == 5:
                print("Thank you for playing!")
                break
            else:
                raise ValueError
        except ValueError: #If action is not any of the options, it asks the user to try again.
            print("Please try again.")
if __name__ == "__main__": #Allows the game to only run when it is executed on this file directly.
    main_menu()
