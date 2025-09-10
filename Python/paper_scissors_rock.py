import random
import time
import utils
def play():
    #Similar overall structure to other games.
    streak = 0
    playing = 1
    #A set of rules is created to determine who wins.
    rules = {
  ('scissors', 'paper'): 'scissors',
  ('paper', 'rock'): 'paper',
  ('rock', 'scissors'): 'rock',
}
    #The list keeps track of what hand the user has played until now. 
    hands_frequency = ["paper", "scissors", "rock"]
    print(f"\n === Paper Scissors Rock === \n Welcome to paper scissors rock {utils.name}! \n Simple game where scissors win paper, paper wins rock and rock wins scissors.\n Same hand is a tie. \n You can keep winning against a computer to increase your win streak, and the highest streak goes in the leaderboard. \n Good luck!")
    while playing: 
        print("\n======")
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
                if user_hand == "paper" or user_hand == "scissors" or user_hand == "rock":  #If the user wrote the hand itself, it still accepts it
                    break
                print("Invalid input.")
        hands_frequency.append(user_hand)  #The hand user did is appended to the list for the computer to use the winning hand more frequently, as explained above.
        winner = rules.get((computer_hand, user_hand), rules.get((user_hand, computer_hand), 'tie')) #From the rules, it determines who wins or if it's a tie.
        time.sleep(0.5) #Just a delay to prvent user from spamming.
        print(f"Computer: {computer_hand}  You: {user_hand}")
        if winner == user_hand: #Winning and losing message and streak, and highest streak system.
            print(f"{utils.name} won!")
            streak += 1
            print(f"You have won {streak} games in a row!")
            if streak > int(utils.open_leaderboard(2)[1]): 
                        utils.add_leaderboard(2,str(utils.name) + " " + str(streak))
                        print(f"New high record! {utils.name} : {streak} games won in a row!")
        elif winner == computer_hand:
            print(f"Computer won...")
            streak = 0
        else:
            print("It's a tie. You still have your winning streak.")
        playing = utils.replay("STREAK ENDS IF YOU LEAVE! ")
    return