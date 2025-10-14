"""A game of Speed Typing."""
import random
import time
import utils


def play():
    """Run the speed typing game."""
    playing = 1
    print(
        "\n=== Speed Typing ==="
        f"\nWelcome to speed typing {utils.name}!"
        "\nJust type 10 randomly chosen words correctly as fast as you can."
        "\nUse correct spacing and capitalisation."
        "\nFastest time is saved. Aim to be on the leaderboard!"
        "\nStarts in 3 seconds. Good luck!")
    # Allows the user to read the instruction by waiting 3 seconds
    time.sleep(3)
    while playing:
        print("\n======")
        # Seperates words file into a list and strips every element
        with open("Files\\common_words.txt", "r") as f:
            typing_words_list = [word.strip() for word in f.readlines()]
        # Creates a 10 word sentence by adding random word to a blank string 10
        # times.
        target_sentence = ""
        for i in range(10):
            target_sentence += typing_words_list[random.randint(
                0, len(typing_words_list) - 1)] + " "
        # 3 second countdown before starting.
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        print(f"Type: {target_sentence}")
        start_time = time.time()
        user_sentence = input("Type: ")
        # If the user sentence matches target sentnece, record is calculated.
        if user_sentence.strip() == target_sentence.strip():
            end_time = time.time()
            # Record is calculated by the difference between starting and the
            # ending time.
            time_record = round(end_time - start_time, 2)
            print(time_record, "seconds")
            # If the user has no high scores yet, appends their name and high score.
            # Or if the user their previous high score, updates their high
            # score.
            if utils.check_high_score("Files\\speed_typing_scores.txt") == 0 or (
                    time_record < utils.check_high_score("Files\\speed_typing_scores.txt")):
                print("New Personal High Record!")
                utils.add_leaderboard(
                    "Files\\speed_typing_scores.txt", time_record)
        else:
            print("Incorrect sentence.")
        # Asks for the user to play the game again.
        playing = utils.replay(" ")
    return
