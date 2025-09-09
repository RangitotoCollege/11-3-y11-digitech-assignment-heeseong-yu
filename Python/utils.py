name = None
def set_name(new_name):
    global name
    name = new_name
def replay(message):
    playing = None
    while playing != 0 and playing != 1:
        try:
            playing = int(input(f"\nDo you want to play again? {message} \n 0 : No \n 1 : Yes \n"))
            if playing != 0 and playing != 1:
                raise ValueError
        except ValueError:
            print("Please try again.")
    return (playing)
def add_leaderboard(line,score):
    with open('leaderboard.txt', 'r') as leaderboard:
        modified_leaderboard = leaderboard.readlines()
        print(modified_leaderboard)
        modified_leaderboard[line] = score + "\n"
    with open('leaderboard.txt', 'w') as leaderboard:
        leaderboard.writelines(modified_leaderboard)
