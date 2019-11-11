# CSI ice cream investigation based on DNA samples. Find the right DNA sequences in a long chain of DNA data. This solution is based on the one provided by SmartNinja.

with open("dna.txt", "r") as dnaRead:
	fullDNA = dnaRead.read()

# Initialize suspects
suspects = {"eva": ["TGAAGGACCTTC","AAAACCTCA","TTAGCTATCGC","TTGTGGTGGC","AGGCCTCA"],
"larisa": ["TGAAGGACCTTC","AAAACCTCA","GCCAGTGCCG","AAGTAGTGAC","AAGTAGTGAC"],
"matej": ["TGCAGGAACTTC","AAAACCTCA","CCAGCAATCGC","TTGTGGTGGC","AGGCCTCA"],
"miha": ["TGCAGGAACTTC","AAAACCTCA","GCCAGTGCCG","GGGAGGTGGC","GCCACGG"]}

print("\n\nWelcome to CSI. We will find the ice cream thief based on their DNA.\n")
print("The suspects are Eva, Larisa, Matej, and Miha. This is the DNA found at the crime scene:")
print(fullDNA)

input("Now we will run the suspects' DNA characteristics through full DNA set. Press ENTER to start.")
for suspect in suspects:
	guilty = True
	for suspDNA in suspects[suspect]:
		if suspDNA not in fullDNA:
			guilty = False
			break
	if guilty is True:
		print("\n" + suspect + " is our perpetrator!")
		