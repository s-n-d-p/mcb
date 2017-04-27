#! /usr/bin/python2.7
# mcb.pyw - Saves and load pieces of text to the clipboard

# Usage: py mcb.pyw save <keyword> - Save clipboard to keyword.
# 		 py mcb.pyw <keyword> - Loads keyword to clipboard.    
#		 py mcb.pyw list - Loads all keywords to the clipboard.

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