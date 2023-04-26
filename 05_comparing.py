rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        computer_choice = rps_list[comp_index]
        # user_index += 1

        if user_choice == computer_choice:
            result = "tie"

        elif user_choice == "paper" and computer_choice == "rock":
            result = "win"
        elif user_choice == "scissors" and computer_choice == "paper":
            result = "win"
        elif user_choice == "rock" and computer_choice == "scissors":
            result = "win"
        else:
            result = "lose"

        print(f"You chose: {user_choice}, the computer chose {computer_choice}")

        print(f"Results: {result}")
    comp_index += 1

