# Guess a random secret number and stored in a list.

import random
import json
import datetime

# Initialize variables and lists
secret = random.randint(1, 100)
attempts = 0
hsDisplay = []
failedAttempts = []

# Greetings to user
print("\n")
print("Hello, I'll think of a random number between 1 and 100, and you can try to guess it.")

# Read past scores and show them
with open("scores_names.txt", "r") as hsRead:
	hsDisplay = json.loads(hsRead.read())
	print("\n")

# Get players name to save later to the score file
playerName = input("Before you start guessing, please enter you name: ")

# Core guessing game
while True:
	attempts = attempts + 1
	guess = int(input("\nEnter your guess here: "))

	# Success
	if guess == secret:
		# Reduce the date to a sane format
		playDate = datetime.datetime.now().strftime("%d.%m.%y, %H:%M")

		# Append values to the score list		
		hsDisplay.append({"name": playerName,"attempts": attempts,"playDate": str(playDate),"failedattempts": failedAttempts})

		# Write scores and other values into the file
		with open("scores_names.txt", "w") as hsWrite:
			hsWrite.write(json.dumps(hsDisplay))

		# Tell user results		
		print("\n")
		print("You are correct. Your guess is right.")
		print("You took " + str(attempts) + " attempts.")
		print("\n")
		print("The best past scores are:")
		# sort the list of dicts per attempts - Copied from solution on Smartninja Git Repo
		hsDisplaySort = sorted(hsDisplay, key=lambda k: k['attempts'])[:3]
		for i in hsDisplaySort:
			sortedScoreText = "Player {0} had {1} attempts on {2}. The wrong guesses were: {3}".format(i.get("name"),str(i.get("attempts")),i.get("playDate"),i.get("failedattempts"))
		print(sortedScoreText)
		break

	# Tell user how their wrong guess is positioned
	elif guess > secret:
		print("Your guess is too high.")
		failedAttempts.append(guess)
		print("Your failed attempts so far: " + str(failedAttempts))
	elif guess < secret:
		print("Your guess is too low.")
		failedAttempts.append(guess)
		print("Your failed attempts so far: " + str(failedAttempts))