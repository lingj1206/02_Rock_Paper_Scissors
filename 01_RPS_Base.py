import random


# functions go here
def check_rounds():
    while True:
        print("press <enter> to play infinite mode")
        response = input("How many rounds: ")

        round_error = "please press <enter>" \
                      "  or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
                else:
                    return response

            except ValueError:
                print(round_error)
                continue
        return response


def instructions():
    print("**** How to PLay ****")
    print()
    print("This game is a simple game of rock paper scissors")
    print("you should know how play")
    print()
    return ""


def choice_checker(question, valid_list):
    error = "Please choose rock / paper / scissors or xxx to quit"

    while True:
        # ask for user choice
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()

yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

mode = "regular"

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5

end_game = "no"
while end_game == "no":

    print()
    if mode == "infinite":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
        rounds += 1
        print(heading)
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        print(heading)

    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s):", rps_list)

    if user_choice == "xxx":
        break

    if rounds_played == rounds - 1:
        end_game = "yes"
    print()

    computer_choice = random.choice(rps_list[:-1])

    if user_choice == computer_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "paper" and computer_choice == "rock":
        result = "win"
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "win"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "win"
    else:
        result = "lose"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"
        print(f"You chose {user_choice}")
        print("computer chose:", computer_choice)

    else:
        feedback = f"{user_choice} vs {computer_choice} - you {result}"

    print(feedback)

    rounds_played += 1

    if rounds_played == rounds:
        break

rounds_won = rounds_played - rounds_lost - rounds_drawn

if rounds_played > 0:
    percent_win = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tie = rounds_drawn / rounds_played * 100

    print()
    print('***** End Game Summary *****')
    print(f"Won: {rounds_won} |  Lost: {rounds_lost}  | Draw: {rounds_drawn}")

    print()

    print("***** Game Statistics *****")
    print(f"Win: {rounds_won},({percent_win:.0f}%)\nLoss:{rounds_lost}, "
          f"({percent_lost:.0f}%)\nTie: {rounds_drawn}, ({percent_tie:.0f}%) ")
    print()
    print("Thank you for playing")

else:
    print("🐔🐔🐔 You chickened out.  Squawk, squawk.  🐔🐔🐔")
    