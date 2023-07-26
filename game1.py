import random
print("Rock...".lower())
print("Paper...".lower())
print("Scissors...".lower())
print("------------------")

number=random.randint(0,2)
computer="rock"
if number == 0 :
    computer="rock"
elif number ==1:
    computer="paper"
elif number ==2:
    computer="scissors"

Player_1 = input("Player_1 , make your move :").lower()
Player_2=computer
print(f"Player_2 , make your move :{computer}")

if Player_1 == Player_2 :
    print("thats a tie ....")
elif Player_1 == "rock":
    if Player_2 == "scissors":
        print("Player_1 wins!...")
    elif Player_2 == "paper":
        print("Player_2 wins!...")
elif Player_1 == "paper":
    if Player_2 == "rock":
       print("Player_1 wins!...")
    elif Player_2 == "scissors":
        print("Player_2 wins!...")

elif Player_1 == "scissors" :
    if Player_2 == "paper:":
        print("Player_1 wins!...")
    elif Player_2 == "rock" :
        print("Player_2 wins!..")
else:
    print("something went wrong ....")

if Player_1 == "rock" and Player_2 == "scissors":
  print("Player_1 wins!...")
elif Player_1 == "rock" and Player_2 == "paper":
   print("Player_2 wins!...")
elif Player_1 == "paper" and Player_2 == "rock":
   print("Player_1 wins!...")
elif Player_1 == "paper" and Player_2 == "scissors":
   print("Player2 wins!...")

elif Player_1 == "scissors" and Player_2 == "paper":
   print("Player_1 wins!...")
elif Player_1 == "scissors" and Player_2 == "rock":
   print("Player_2 wins...")
elif Player_1 == "rock":
   print("thats a tie...")
else:
   print("something went wrong ....")
