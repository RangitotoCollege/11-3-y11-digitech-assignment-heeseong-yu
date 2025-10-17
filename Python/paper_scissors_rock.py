"""A game of Paper Scissors Rock."""
import random
import time
import utils


def play():
    """Run the paper scissors rock game."""
    streak = 0
    playing = 1
    # Create a set of rules to determine who wins for each case.
    rules = {
        ('scissors', 'paper'): 'scissors',
        ('paper', 'rock'): 'paper',
        ('rock', 'scissors'): 'rock',
    }
    # List of possible hands.
    hands_list = ["paper", "scissors", "rock"]
    hands_emoji = {"paper": "📃", "scissors": "✂️", "rock": "🪨"}
    # The list keeps track of what hand the user has played until now.
    user_hands_frequency = []
    print(
        "\n=== Paper Scissors Rock ==="
        f"\nWelcome to paper scissors rock {utils.name}!"
        "\nSimple game where scissors win paper, paper wins rock and rock wins scissors."
        "\nSame hand is a tie."
        "\nConsecutively win against a computer to increase your win streak."
        "\nYour highest streak is saved. Aim for top 3 in the leaderboard."
        "\nGood luck!")
    while playing:
        print("\n======")
        # On average of once every 10 games, randomly resets the user frequency.
        # Prevent user from over loading their user frequency with a specific hand,
        # which can lead to computer only using one hand and exploting the system.
        if random.randint(1, 10) == 10:
            user_hands_frequency = []
        # Computer most likely use the hand that beats the user's most frequent hand.
        # By inverting the user hands frequency list with hands that win it.
        # Also adds the base set of hands to give at least one chance for each hand.
        computer_hands_frequency = [] + hands_list
        for hands in user_hands_frequency:
            if hands == "paper":
                computer_hands_frequency.append("scissors")
            elif hands == "scissors":
                computer_hands_frequency.append("rock")
            elif hands == "rock":
                computer_hands_frequency.append("paper")
        # Computer hand is randomly chosen.
        computer_hand = computer_hands_frequency[random.randint(
            0, len(computer_hands_frequency) - 1)]
        user_hand = None
        # Make the user input a valid hand.
        while user_hand not in hands_list:
            try:
                user_hand = input(
                    "Which hand?"
                    "\n0 : Paper"
                    "\n1 : Scissors"
                    "\n2 : Rock\n")
                if int(user_hand) not in [0, 1, 2]:
                    raise ValueError
                user_hand = hands_list[int(user_hand)]
            except ValueError:
                user_hand = user_hand.lower().strip()
                # If the user wrote the hand itself as string accept it.
                if user_hand == "paper" or user_hand == "scissors" or user_hand == "rock":
                    break
                # Else, print invalid input and re-ask.
                print("Invalid input.")
        # The hand user played is appended to the hand frequeny.
        user_hands_frequency.append(user_hand)
        # From the rules, it determines who wins.
        # Check one way then the other way around.
        # If there is no values from checking the winner, return tie.
        winner = rules.get(
            (computer_hand, user_hand), rules.get(
                (user_hand, computer_hand), 'tie'))
        # Delay to prevent user from spamming and give dramatic effect.
        time.sleep(0.5)
        print(f"{utils.name}: {user_hand}{hands_emoji[user_hand]}")
        time.sleep(0.5)
        print(f"Computer: {computer_hand}{hands_emoji[computer_hand]}")
        time.sleep(0.5)
        # If user wins, increase streak.
        if winner == user_hand:
            print(f"{utils.name} won!")
            streak += 1
            print(f"You have won {streak} games in a row!")
            # If user gets a high score, either append or update,
            # depending on if they had a previous high score.
            if streak > utils.get_user_high_score(
                    "Files\\paper_scissors_rock_scores.txt"):
                print(
                    f"New high record! {utils.name} : {streak} games won in a row!")
                utils.add_leaderboard(
                    "Files\\paper_scissors_rock_scores.txt", streak)
        # If user lose, reset streak.
        elif winner == computer_hand:
            print("The computer has won...")
            streak = 0
        # If tie, keep streak.
        else:
            print("It's a tie. You still have your winning streak.")
        # Asks the user for a replay.
        time.sleep(1)
        playing = utils.replay("STREAK ENDS IF YOU LEAVE! ")
    return
