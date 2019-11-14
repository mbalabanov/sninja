# Exercise 12.1: The sum of two numbers

def sum_numbers(firstNumber,secondNumber):
	sumOfNumbers = firstNumber + secondNumber
	return sumOfNumbers

print("Now we will add two numbers together.\n")
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

print("The sum is: ", sum_numbers(firstNumber, secondNumber))

