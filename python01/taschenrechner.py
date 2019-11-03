# Taschenrechner für die Grundrechenarten

print("Herzlich willkommen zum Rechner.")

ersteZahl = int(input("Bitte geben Sie die erste Zahl ein: "))
rechenZeichen = input("Geben Sie nun die Rechnart ein (+, -, *, /): ")
zweiteZahl = int(input("Geben Sie die dritte Zahl ein: "))

if rechenZeichen == "+":
	print("Das Ergebnis der Addition ist: " + ersteZahl + zweiteZahl)
elif rechenZeichen == "-":
	print("Das Ergebnis der Subtraktion ist: ")
	print(ersteZahl - zweiteZahl)
elif rechenZeichen == "*":
	print("Das Ergebnis der Multiplikation ist: ") 
	print(ersteZahl * zweiteZahl)
elif rechenZeichen == "/":
	print("Das Ergebnis der Division: ")
	print(ersteZahl / zweiteZahl)
else:
	print("Ihre Eingabe war ungültig.")