import json
import os

file = open('Prefixes.json', 'r+')
prefixes = json.load(file)

wordsFile = open('words_dictionary.json', 'r')
words = json.load(wordsFile)


#Add a prefix to the list. The category should be a word or phrase in the form of a string that describes the type of project that would use this prefix.
#The prefix should be two capital letters in the form of a string that fit the category and are a common start for words. Ex: Category; Python, Prefix; PI.
#For python the prefix could have been py, but there aren't as many words that start with py as there are that start with pi.
def addPrefix(category, prefix):
    if isinstance(category, str) and isinstance(prefix, str) and len(prefix) == 2:
        prefixes[category] = prefix
        global file
        file.close()
        os.remove('Prefixes.json')
        file = open('Prefixes.json', 'w+')
        json.dump(prefixes, file, indent=4)

#Change a prefix on the list. Include the old category and the program will find that prefix and set the category and prefix to the second set of 
#inputs. The category should be a word or phrase in the form of a string that describes the type of project that would use this prefix.
#The prefix should be two capital letters in the form of a string that fit the category and are a common start for words. Ex: Category; Python, Prefix; PI.
#For python the prefix could have been py, but there aren't as many words that start with py as there are that start with pi.
def editPrefix(oldCategory, newCategory, newPrefix):
    removePrefix(oldCategory)
    addPrefix(newCategory, newPrefix)
    global file
    file.close()
    os.remove('Prefixes.json')
    file = open('Prefixes.json', 'w+')
    json.dump(prefixes, file, indent=4)
    

#Remove a prefix from the list. The category should be a word or phrase in the form of a string that describes the type of project that would use this prefix.
#The prefix should be two capital letters in the form of a string that fit the category and are a common start for words. Ex: Category; Python, Prefix; PI.
#For python the prefix could have been py, but there aren't as many words that start with py as there are that start with pi.
def removePrefix(category):
    global file
    if category in prefixes:
        prefixes.pop(category)
        file.close()
        os.remove('Prefixes.json')
        file = open('Prefixes.json', 'w+')
        json.dump(prefixes, file, indent=4)
    else:
        return 'Category not found'
 

#Generate a list of project names from a two capital letters in the form of a string. These project names will be any words that start with the prefix. outputFilePath should be a string.
#This will output a long list on names like Project PIANO and Project PICTRUEFRAME (in the case of a PI prefix for python), if you want names like PISTORM and PICAMERA, use generateWordNAME()
def generateNameList(prefix, outputFileName):
    global words
    f = open(outputFileName, 'w+')
    count = 0
    output = {}
    if isinstance(prefix, str) and len(prefix) == 2:
        for word in words:
            lowerPrefix = prefix.lower()
            if isinstance(word, str) and word[0:2] == lowerPrefix[0:2]:
                count += 1
                caps = word.upper()
                append = caps[2:len(caps)]
                output[count] = ("Project " + prefix + append)
    json.dump(output, f, indent=4)
generateNameList("PI", 'Output.json')

wordsFile.close
file.close()