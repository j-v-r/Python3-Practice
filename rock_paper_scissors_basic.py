# print("Player 1 Choice:")
# player_one = input().lower()
# print("Player 2 Choice:")
# player_two = input().lower()
# if (player_one == "rock" and player_two == "scissors") or (player_one == "paper" and player_two == "rock") or (player_one == "scissors" and player_two == "paper"):
# 	print("Player One Wins!")
# elif player_one == player_two:
# 	print("Tie")
# else: 
# 	print("Player Two Wins!")

# VERSION 2 

from random import randint

rand_num = randint(0, 2)

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player, make your move: ").lower()

if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays: {computer}")

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("something went wrong")






































