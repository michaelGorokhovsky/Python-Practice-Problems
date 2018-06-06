#This program
#takes a list of lists of strings and displays it in a 
#well-organized table with each column right-justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
			 
def printTable(listOfCols):
#maxLen = 0
#Getting all column sizes
	maxLen = [0,0,0]
	for i in range(len(listOfCols)):
		maxLen[i] = 0
		for j in range(len(listOfCols[i])):
			if len(listOfCols[i][j]) + 1 > maxLen[i]:
				maxLen[i] = len(listOfCols[i][j]) + 1
	#Printing out the table
	r = ['','','','']
	for i in range(len(listOfCols[0])):
		for j in range(len(listOfCols)):
			r[i] += listOfCols[j][i].rjust(maxLen[j])
	print(r[0])
	print(r[1])
	print(r[2])
	print(r[3])
printTable(tableData)