# Joining Strings

firstString = "Empty text 1"
secondString = "Empty text 2"
contJoin = "y"

while contJoin == "y":
	print("\n")

	print("Hello, this is the useful text-joiner. Enter two texts and we will join them together for you, so you don't have to.")
	
	firstString = input("Enter the first text: ")
	
	secondString = input("Enter the second text: ")
	
	print("\n")
	
	print("The joined result is: " + firstString + secondString)
	
	print("\n")
	
	contJoin = input("Do you want to join another two texts? (Y/N)").lower()
