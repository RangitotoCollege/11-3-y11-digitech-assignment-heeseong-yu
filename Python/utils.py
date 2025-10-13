"""File storing useful tools used in all of the files.

 All the functions and variables that are used globally are defined here.
 """
name = "name"
games = ["Speed Typing",
         "Wordle",
         "Paper Scissors Rock"]
files = ["Files\speed_typing_scores.txt",
         "Files\wordle_scores.txt",
         "Files\paper_scissors_rock_scores.txt"]


def set_name(new_name):
    """Set the name of the user globally in this file."""
    global name
    name = new_name.strip()


def replay(extra_message):
    """Ask the user if they want to replay the same game.

    Extra message can be added for each game.
    Loops until user writes 1 (yes) or 0 (no).
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


def find_user(leaderboard):
    """Return the index of the user in the score file."""
    for scores in leaderboard:
        if scores.split()[0] == name:
            return(leaderboard.index(scores))
    return(None)


def check_high_score(file):
    """Return the highest score of the user."""
    with open (file, 'r') as f:
        leaderboard = f.readlines()
    user_index = find_user(leaderboard)
    if user_index is None:
        return (0)
    score = float(leaderboard[user_index].split()[1])
    return(score)


def add_leaderboard(file, score):
    r"""Overwrite the user's new high score into their previous high score.

    Score takes the format "name score\n"
    If the user has no high score yet, it's newly appended to the last line.
    """
    name_score = str(name) + " " + str(score) + "\n"
    with open(file, 'r') as f:
        leaderboard = f.readlines()
    user_index = find_user(leaderboard)
    if user_index is None:
        with open(file, 'a') as f:
            f.write(name_score)
            return()
    overwrite(file, name_score, user_index)


def filter_top3(file, reverse_order):
    """Returns the top 3 scores in the file.

    Turns the file into a list of tuples which contain (name,score)
    Sorts the list based on the score, reverse if speed typing.
    """
    with open(file, 'r') as f:
        leaderboard = f.readlines()
    leaderboard = [tuple(lines.strip().split()) for lines in leaderboard]
    top3 = sorted(leaderboard, key=lambda x: x[1], reverse=reverse_order)[:3]
    return (top3)


def view_leaderboard(file,game):
    """Go over the top 3 for a specific game and print in a nice format.

    The order is reversed for speed typing as the faster the better.
    """
    if game == 0:
        top3 = filter_top3(file, False)
    else:
        top3 = filter_top3(file, True)
    print(f"--- {games[game]} ---")
    for score in top3:
        print(" : ".join(score))
    return()
