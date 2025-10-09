"""A game of Wordle"""
import random
import utils
def play():
    streak = 0
    playing = 1
    #Similar overall structure as speed_typing
    print(f"\n === Wordle === \n Welcome to Wordle {utils.name}! \n Guess a random 5-letter English word in 6 tries. \n If your try contains: \n Correct letter at the correct place, GREEN \n Correct letter but at the wrong place, YELLOW \n Incorrect letter, RED, will be printed accordingly. \n Keep playing to get the highest win streak and go in the leaderboard. \n Type 'quit' or 'exit' to quit the game. \n Good luck!")  
    terminator = ["quit","exit"]
    while playing: 
        tries = 6  #The user has 6 guesses of words.
        with open("Files\wordle_words.txt","r")  as f:
            wordle_words_list = [word.strip() for word in f.readlines()]
        with open("Files\wordle_answers.txt","r")  as f:
            wordle_answers_list = [word.strip() for word in f.readlines()]  #There is a seperate list for possible answers and possible guesses to make answers easy while making guesses have more freedom.
        target_word = wordle_answers_list[random.randint(0,len(wordle_answers_list)-1)]  #Gets a random word from the 5-letter word list
        while tries != 0:  #Until the user uses all guesses, it repeats asking the user to input a guess.
            match = []  
            guess = input("\nGuess : ").lower().strip()
            if guess in terminator:
                break
            if guess not in wordle_words_list:
                print("Invalid word.")
                continue  #If the guess is in the possible solutions, it allows the guess.           
            tries -= 1
            for i in range(5):  #Goes over the word to check if it is in the right place, in the wrong place, or not at all and appends the corresponding colour in order.
                if guess[i] == target_word[i]:
                    match.append("GREEN")
                elif guess[i] in target_word:
                    match.append("YELLOW")
                else:
                    match.append("RED")
            for colours in match:  #Prints out to the user what letter is in which state and how many tries they have left.
                print(colours,end = " ")
            print(f"\n{tries} tries left.")
            if guess != target_word:  #If the user correctly guesses the word, it increases their streak and ends the game.
                if tries == 0: #If the game ends without the user guessing it correctly, the streak resets and the word is revealed.
                    print(f"Unfortunate, the answer was: {target_word}.")
                    streak = 0
                    break
                continue
            print("Correct!")
            streak += 1
            print(f"You have got {streak} correct answers in a row!")
            if streak > utils.check_high_score("Files\wordle_scores.txt"): 
                print(f"New high record! {utils.name} : {streak} correct answers in a row!")
                utils.add_leaderboard("Files\wordle_scores.txt",streak)
                break           
        playing = utils.replay("STREAK ENDS IF YOU LEAVE! ")
    return
