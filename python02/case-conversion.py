# Upper and lower case strings

textString = "Empty Text"
conversion = "u"
continueConv = "y"

while continueConv == "y":
	print("\n\n")
	textString = input("Enter any text and it will be converted to upper or lower case: ")

	conversion = input("Do you want this converted to upper or lower case? (U or L)")

	conversion = conversion.lower()

	print(conversion)

	if conversion == "u":
		textString = textString.upper()
		print("Your upper case text is: " + textString)

	if conversion == "l":
		textString = textString.lower()
		print("Your lower case text is: " + textString)

	print("\n")

	continueConv = input("Do you want to convert more text? (Y/N)").lower()

