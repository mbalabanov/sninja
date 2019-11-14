# Homework 12.2: Make the guessing game more modular

# Code based on example in SmartNinja curriculum and not based on my previous work.

import datetime
import json
import random

def get_score_list():
	with open("score_list.txt", "r") as score_file:
		score_list = json.loads(score_file.read())
		return score_list

def play_game():
	secret = random.randint(1, 30)
	attempts = 0
	score_list = get_score_list()
	wrong_guesses = []

	while True:
		
		guess = int(input("Guess the secret number (between 1 and 30): "))
		attempts += 1
		
		if guess == secret:
			wrong_guesses.append(guess)
			score_list.append({"name": name, "attempts": attempts, "date": str(datetime.datetime.now()), "secret_number": secret, "wrong_guesses": wrong_guesses})
			with open("score_list.txt", "w") as score_file:
				score_file.write(json.dumps(score_list))
			print("You've guessed it - congratulations! It's number " + str(secret))
			print("Attempts needed: " + str(attempts))
			break
	
		elif guess > secret:
			print("Your guess is not correct... try something smaller")
			wrong_guesses.append(guess)

		elif guess < secret:
			print("Your guess is not correct... try something bigger")
			wrong_guesses.append(guess)

def get_top_scores():
	score_list = get_score_list()

	new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

	for score_dict in new_score_list:
		score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(score_dict.get("name"),str(score_dict.get("attempts")),score_dict.get("date"),score_dict.get("secret_number"),score_dict.get("wrong_guesses"))
		print(score_text)

while True:
	choose = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")
	if choose.upper() == "A":
		name = input("Please enter your name: ")
		play_game()
	elif choose.upper() =="B":
		get_top_scores()
	else:
		break