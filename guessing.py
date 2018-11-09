import random

play_again = "y"

while play_again == "y":
	random_number = random.randint(1, 10)
	guess = None
	while guess != random_number:
		guess = int(input("Pick a random number between 1 and 10: "))
		if guess < random_number:
			print("Too low!")
		elif guess > random_number: 
			print("Too high!")
		else:
			play_again = input("You won! Play again? (y/n) ")