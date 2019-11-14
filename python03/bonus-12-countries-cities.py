# Bonus homework 12.3: Geography Quiz

import random

countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana", "United Kingdom": "London", "Germany": "Berlin"}

countriesList = []
citiesList = []

for i in countries_cities:
	countriesList.append(i)

countryIndex = random.randint(1, len(countriesList))
guessCountry = countriesList[countryIndex]
guessCity = countries_cities[guessCountry]

guess = input("\nWhat is the capital of " + guessCountry + "? ")

if guess.upper() == guessCity.upper():
	print("Awesome! Your guess is right.")
else:
	print("Sorry, your guess is wrong. The right answer is " + guessCity + ".\n")
