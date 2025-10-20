"""11DGT Python games compendium assessment.

Contains text-based games which are:
Speed Typing, Wordle and Paper, Scissors, Rock.
Each game has a leaderboard system that can be seen. This is the main menu.
"""
# Imports functions from different Python files.
import speed_typing
import wordle
import paper_scissors_rock
import utils


def main_menu():
    """Run the main menu."""
    action = 0
    print("=== Name setting ===\n")
    # To prevent bugs, only 1 and 20 characters is accepted as a name.
    while len(utils.name) == 0 or len(utils.name) > 20:
        print("Name should be between 1 to 20 letters.")
        # Save the name in the utils file where it can be used across all files.
        utils.set_name(input("What is your name? "))
    print(f"Welcome to Games Compendium, {utils.name}!")
    # Until the user wants to exit, they can keep playing the game.
    while action != 5:
        try:
            action = int(input("\n=== Main Menu ==="
                               "\nWhat do you wish to do?"
                               "\n1 : Speed Typing"
                               "\n2 : Wordle"
                               "\n3 : Paper Scissors Rock"
                               "\n4 : Leaderboard,"
                               "\n5 : Exit\n"))
            if action == 1:
                speed_typing.play()
            elif action == 2:
                wordle.play()
            elif action == 3:
                paper_scissors_rock.play()
            elif action == 4:
                print("=== Leaderboard ===")
                # Loops over all games.
                # Then prints the corresponding top 3 leaderboard for each.
                for i in range(len(utils.games)):
                    utils.print_leaderboard(i)
            elif action == 5:
                print("Thank you for playing!")
        # If action is not any of the options, it asks the user to try again.
            else:
                raise ValueError
        except ValueError:
            print("Please try again.")


# Allows the game to only run when it is executed on this file directly.
if __name__ == "__main__":
    main_menu()
