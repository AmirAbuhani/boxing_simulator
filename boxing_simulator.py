# Amir Abu Hani
import random
# Here is the dictionary where I decided for each move in which it wins, and in which it lose
move_dict = {"1": {"name": "Jab", "win": ["Uppercut"], "lose": ["Hook", "Cross"]},
             "2": {"name": "Cross", "win": ["Jab", "Hook"], "lose": ["Uppercut"]},
             "3": {"name": "Hook", "win": ["Jab"], "lose": ["Cross", "Uppercut"]},
             "4": {"name": "Uppercut", "win": ["Cross", "Hook"], "lose": ["Jab"]},
             }


def boxing_simulator():
    # This while loop is run as long as the user choice is the same to the opponent choice
    while True:
        # The user choice a number
        user_choice = input("Enter a number that representing a boxing move 1-4: ")
        # according to the user number, we extract the name of the move
        user_choice_name = move_dict[user_choice]["name"]
        print(f"Your move is: {user_choice_name}")
        # Extracting the win list for the user move in order to compare with the opponent choice
        user_choice_win = move_dict[user_choice]["win"]
        opponent_choice = str(random.randint(1, 4))
        print(f"Your opponent number is {opponent_choice}")
        opponent_choice_name = move_dict[opponent_choice]["name"]
        print(f"Your opponent move is: {opponent_choice_name}")
        if user_choice != opponent_choice:
            # if the opponent choice name in the user list win, this mean that the user is the win
            if opponent_choice_name in move_dict[user_choice]["win"]:
                print("You are the winner!")
                break
            else:
                # the opponent choice name is not in the user list win, this mean that the user lose
                # in other words, the user choice name is in the opponent win list
                print("Your opponent is the winner!")
                break
        # if the user and the opponent chose the same move
        else:
            print("Your move and your opponent's move are the same. Try again")


boxing_simulator()
