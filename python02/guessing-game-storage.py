# Guess a random secret number and stored in a list and the top three scores outputted sorted.

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
	print("\nNow it is your turn to guess.")

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
		print("The best three scores are now:")
		print(hsDisplay[:3])
		break
	elif guess > secret:
		print("Your guess is too HIGH. Please try again.")
	elif guess < secret:
		print("Your guess is too LOW. Please try again")