# Fizzbuzz -  Zahlen, die durch 3 teilbar sind, sollen durch "Fizz" ersetzt werden. Zahlen, die durch 5 teilbar sind, sollen durch "Buzz" ersetzt werden. Zahlen, die sowohl durch 3 als auch 5 teilbar sind, sollen durch "Fizz Buzz" ersetzt werden.

x = 1
zahl = 1

zahl = int(input("Wir spielen Fizz Buzz. Bitte geben Sie eine Zahl zwischen 1 und 100 ein: "))

for x in range(1 , zahl+1):
	if x % 3 == 0:
		print("Fizz")
	if x % 5 == 0:
		print("Buzz")
	if x % 3 == 0 and x % 5 == 0:
		print("Fizz Buzz")
	else:
		print(x)