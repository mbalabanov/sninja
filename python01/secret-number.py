# Guess the secret number

print("Hello, try to guess the secret number.")

secret = 52
guess = 0

while guess != secret:
	guess = int(input("Enter your guess for the secret number (it is somewhere between 1 to 100): "))

	if guess == secret:
		print("Congratulations! You have guessed the secret number.")
	else:
		print("Sorry, your guess is not correct... please try again")
	