name = ""
personal_fastest_speed_typing = 9999999
personal_highest_wordle_streak = 0
personal_highest_paper_scissors_rock_streak = 0
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
    name_score = str(name) + " " + str(score) + "\n"
    with open (file,'r') as f:
        leaderboard = f.readlines()
    with open(file, 'a') as f:
        if name_score not in leaderboard:
            f.write(name_score)
def filter_top3(file,reverse_order):
    with open(file, 'r') as f:
        leaderboard = f.readlines()
        leaderboard = [lines.strip().split() for lines in leaderboard]
        top3 = sorted(leaderboard,key=lambda x: x[1],reverse=reverse_order)[:3]
        return (top3)
def view_leaderboard(file,game):
    if game == 0:
        top3 = filter_top3(file,False)
    else:
        top3 = filter_top3(file,True)
    print(f"--- {games[game]} ---")
    for score in top3:
        print(" : ".join(score))
    return()
