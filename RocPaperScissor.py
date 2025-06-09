import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter your move = Rock,Paper,Scissor : ").capitalize()
computer_choice=random.choice(item_list)
print(f"User choice = {user_choice}, Computer choice = {computer_choice}")
if user_choice == computer_choice:
    print("Both chooses same : = Match Tie")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock = Computer")
    else:
        print("Rock smashes Scissor = You win ")
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cuts paper, Computer win")
    else:
        print("Paper covers rock, You win ")

elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")
else:
    print("Invalid input! Please choose Rock, Paper, or Scissor.")     


