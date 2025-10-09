"""All the functions and variables that are used globally in the file is defined here"""
name = ""
games = ["Speed Typing","Wordle","Paper Scissors Rock"]
files = ["Files\speed_typing_scores.txt","Files\wordle_scores.txt","Files\paper_scissors_rock_scores.txt"]
def set_name(new_name): #Allows the name to be used in all files by using utils.name and it can be set in the main menu.
    global name
    name = new_name.strip()
def replay(message): #Asks the user for replaying the game until the user writes 1 or 0.
    playing = None
    while playing not in [0,1]:
        try:
            playing = int(input(f"\nDo you want to play again? {message} \n 0 : No \n 1 : Yes \n"))
            if playing not in [0,1]:
                raise ValueError
        except ValueError:
            print("Please try again.")
    return (playing)
def overwrite(file,score,index): #Opens a specific file, gets the last line, modifiy it to user's score and rewrite the file with the modification.
    with open(file, 'r') as f:
        leaderboard = f.readlines()
    leaderboard[index] = score
    with open(file,'w') as f:
        f.writelines(leaderboard)
def find_user(leaderboard):
    try:
        for scores in leaderboard:
            if scores.split()[0] == name:
                return(leaderboard.index(scores))
        return(None)
    except:
        return(None)
def check_high_score(file):
    with open (file,'r') as f:
        leaderboard = f.readlines()
    user_index = find_user(leaderboard)
    if user_index == None:
        return (0)
    score = float(leaderboard[user_index].split()[1])
    return(score)
def add_leaderboard(file,score): #Overwrites the user's score into their personal best. 
    name_score = str(name) + " " + str(score) + "\n" #Score take the format "name score\n"
    with open (file,'r') as f:
        leaderboard = f.readlines()
        user_index = find_user(leaderboard)
        if user_index == None: #If the user has no personal score in the file yet, it needs to be newly appended.
            with open(file,'a') as f: #Appends the score into the last line of the file.
                f.write(name_score)
                return()
        overwrite(file,name_score,user_index)
            
def filter_top3(file,reverse_order): #Filters top 3 that is shown on the leaderboard.
    with open(file, 'r') as f:
        leaderboard = f.readlines()
        leaderboard = [lines.strip().split() for lines in leaderboard] #Turns the file into a list of lists which contain [name,score]
        top3 = sorted(leaderboard,key=lambda x: x[1],reverse=reverse_order)[:3]  #Sorts the list based on the score, reverse if speed typing.
        return (top3)
def view_leaderboard(file,game): #Goes over the top 3 for a specific game and prints them in a nice format.
    if game == 0:
        top3 = filter_top3(file,False)
    else:
        top3 = filter_top3(file,True)
    print(f"--- {games[game]} ---")
    for score in top3:
        print(" : ".join(score))
    return()
