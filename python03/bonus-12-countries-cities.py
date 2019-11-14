# Bonus homework 12.3: Geography Quiz

import random

# Dictionart of countries and their capitals
countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana", "United Kingdom": "London", "Germany": "Berlin"}

# The gameplay function
def guessCapital():

	# Initialize lists and variables
	countriesList = []
	limitRandom = len(countries_cities)

	for i in countries_cities:
		countriesList.append(i)

	# Generate random number, pick a random country and find the capital
	countryIndex = random.randint(1, limitRandom)
	guessCountry = countriesList[countryIndex]
	guessCity = countries_cities[guessCountry]

	# Play game
	while True:
		# User input starts here
		guess = input("\nWhat is the capital of " + guessCountry + "? ")
		
		if guess.upper() == guessCity.upper():
			print("Awesome " + name + "! Your guess is right.")
			break
		elif guess.upper() != guessCity.upper():
			print("Sorry, your guess is wrong. Try again. Here's a hint, it starts with " + guessCity[0].upper() + ".")
				

# Intro for player
print("\n\nWelcome to Guess the Capital City!")

while True:
	choose = input("\nWould you like to A) play a new game of guess the capital city, or B) quit?")
	if choose.upper() == "A":
		name = input("Please enter your name: ")
		guessCapital()
	else:
		break
