"""File storing useful tools used in all of the files.

All the functions and variables that are used globally are defined here.
"""
name = ""
games = ["Speed Typing",
         "Wordle",
         "Paper Scissors Rock"]
files = ["Files\\speed_typing_scores.txt",
         "Files\\wordle_scores.txt",
         "Files\\paper_scissors_rock_scores.txt"]


def set_name(new_name):
    """Set the name of the user globally in this file."""
    global name
    # Delete the leading and following spaces.
    # After, replace the space in between to "-"" to prevent bugs.   
    name = new_name.strip().replace(" ", "-")


def replay(extra_message):
    """Ask the user if they want to replay the same game.

    Extra messages can be added for each game.
    Loops until the user writes 1 (yes) or 0 (no).
    """
    playing = None
    while playing not in [0, 1]:
        try:
            playing = int(input(f"\nDo you want to play again? {extra_message}"
                                "\n0 : No"
                                "\n1 : Yes\n"))
            if playing not in [0, 1]:
                raise ValueError
        except ValueError:
            print("Please try again.")
    return (playing)


def overwrite(file, score, index):
    """Modify the file with a score in the specific index of the file."""
    with open(file, 'r') as f:
        leaderboard = f.readlines()
    leaderboard[index] = score
    with open(file, 'w') as f:
        f.writelines(leaderboard)


def get_user_index(leaderboard):
    """Return the index of the user in the score file."""
    try:
        for scores in leaderboard:
            if scores.split()[0] == name:
                return (leaderboard.index(scores))
        return (None)
    except IndexError:
        return (None)


def get_user_high_score(file):
    """Return the highest score of the user."""
    with open(file, 'r') as f:
        leaderboard = f.readlines()
    user_index = get_user_index(leaderboard)
    if user_index is None:
        return (0)
    score = float(leaderboard[user_index].split()[1])
    return (score)


def add_leaderboard(file, score):
    r"""Add the user's score in a specific game into the leaderboard.

    Score takes the format "name score\n".
    If the user has a previous high score, overwrite it with their new best.
    Else, newly append to the last line of the file.
    """
    name_score = str(name) + " " + str(score) + "\n"
    with open(file, 'r') as f:
        leaderboard = f.readlines()
    user_index = get_user_index(leaderboard)
    if user_index is None:
        with open(file, 'a') as f:
            f.write(name_score)
            return ()
    overwrite(file, name_score, user_index)


def filter_top3(file, reverse_order):
    """Return the top 3 scores in the file.

    Turn the file into a list of tuples which contain (name,score)
    Sort the list based on the score, reverse if speed typing.
    """
    with open(file, 'r') as f:
        leaderboard = f.readlines()
    leaderboard = [tuple(lines.strip().split()) for lines in leaderboard]
    # Sort the leaderboard in the wanted order and slice the first 3 elements.
    top3 = sorted(leaderboard, key=lambda x: x[1], reverse=reverse_order)[:3]
    return (top3)


def print_leaderboard(game_number):
    """Go over the top 3 for a specific game and print in a nice format.

    The order is reversed for speed typing as the faster the better.
    """
    if game_number == 0:
        top3 = filter_top3(files[game_number], False)
    else:
        top3 = filter_top3(files[game_number], True)
    print(f"--- {games[game_number]} ---")
    for score in top3:
        print(" : ".join(score))
    return
