name = "User"
games = ["Speed Typing","Wordle","Paper Scissors Rock"]
def set_name(new_name):
    global name
    name = new_name.strip()
def replay(message):
    playing = None
    while playing not in [0,1]:
        try:
            playing = int(input(f"\nDo you want to play again? {message} \n 0 : No \n 1 : Yes \n"))
            if playing not in [0,1]:
                raise ValueError
        except ValueError:
            print("Please try again.")
    return (playing)
def add_leaderboard(file,score):
    with open(file, 'a') as f:
        f.write(f"{name} {score}\n")
def filter_top3(file):
    with open(file, 'r') as f:
        leaderboard = f.readlines()
        leaderboard = [lines.strip().split() for lines in leaderboard]
        top3 = sorted(leaderboard,key=lambda x: x[1],reverse=True)[:3]
        return (top3)
def view_leaderboard(file,game):
    print("=== Leaderboard ===")
    top3 = filter_top3(file)
    print(f"--- {game} ---")
    for score in top3:
        print(" : ".join(score))
    return()
