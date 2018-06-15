#! python3
#! strongPasswordDetection.py - checks if a password is at least eight characters long, 
#!contains both uppercase and lowercase characters, and has at least one digit

import re

passwordW = 'weak_password'
passwordW2 = 'aA1'
passwordS = 'StrongPa55word'

passRegex = re.compile(r'''(
	(?=.*[A-Z]+)		#at least one uppercase character
	(?=.*[a-z]+)		#at least one lowercase character
	(?=.*[\d]+)		#at least one digit
	.{8,} 	#at least 8 characters
	)''', re.VERBOSE)


result1 = passRegex.search(passwordW) is not None
result2 = passRegex.search(passwordW2) is not None
result3 = passRegex.search(passwordS) is not None
print('Pasword: ' + passwordW + ' is '+ str(result1) + 'ly a strong password')
print('Pasword: ' + passwordW2 + ' is '+ str(result2) + 'ly a strong password')
print('Pasword: ' + passwordS + ' is '+ str(result3) + 'ly a strong password')
