#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# usage: py.exe mcb.pyw save <keyword> - Saves clipbord to keyword.
# 		py.exe mcb.pw <keyword> - Loads keyword to clipboard.
# 		py.exe mcb.pyw list - Loads all keywords to clipboard.
#		py.exe mcb.pyw delete <keyword> - delete's keyword from record
#		py.exe mcb.pyw delete - deletes all keywords from record

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

	#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
	#delete a keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	del mcbShelf[sys.argv[2]]
	
elif len(sys.argv) == 2:
	#List keywords and load content
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	#delete all keywords
	elif sys.argv[1].lower() == 'delete':
		for x in mcbShelf:
			del mcbShelf[x]
	#List keywords and load content
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		
	mcbShelf.close()