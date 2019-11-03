# Guess a random secret number

import random

print("Hello, I'll think of a random number between 1 and 100, and you can try to guess it.")

secret = random.randint(1, 100)

while True:
	guess = int(input(" Enter your guess here: "))
	
	if guess == secret:
		print("You are correct. Your guess is right")
		break
	elif guess > secret:
		print("Your guess is too high.")
	elif guess < secret:
		print("Your guess is too low.")