# This unit converter can convert kilometers into miles

print("Hello, this unit converter can convert kilometers into miles")

km = 0
miles = 0
abfrage = True

while abfrage:
	km = int(input("Enter the kilometers you want to convert into miles: "))
	miles = km * 1.6
	print("The kilometers you entered are this many mile: ")
	print(miles)
	
	frage = input("Do you want to do more conversions? Y/N ")
	
	if frage.lower() == "n":
		print("Thank you very much. We will now stop converting. You have made a simple Unit Converter very happy. All the best.")
		abfrage = False
		
		
	
