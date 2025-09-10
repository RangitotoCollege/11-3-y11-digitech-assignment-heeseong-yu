name = None
games = ["Speed Typing","Wordle","Paper Scissors Rock"]
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
        modified_leaderboard[line] = score + "\n"
    with open('leaderboard.txt', 'w') as leaderboard:
        leaderboard.writelines(modified_leaderboard)
def open_leaderboard(line):
    stripped_leaderboard = []
    with open('leaderboard.txt', 'r') as leaderboard:
        leaderboard = leaderboard.readlines()
        for lines in leaderboard:
            stripped_leaderboard.append(lines.strip().split())
        return (stripped_leaderboard[line])
def view_leaderboard():
    print("=== Leaderboard ===")
    for i in range(len(games)):
        print(f"{games[i]} - " + " : ".join(open_leaderboard(i)))