# CSI Program - Finding a specific DNA code in a larger DNA chain

# Read DNA file
with open("dna.txt", "r") as rndRead:
	fullDNA = rndRead.read()

# Initialize variables and lists
evaSuspicion = 0
larisaSuspicion = 0
matejSuspicion = 0
mihaSuspicion = 0

evaDNA = ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"]
larisaDNA = ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AAGTAGTGAC"]
matejDNA = ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"]
mihaDNA = ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]
indicator = ["Gender:","Race:","Hair color:","Eye color:","Face Shape:"]

# Introducing issue
print("\nSearching for the DNA patterns of suspects in this DNA chain...")
print(fullDNA)

# Starting analysis of all suspects

print("Eva: ")
for i in range(len(evaDNA)):
	print(indicator[i], evaDNA[i] in fullDNA)
	if evaDNA[i] in fullDNA:
		evaSuspicion = evaSuspicion + 1
if evaSuspicion == 5:
	print("Eva is guilty!")
else:
	print("Eva is innocent!")

print("\n")
print("Larisa: ")
for i in range(len(larisaDNA)):
	print(indicator[i], larisaDNA[i] in fullDNA)
	if larisaDNA[i] in fullDNA:
		larisSuspicion = larisaSuspicion + 1
if larisaSuspicion == 5:
	print("Larisa is guilty!")
else:
	print("Larisa is innocent!")

print("\n")
print("Matej: ")
for i in range(len(matejDNA)):
	print(indicator[i], matejDNA[i] in fullDNA)
	if matejDNA[i] in fullDNA:
		matejSuspicion = matejSuspicion + 1
if matejSuspicion == 5:
	print("Matej is guilty!")
else:
	print("Matej is innocent!")

print("\n")
print("Miha: ")
for i in range(len(mihaDNA)):
	print(indicator[i], mihaDNA[i] in fullDNA)
	if mihaDNA[i] in fullDNA:
		mihaSuspicion = mihaSuspicion + 1
if mihaSuspicion == 5:
	print("Miha is guilty!")
else:
	print("Miha is innocent!")