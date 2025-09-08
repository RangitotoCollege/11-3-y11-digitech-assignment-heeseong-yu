import random
import utils
def play():
    playing = 1 
    global highest_wordle_streak
    streak = 0
    #Similar overall structure as speed_typing
    print(f" Welcome to Wordle {utils.name}! \n Guess a random 5-letter English word in 6 tries. Unfortunately, not all words are included. \n If your try contains the correct letter at the correct place, it will be printed GREEN \n Correct letter but at the wrong place YELLOW \n Incorrect letter RED. \n You can keep playing to increase your win streak, and the highest streak goes in the leaderboard. \n Good luck!")  
    while playing: 
        tries = 6  #The user has 6 guesses of words.
        wordle_words_list = open("wordle_words.txt") 
        stripped_wordle_words_list = [word.strip() for word in wordle_words_list.readlines()]
        wordle_answers_list = open("wordle_answers.txt")
        stripped_wordle_answers_list = [word.strip() for word in wordle_answers_list.readlines()]  #There is a seperate list for possible answers and possible guesses to make answers easy while making guesses have more freedom.
        word = stripped_wordle_answers_list[random.randint(0,len(stripped_wordle_answers_list)-1)]  #Gets a random word from the 5-letter word list
        while tries != 0:  #Until the user uses all guesses, it repeats asking the user to input a guess.
            guess_hint = []  
            guess = input("\n Guess : ")
            if guess.lower().strip() in stripped_wordle_words_list:  #If the guess is in the possible solutions, it allows the guess.
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
                    highest_wordle_streak = (streak,utils.name)
                    print(f"New high record! {utils.name} : {streak} correct answers in a row!")
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
    wordle_words_list.close() 
    wordle_answers_list.close() 
    return