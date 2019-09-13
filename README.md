# Project Cryptonym
A project to generate names for all of my future projects.

## Format
The format of the naming convention will be based on the CIA's system for generating cryptonyms. Each name starts with a two character prefix that corresponds to the subject of the project. The rest of the word can be a separate dictionary word (Ex: MKULTRA) or more characters to make the entirety into a single dictionary word (Ex: ESSENCE). 

## Plan
My plan for the project is to store a list of prefixes for common subjects, such as WE for web, CH for c#, PI, for Python, and allow the user to add, remove, or edit these prefixes. This way, ~~if~~ when you learn new programming languages you can just add a new prefix for it. 

After you have a prefix, the program take will find all of the dictionary words that start with the prefix and put them into a list.

Example: The project is a twitter bot that posts the weather. TW could be your prefix.

The program will give a list of words that start with the prefix and they will be closer to the top if they match the key word:
	
	- Project TWISTER
	- Project TWINE
	
## Possible Improvements
If you want a project to work on, you could add a function that that takes a list of key words and your prefix and generates synonyms for your key words and appends them to the prefix.

Example:

	- Project TWSTORM
	- Project TWRAIN

