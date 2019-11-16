# Homework 13.1 - Create new players as object and store them in a file as a dictinary

class Player():
	def __init__(self, first_name, last_name, height_cm, weight_kg):
		self.first_name = first_name
		self.last_name = last_name
		self.height_cm = height_cm
		self.weight_kg = weight_kg
		
	def weight_to_lbs(self):
		pounds = self.weight_kg * 2.20462262
		return pounds

class BasketballPlayer(Player):
	def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
		super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
		self.points = points
		self.rebounds = rebounds
		self.assists = assists

class FootballPlayer(Player):
	def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
		super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
		self.first_name = first_name
		self.last_name = last_name
		self.height_cm = height_cm
		self.weight_kg = weight_kg
		self.goals = goals
		self.yellow_cards = yellow_cards
		self.red_cards = red_cards

print("\n\nWe'll create a new player and save it to our player file.")
newPlayer_fist_name = input("\nPlease enter the player's first name: ")

newPlayer_last_name = input("Please enter the player's last name: ")

newPlayer_height_cm = float(input("Please enter the player's height in cm: "))

newPlayer_weight_kg = int(input("Please enter the player's weight in kg: "))

while True:

	playerType = str(input("Is the new player 1) a basketball player or 2) a football player? "))

	if playerType == "1":
		newPlayer_points = int(input("Please enter the player's number of points: "))

		newPlayer_rebounds = int(input("Please enter the player's number of rebounds: "))
	
		newPlayer_assists = int(input("Please enter the player's number of assists: "))

		newPlayer_basketball = BasketballPlayer(first_name=newPlayer_fist_name, last_name=newPlayer_last_name, height_cm=newPlayer_height_cm, weight_kg=newPlayer_weight_kg, points=newPlayer_points, rebounds=newPlayer_rebounds, assists=newPlayer_assists)
	
		print("\nThis is your new basketball player: ")
		print("First name: " + newPlayer_basketball.first_name)
		print("Last name: " + newPlayer_basketball.last_name)
		print("Height in cm: " + str(newPlayer_basketball.height_cm))
		print("Weight in kg: " + str(newPlayer_basketball.weight_kg))
		print("Weight in lbs: " + str(newPlayer_basketball.weight_to_lbs()))
		print("Number of points: " + str(newPlayer_basketball.points))
		print("Number of rebounds: " + str(newPlayer_basketball.rebounds))
		print("Number of assists: " + str(newPlayer_basketball.assists))
		print("Your new basketball player is now saved in the basketball file.")

		with open("basketball_players.txt", "w") as basketball_file:
			basketball_file.write(str(newPlayer_basketball.__dict__))
		break

	elif playerType == "2":
		newPlayer_goals = int(input("Please enter the player's number of goals: "))

		newPlayer_red_cards = int(input("Please enter the player's number of red cards: "))
	
		newPlayer_yellow_cards = int(input("Please enter the player's number of yellow cards: "))

		newPlayer_football = FootballPlayer(first_name=newPlayer_fist_name, last_name=newPlayer_last_name, height_cm=newPlayer_height_cm, weight_kg=newPlayer_weight_kg, goals=newPlayer_goals, red_cards=newPlayer_red_cards, yellow_cards=newPlayer_yellow_cards)
	
		print("\nThis is your new football player: ")
		print("First name: " + newPlayer_football.first_name)
		print("Last name: " + newPlayer_football.last_name)
		print("Height in cm: " + str(newPlayer_football.height_cm))
		print("Weight in kg: " + str(newPlayer_football.weight_kg))
		print("Weight in lbs: " + str(newPlayer_football.weight_to_lbs()))
		print("Number of gloals: " + str(newPlayer_football.goals))
		print("Number of red cards: " + str(newPlayer_football.red_cards))
		print("Number of yellow cards: " + str(newPlayer_football.yellow_cards))

		print("Your new football player is now saved in the football file.")

		with open("football_players.txt", "w") as football_file:
			football_file.write(str(newPlayer_football.__dict__))
		break

	else:
		print("\nSorry, your input is invalid.")

