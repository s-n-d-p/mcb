#! /usr/bin/python2.7
# mcb.py - Saves and load pieces of text to the clipboard

# Usage: 
#		python mcb.py save <keyword> - Save clipboard to keyword.
# 		python mcb.py <keyword> - Loads keyword to clipboard.
#		python mcb.py delete <keyword> - Deletes the keyword entry
#		python mcb.py delete - Deletes all the entries
#		python mcb.py list - Loads all keywords to the clipboard.

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2].lower()] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	del mcbShelf[sys.argv[2].lower()]
elif sys.argv[1].lower() == 'delete':
	for key in mcbShelf.keys():
		del mcbShelf[key]
elif sys.argv[1].lower() == 'list':
	pyperclip.copy(str(list(mcbShelf.keys())))
else:
	pyperclip.copy(mcbShelf[sys.argv[1].lower()])

mcbShelf.close()
sys.exit()	
