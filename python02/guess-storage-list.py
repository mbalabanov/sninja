# Guess a random secret number and stored in a list.

import random
import json

secret = random.randint(1, 100)
attempts = 0
hsDisplay = []

print("\n")

print("Hello, I'll think of a random number between 1 and 100, and you can try to guess it.")

with open("scores.txt", "r") as hsRead:
	hsDisplay = json.loads(hsRead.read())
	print("The scores so far: ")
	print(hsDisplay)
	print("\n")
	print("Now it is your turn to guess.")

while True:
	attempts = attempts + 1
	guess = int(input("\nEnter your guess here: "))
	
	if guess == secret:
		hsDisplay.append(attempts)
		hsDisplay.sort()
		with open("scores.txt", "w") as hsWrite:
			hsWrite.write(json.dumps(hsDisplay))
		print("You are correct. Your guess is right.")
		print("You took " + str(attempts) + " attempts.")
		print("The scores now are:")
		print(hsDisplay)
		break
	elif guess > secret:
		print("Your guess is too high.")
	elif guess < secret:
		print("Your guess is too low.")