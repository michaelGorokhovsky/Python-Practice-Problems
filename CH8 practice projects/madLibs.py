#! python3
# madLibs.py - read in a mad-lib and prompt the user 
# to fill in where an ADJECTIVE, NOUN, ADVERB, or VERB appears

#get contents of the AdLib file
madLibFile = open('madLib.txt')
madLib = madLibFile.read()
outputString = ''
#Stop at each ADJECTIVE, NOUN, ADVERB, or VERB to take in user input
for word in madLib.split():
	if word == 'ADJECTIVE':
		newWord = input('Enter an adjective: ')
		outputString += newWord
	elif word == 'NOUN':
		newWord = input('Enter a noun: ')
		outputString += newWord
	elif word == 'VERB':
		newWord = input('Enter a verb: ')
		outputString += newWord
	elif word == 'ADVERB':
		newWord = input('Enter an adverb: ')
		outputString += newWord
	else:
		outputString += word
	outputString += ' '
#print output to screen and write to output text file
resultsFile = open('madLibResult.txt', 'w')
print(outputString)	
resultsFile.write(outputString)