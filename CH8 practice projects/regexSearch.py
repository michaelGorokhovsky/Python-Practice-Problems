#! python3
#regexSearch.py - opens all .txt files in a folder and searches for any line
#that matches a user supplied regular expression
import re, os

txtCount = os.listdir('C:\\CH8 practice projects')
#compile the regular expression
regexString = re.compile(sys.argv[1])
regexFile = re.compile(r'\w+\.txt')
#open every txt file one at a time
for file in range(len(txtCount)):
# use the regular expression to search for matching lines
	if regexFile.search(dirfiles[file]):
		openFile = open('C:\\CH8 practice projects\\' + dirfiles[i])
		readFile = openFile.readlines()
		for line in range(len(readFile)):
			r = 0
			if stringRegex.search(readFile[r]):
			print(readFile[r])
			r = r + 1