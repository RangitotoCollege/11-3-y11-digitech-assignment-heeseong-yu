"""11DGT Python games compendium assessment. Contains text-based games which include speed typing, Wordle and paper, scissors, rock. 
Each game has a leaderboard system that can be seen. This is the main menu."""
#Imports function from different Python files.
import speed_typing
import wordle
import paper_scissors_rock
import utils
def main_menu():
    action = 0 
    print("=== Name setting ===\n")
    #To prevent bugs, until the user inputs a name between 1 to 20 letters it repeats asking for the name.
    while len(utils.name) == 0 or len(utils.name) > 20:
        print("Name should be between 1 to 20 letters.")
        #Saves the name in utils file where it can be used across all files.
        utils.set_name(input("What is your name? "))
    print(f"Welcome to Games Conpendium, {utils.name}!")
    #Until the user wants to exit, they can keep playing the game.
    while action != 5: 
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
                #Loops over all games and corresponding files and prints the corresponding top 3 leaderboard.
                for i in range(len(utils.games)):
                    utils.view_leaderboard(utils.files[i],i)
            elif action == 5:
                print("Thank you for playing!")
        #If action is not any of the options, it asks the user to try again.    
            else:
                raise ValueError
        except ValueError: 
            print("Please try again.")
#Allows the game to only run when it is executed on this file directly.
if __name__ == "__main__": 
    main_menu()
