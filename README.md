# multi-clip board

Download mcb.py and mcb files.
Modules used - pyperclip, shelve

To install certain module, use :-

  		pipenv install .

mcb.py - Saves and load pieces of text to/from the clipboard

# Usage: 

		python mcb.py save keyword - Save clipboard to keyword. 
		python mcb.py keyword - Loads keyword to clipboard.
		python mcb.py delete keyword - Deletes the keyword entry
		python mcb.py delete - Deletes all the entries
		python mcb.py list - Loads all keywords to the clipboard.
