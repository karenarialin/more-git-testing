import re
import os
# This function takes a user defined file and replaces all instances of the word "Karen" or "Lin" with the word "Pot"
def karenReplace(outputFile = "karenReplace.txt", useFile = True):
	if useFile == True:
		while True:
			try:
			    filepath = raw_input("What directory?: ")
			    os.chdir(filepath)
			    break
			except OSError:
			    print "Please choose an acceptable directory"
		while True: 
			try:
			    filename = raw_input("What file?: ")
			    open(filename)
			    break
			except IOError:
			    print "Please choose an acceptable file"
		with open(filename) as f: #write new file
			with open("karenOut.txt", "w") as f1:
			    for line in f:
			        f1.write(re.sub(r"\b(Karen|Lin)\b", "Pot", line, flags = re.IGNORECASE))
			f.close()
			f1.close()
	else:
		karenStr = raw_input("Type something here: ")
		karenStr = karenStr + "\n"
		print("\n" + re.sub(r"\b(Karen|Lin)\b", "Pot", karenStr, flags = re.IGNORECASE))
		with open("karenOut.txt", "w") as f:
			f.write(re.sub(r"\b(Karen|Lin)\b", "Pot", karenStr, flags = re.IGNORECASE))

# ################################################################
#       ACTUAL PROGRAM HERE
# ################################################################
while True: #Ask about files to load
	try:
		foo = raw_input('Do you have a file to load? (y/n): ')
		if foo != "y" and foo != "n":
			raise NameError('notyn')
		break
	except NameError:
		print "You did not choose a valid response: Please choose lowercase y or n"


if foo == "y": #Update variables for function
	useF = True
else:
	useF = False

karenReplace(useFile = useF)




