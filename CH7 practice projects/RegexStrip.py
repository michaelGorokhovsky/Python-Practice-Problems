#! python3
#! RegexStrip - takes a string and does the same thing as the strip() string method. 

import re

def reStrip(input, stripChar):
	if stripChar == '':
		s1Regex = re.compile(r'^(\s+)')
		phase1 = s1Regex.sub('',input)
		s2Regex = re.compile(r'(\s+)$')
		phase2 = s2Regex.sub('',phase1)
		print('Stripped pass is: ' + phase2 + ' and pass length is: ' + str(len(phase2)))
	else:
		s1Regex = re.compile(r'^['+stripChar+']*')
		phase1 = s1Regex.sub('', input)
		s2Regex =  re.compile(r'['+stripChar+']*$')
		phase2 = s2Regex.sub('', phase1)
		print('Stripped pass is: ' + phase2 + ' and pass length is: ' + str(len(phase2)))


	
p1 = '        test       '
p2 = ' testt     1 '
p3 = '0000ab0c000'
reStrip(p1, '')
reStrip(p2, '')
reStrip(p3,'0')