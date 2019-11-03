# Mood Checker - Aufgabe von Marin Balabanov

print("Hello! This is the friendly neighborhood mood checker. I will ask you how you feel and then give you a response.")

mood = input("How do you feel? (happy/sad/excited/tired/nervous/relaxed)")

if mood.lower() == "happy":
	print("It is soooo awesome that you are happy!")
elif mood.lower() == "sad":
	print("I am so sorry that you are sad. Write a Python program. This will cheer you up!")
elif mood.lower() == "excited":
	print("Wow! I am also excited!")
elif mood.lower() == "tired":
	print("I think it is a good idea to take a rest when you are tired.")
elif mood.lower() == "nervous":
	print("Take a deep breath three times, so that you are no longer nervous.")
elif mood.lower() == "relaxed":
	print("I really like you when you are relaxed.")
else:
	print("I'm sorry, I don't recognize your mood.")
