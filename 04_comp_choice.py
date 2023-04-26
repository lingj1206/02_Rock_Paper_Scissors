import random

rps_list = ["rock", "paper", "scissors"]

for item in range(0, 20):
    computer_choice = random.choice(rps_list)
    print(computer_choice, end="\t")
    
