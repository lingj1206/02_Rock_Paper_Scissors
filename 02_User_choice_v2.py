# functions go here
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


# main routine
# lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]
# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    # ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s):", rps_list)

    # print out choice for comparison
    print(f"You chose {user_choice}")
