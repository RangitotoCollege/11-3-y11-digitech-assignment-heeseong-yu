"""A game of Speed Typing"""
import random
import time
import utils
def play():
    playing = 1
    print(f"\n === Speed Typing === \n Welcome to speed typing {utils.name}! \n Just type 10 words which were randomly chosen correctly without capitalisation as fast as you can. \n Fastest time goes to the leaderboard! Starts in 3 seconds. Good luck!")
    time.sleep(3)  #Allows the user to read the instruction by waiting 3 seconds
    while playing:  #Until the user says they want to exit, it keeps looping the 
        print("\n======")
        with open("Files\common_words.txt","r") as f:
            typing_words_list = [word.strip() for word in f.readlines()] #Seperates them into a list and strips every element in the list to create a list with no line breaks.
        target_sentence = ""
        for i in range(10):
            target_sentence +=  typing_words_list[random.randint(0,len(typing_words_list)-1)] + " "  #Creates a sentence by seperating the file into a list of stripped words and then adding on to a blank string 10 times.
        for i in range(3,0,-1): #Waits 3 seconds before starting
            print(i)
            time.sleep(1)    
        print(f"Type: {target_sentence}")
        start_time = time.time()
        user_sentence = input("Type: ")
        if user_sentence.strip() == target_sentence.strip():
            end_time = time.time()
            time_record = round(end_time - start_time,2)  #How fast they typed is calculated by the time the user finished minus the time the user started
            print(time_record, "seconds")
            if utils.check_high_score("Files\speed_typing_scores.txt") == 0 or (time_record < utils.check_high_score("Files\speed_typing_scores.txt") and time_record != 0):
                print("New Personal High Record!")
                utils.add_leaderboard("Files\speed_typing_scores.txt",time_record)
        else:
            print("Incorrect sentence.")
        playing = utils.replay(" ")
    return