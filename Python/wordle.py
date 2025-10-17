"""A game of Wordle."""
import random
import utils


def play():
    """Run the Wordle game."""
    streak = 0
    playing = 1
    print("\n=== Wordle ==="
          f"\nWelcome to Wordle {utils.name}!"
          "\nGuess a random 5-letter English word in 6 tries."
          "\nIf your try contains:"
          "\nCorrect letter at the correct place, GREEN,"
          "\nCorrect letter but at the wrong place, YELLOW,"
          "\nIncorrect letter, RED, will be printed accordingly."
          "\nKeep guessing correctly to increase streak and get in the leaderboard."
          "\nType 'quit' or 'exit' to quit the game."
          "\nGood luck!")
    terminator = ["quit", "exit"]
    while playing:
        # The user has 6 guesses of words.
        tries = 6
        # Turn the files into a stripped list.
        # List of possible answers and possible guesses.
        # This increases user freedom while making answers easy enough.
        with open("Files\\wordle_guesses.txt", "r") as f:
            wordle_guesses_list = [word.strip() for word in f.readlines()]
        with open("Files\\wordle_answers.txt", "r") as f:
            wordle_answers_list = [word.strip() for word in f.readlines()]
        # Gets a random word from the 5 letter word list.
        target_word = wordle_answers_list[random.randint(
            0, len(wordle_answers_list) - 1)]
        # Until all guesses are used, repeat asking for a guess.
        while tries != 0:
            match = []
            guess = input("\nGuess : ").lower().strip()
            # End the game if user inputs a terminator.
            if guess in terminator:
                break
            # Guess rejected if it is not an allowed word.
            if guess not in wordle_guesses_list:
                print("Invalid word.")
                continue
            # If the guess is valid, one of the tries is used.
            tries -= 1
            # Go over the character in the word to check.
            # Appends the corresponding colour in order to a list.
            for i in range(5):
                if guess[i] == target_word[i]:
                    match.append("GREEN")
                elif guess[i] in target_word:
                    match.append("YELLOW")
                else:
                    match.append("RED")
            # Print out state of each letter and the remaining tries.
            for colours in match:
                print(colours, end=" ")
            print(f"\n{tries} tries left.")
            # If guess is incorrect, ask a new guess again.
            if guess != target_word:
                # If no guesses remain and the last guess was incorrect,
                # reveal answer and end the game.
                if tries == 0:
                    print(f"Unfortunate, the answer was: {target_word}.")
                    streak = 0
                    break
                continue
            # If the guess is correct, increase streak.
            print("Correct!")
            streak += 1
            print(f"You have got {streak} correct answers in a row!")
            # If the user gets a high score, either append or update,
            # depending on if they had a previous high score.
            if streak > utils.get_user_high_score("Files\\wordle_scores.txt"):
                print(
                    f"New high record! {utils.name} : {streak} correct in a row!")
                utils.add_leaderboard("Files\\wordle_scores.txt", streak)
                break
        # Asks the user for a replay.
        playing = utils.replay("STREAK ENDS IF YOU LEAVE! ")
    return
