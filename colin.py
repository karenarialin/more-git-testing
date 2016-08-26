import re
import os
import sys
from random import randint

#Original script by Colin McCubbins
#Enhancements by Karen Lin

# This function takes a user defined file and replaces all instances of the word "Colin" or "McCubbins" with a random variation of the word "Pot."

drug_list = ['Pot', 'Weed', 'Cannabis', 'Dope', 'Joint', 'Mary Jane', '420', 'Blaze']

def colinReplace(outputFile = "Potified.txt", useFile = True):
	
	if useFile == True:
		while True: 
			try:
			    raw_file = raw_input("Enter file path (or drag file into terminal window): ")
			    filepath = os.path.dirname(raw_file)
			    name = os.path.basename(raw_file)
			    os.chdir(filepath)
			    filename = name.split()[0]
			    open(filename)
			    break
			except KeyboardInterrupt:
				sys.exit("olin loves weed.")
			except (IOError, OSError):
			    print "Please choose an acceptable file"
		with open(filename) as f:     #write new file
			with open("Potified.txt", "w") as f1:
			    for line in f:
			        f1.write(re.sub(r"\b(Colin|McCubbins)\b", get_drug(), line, flags = re.IGNORECASE))
			f.close()
			f1.close()
	else:
		colinStr = raw_input("Type something here: ")
		colinStr = colinStr + "\n"
		print("\n" + re.sub(r"\b(Colin|McCubbins)\b", get_drug(), colinStr, flags = re.IGNORECASE))
		with open("Potified.txt", "w") as f:
			f.write(re.sub(r"\b(Colin|McCubbins)\b", get_drug(), colinStr, flags = re.IGNORECASE))

def get_drug():
	global drug_list
	return drug_list[randint(0, len(drug_list) - 1)]

# ################################################################
#                     ACTUAL PROGRAM HERE
# ################################################################

print("Type Ctrl-C to quit (or maybe just go to rehab).")

while True: #Ask if user wants to load any files
	try:
		foo = raw_input('Do you have a file to load? (y/n): ')
		if foo != "y" and foo != "n":
			raise NameError('notyn')
		break
	except KeyboardInterrupt:
		sys.exit("olin smokes pot.")
	except NameError:
		print "You did not choose a valid response: Please choose lowercase y or n"



if foo == "y": #Update variables for function
	useF = True
else:
	useF = False

colinReplace(useFile = useF)
print('Success!')




