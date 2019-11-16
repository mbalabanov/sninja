# Homework 13.2: Model for "Guess the secret number" results

import datetime
import json
import random

class Result():
	def __init__(self, score, player_name, date):
		self.score = score
		self.player_name = player_name
		self.date = date

def get_score_list():
	with open("score_list.txt", "r") as score_file:
		score_list = json.loads(score_file.read())
		return score_list

def play_game():
	secret = random.randint(1, 30)
	attempts = 0
	score_list = get_score_list()

	while True:
		
		guess = int(input("Guess the secret number (between 1 and 30): "))
		attempts += 1
		
		if guess == secret:
			current_game = Result(score=attempts, player_name=name, date=str(datetime.datetime.now()))
			score_list.append(current_game.__dict__)
			with open("score_list.txt", "w") as score_file:
				score_file.write(json.dumps(score_list))
			print("You've guessed it - congratulations! It's number " + str(secret))
			print("Attempts needed: " + str(attempts))
			break
	
		elif guess > secret:
			print("Your guess is not correct... try something smaller")

		elif guess < secret:
			print("Your guess is not correct... try something bigger")

def get_top_scores():
	score_list = get_score_list()

	new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

	for score_dict in new_score_list:
		score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}.".format(score_dict.get("name"),str(score_dict.get("attempts")),score_dict.get("date"),score_dict.get("secret_number"))
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