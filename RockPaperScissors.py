import random


def game():
    user_action = input("Chose your action (rock, paper or scissors): ").lower()

    # computer actions
    possible_actions = ["rock", "paper", "scissors"]
    comp_action = random.choice(possible_actions)

    print(f"\n You chose {user_action}, the computer chose {comp_action}.\n")

    if user_action == "rock":
        if comp_action == "scissors":
            print("Congratulations! You won!")
        if comp_action == "rock":
            print("It's a draw!")
        else:
            print("You lost!")

    if user_action == "scissors":
        if comp_action == "paper":
            print("Congratulations! You won!")
        if comp_action == "scissors":
            print("It's a draw!")
        else:
            print("You lost!")

    if user_action == "paper":
        if comp_action == "rock":
            print("Congratulations! You won!")
        if comp_action == "paper":
            print("It's a draw!")
        else:
            print("You lost!")

    #ask if repeat the game
    repeat = input("\nDo you want to play again (y/n)? ").lower()
    if repeat == "y":
        print("Okay! Let's play again!\n")
        game()
    else:
        print("Alright! See you next time!")
        quit()


game()



