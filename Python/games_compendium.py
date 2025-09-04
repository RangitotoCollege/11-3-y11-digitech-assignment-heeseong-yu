"""11DGT Python games compendium assessment. Contains text-based games which include speed typing, Wordle and paper, scissors, rock. 
Each game has a leaderboard system that can be seen."""
import time
import random
action = 0   #Placeholder variables and word lists that are used later in the code
fastest_time_record = (999999, "No one")
highest_wordle_streak = (0, "No one")
highest_paper_scissors_rock_streak = (0, "No one")
#Different functions for different games
def speed_typing():
    playing = 1     #Currently the user is playing the game
    global fastest_time_record  #Uses global to allow it to change a value that is outside the function so that it can be used in the leaderboard.
    print(f"Welcome to speed typing {name}! \n Just type 10 words which were randomly chosen correctly without capitalisation as fast as you can. \n Fastest time goes to the leaderboard! Starts in 3 seconds. Good luck!")
    time.sleep(5)  #Allows the user to read the instruction by waiting 5 seconds
    while playing:  #Until the user says they want to exit, it keeps looping the game
        sentence = ""
        for i in range(10):
            with open("common_10000_words.txt") as typing_words_list:
                sentence +=  typing_words_list.read([random.randint(0,9999)]) + " "  #Creates a sentence by getting a random word from 1000 words list and adding it 10 times to a blank string
        for i in range(3,0,-1): #Waits 3 seconds before starting
            print(i)
            time.sleep(1)    
        print(f"Type: {sentence}")
        start_time = time.time()
        user_sentence = input("Type: ")
        if user_sentence.strip() == sentence.strip():
            end_time = time.time()
            time_record = round(end_time - start_time,2)  #How fast they typed is calculated by the time the user finished minus the time the user started
            print(time_record, "seconds")
            if time_record < fastest_time_record[0]:  #If the user did faster than the fastest record, it becomes the new fastest record.
                fastest_time_record = (time_record,name)
                print(f"New high record! {name} : {time_record} seconds")
        else:
            print("Incorrect sentence.")
        playing = None
        while playing != 0 and playing != 1:  #Until the user inputs to play again or exit, it keeps asking if they want to play again.
            try:
                playing = int(input("Do you want to play again? \n 0 : No \n 1 : Yes \n"))
                if playing != 0 and playing != 1:
                    raise ValueError
            except ValueError:
                print("Please try again.")
    return
def wordle():
    playing = 1 
    global highest_wordle_streak
    streak = 0
    #Similar overall structure as speed_typing
    print(f" Welcome to Wordle {name}! \n Guess a random 5-letter English word in 6 tries. Unfortunately, not all words are included. \n If your try contains the correct letter at the correct place, it will be printed GREEN \n Correct letter but at the wrong place YELLOW \n Incorrect letter RED. \n You can keep playing to increase your win streak, and the highest streak goes in the leaderboard. \n Good luck!")  
    while playing: 
        tries = 6  #The user has 6 guesses of words.
        word = wordle_words_list[random.randint(0,len(wordle_words_list)-1)]  #Gets a random word from the 5-letter word list
        while tries != 0:  #Until the user uses all guesses, it repeats asking the user to input a guess.
            guess_hint = []  
            guess = input("\n Guess : ")
            if guess.lower().strip() in wordle_words_list:  #If the guess is in the possible solutions, it allows the guess.
                tries -= 1
                for i in range(5):  #Goes over the word to check if it is in the right place, in the wrong place, or not at all and appends the corresponding colour in order.
                   if guess.lower()[i] == word[i]:
                       guess_hint.append("GREEN")
                   elif guess.lower()[i] in word:
                       guess_hint.append("YELLOW")
                   else:
                       guess_hint.append("RED")
            else: #If the guess is invalid, it goes back to asking a guess.
                print("Invalid word.")
                continue
            for colours in guess_hint:  #Prints out to the user what letter is in which state and how many tries they have left.
                print(colours,end = " ")
            print(f"\n{tries} tries left.")
            if guess == word:  #If the user correctly guesses the word, it increases their streak and ends the game.
                print("Correct!")
                streak += 1
                print(f"You have got {streak} correct answers in a row!")
                if streak > highest_wordle_streak[0]: 
                    highest_wordle_streak = (streak,name)
                    print(f"New high record! {name} : {streak} correct answers in a row!")
                    tries = 6  #To prevent guessing correctly on the last try, printing that you didn't get it, tries resets to 6.
                    break
        if tries <= 0: #If the game ends without the user guessing it correctly, the streak resets and the word is revealed.
            print(f"Unfortunate, the answer was: {word}.")
            streak = 0
        playing = None
        while playing != 0 and playing != 1:
            try:
                playing = int(input("Do you want to play again? (STREAK ENDS IF YOU EXIT) \n 0 : No \n 1 : Yes \n"))
                if playing != 0 and playing != 1:
                    raise ValueError
            except ValueError:
                print("Please try again.")
    return
def paper_scissors_rock():
    #Similar overall structure to other games.
    playing = 1 
    global highest_paper_scissors_rock_streak
    streak = 0
    #A set of rules is created to determine who wins.
    rules = {
  ('scissors', 'paper'): 'scissors',
  ('paper', 'rock'): 'paper',
  ('rock', 'scissors'): 'rock',
}
    #The list keeps track of what hand the user has played until now. 
    hands_frequency = ["paper", "scissors", "rock"]
    print(f"Welcome to paper scissors rock {name}! \n Simple game where scissors win paper, paper wins rock and rock wins scissors.\n Same hand is a tie. \n You can keep winning against a computer to increase your win streak, and the highest streak goes in the leaderboard. \n Good luck!")
    while playing: 
        if random.randint(1,10) == 10:  #Once in a while, it randomly resets the user frequency to prevent the user from overloading with one hand and then spamming another hand.
            hands_frequency = ["paper", "scissors", "rock"]
        winning_hands_frequency = []  #From what user did, it creates a list for the computer to choose from by inverting the list with hands that win it.
        for hands in hands_frequency:
            if hands == "paper":
                winning_hands_frequency.append("scissors")
            elif hands == "scissors":
                winning_hands_frequency.append("rock")
            elif hands == "rock":
                winning_hands_frequency.append("paper")
        computer_hand = winning_hands_frequency[random.randint(0,len(winning_hands_frequency)-1)]
        user_hand = None
        while user_hand not in hands_frequency: #Until the user gives a valid input, it repeats asking what hand they want to play.
            try:
                user_hand = input("What hand? \n 0 : Paper \n 1 : Scissors \n 2 : Rock \n")
                if int(user_hand) > 2:  #User hand above 2 is created by the user, so avoid confusion, it raises a value error.
                    raise ValueError
                user_hand = hands_frequency[int(user_hand)]
            except ValueError:
                user_hand = user_hand.lower().strip() 
                if user_hand == hands_frequency[0] or user_hand == hands_frequency[1] or user_hand == hands_frequency[2]:  #If the user wrote the hand itself, it still accepts it
                    break
                print("Invalid input.")
        hands_frequency.append(user_hand)  #The hand user did is appended to the list for the computer to use the winning hand more frequently, as explained above.
        winner = rules.get((computer_hand, user_hand), rules.get((user_hand, computer_hand), 'tie')) #From the rules, it determines who wins or if it's a tie.
        time.sleep(1) #Just a delay to prvent user from spamming.
        print(f"Computer: {computer_hand}  You: {user_hand}")
        if winner == user_hand: #Winning and losing message and streak, and highest streak system.
            print(f"{name} won!")
            streak += 1
            print(f"You have won {streak} games in a row!")
            if streak > highest_paper_scissors_rock_streak[0]: 
                        highest_paper_scissors_rock_streak = (streak,name)
                        print(f"New high record! {name} : {streak} games won in a row!")
        elif winner == computer_hand:
            print(f"Computer won...")
            streak = 0
        else:
            print("It's a tie. You still have your winning streak.")
        playing = None
        while playing != 0 and playing != 1: #Same replay system
            try:
                playing = int(input("Do you want to play again? (STREAK ENDS IF YOU EXIT) \n 0 : No \n 1 : Yes \n"))
                if playing != 0 and playing != 1:
                    raise ValueError
            except ValueError:
                    print("Please try again.")
    return
name = input("What is your name? ")
print(f"Welcome to Games Conpendium, {name}!")
while action != "exit": #Keep taking inputs and allow the user to take the following action. The user can keep playing as much as they want.
    try:
        action = int(input("What do you wish to do? \n 1 : speed typing \n 2 : wordle \n 3 : paper scissors rock \n 4 : leaderboard, \n 5 : exit \n"))
    
        if action == 1:
            speed_typing()
            continue
        elif action == 2:
            wordle()
            continue
        elif action == 3:
            paper_scissors_rock()
            continue
        elif action == 4:
            print("show leaderboard")
            continue
        elif action == 5:
            print("Thank you for playing!")
            break
        else:
            raise ValueError
    except ValueError: #If action is not any of the options, it asks the user to try again.
        print("Please try again.")
        continue
