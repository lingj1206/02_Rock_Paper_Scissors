# functions go here
def choice_checker(question):

    error = "Please choose rock / paper / scissors or xxx to quit"

    while True:
        # ask for user choice
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "s" or response == "scissors":
            return response
        elif response == "p" or response == "paper":
            return response

        # exit code

        elif response == "x" or response == "xxx":
            return response
        else:
            print(error)

# main routine

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock / paper / scissors (r/p/s):")

    # print out choice for comparison
    print(f"You chose {user_choice}")