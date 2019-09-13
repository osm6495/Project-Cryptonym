import json
import os

#Opens the Prefix file in read and write mode ('r+') and loads the JSON into a dictionary named prefixes.
file = open('Prefixes.json', 'r+')
prefixes = json.load(file)

#Opens the dictionary file in read and write mode ('r+') and loads the JSON into a dictionary named words.
wordsFile = open('words_dictionary.json', 'r')
words = json.load(wordsFile)


#Add a prefix to the list. The category should be a word or phrase in the form of a string that describes the type of project that would use this prefix.
#The prefix should be two capital letters in the form of a string that fit the category and are a common start for words. Ex: Category; Python, Prefix; PI.
#For python the prefix could have been py, but there aren't as many words that start with py as there are that start with pi.
def addPrefix(category, prefix):

    #Check that category and prefix are strings and that prefix is only two letters.
    if isinstance(category, str) and isinstance(prefix, str) and len(prefix) == 2:

        #Add the pair to the prefixes dictionary.
        prefixes[category] = prefix
   
        #Accesses the global vaiable file and then closes it and removes the old prefixes file.
        global file
        file.close()
        os.remove('Prefixes.json')

        #Makes a new prefixes file and puts the prefixes dictionary, with the new prefix, in it.
        file = open('Prefixes.json', 'w+')
        json.dump(prefixes, file, indent=4)

#Change a prefix on the list. Include the old category and the program will find that prefix and set the category and prefix to the second set of 
#inputs. The category should be a word or phrase in the form of a string that describes the type of project that would use this prefix.
#The prefix should be two capital letters in the form of a string that fit the category and are a common start for words. Ex: Category; Python, Prefix; PI.
#For python the prefix could have been py, but there aren't as many words that start with py as there are that start with pi.
def editPrefix(oldCategory, newCategory, newPrefix):

    #Reuses the other methods for efficiency.
    removePrefix(oldCategory)
    addPrefix(newCategory, newPrefix)

    #Accesses the global vaiable file and then closes it and removes the old prefixes file.
    global file
    file.close()
    os.remove('Prefixes.json')

    #Makes a new prefixes file and puts the prefixes dictionary, without the removed prefix, in it.
    file = open('Prefixes.json', 'w+')
    json.dump(prefixes, file, indent=4)
    

#Remove a prefix from the list. The category should be a word or phrase in the form of a string that describes the type of project that would use this prefix.
#The prefix should be two capital letters in the form of a string that fit the category and are a common start for words. Ex: Category; Python, Prefix; PI.
#For python the prefix could have been py, but there aren't as many words that start with py as there are that start with pi.
def removePrefix(category):

    #Accesses the global variable file.
    global file

    #Make sure the category has a prefix.
    if category in prefixes:

        #Remove the category and prefix pair from prefixes.
        prefixes.pop(category)

        #Close the file and remove the old prefix file.
        file.close()
        os.remove('Prefixes.json')

        #Make a new prefixes file and put the prefixes dictionary, without the removed prefix, in it.
        file = open('Prefixes.json', 'w+')
        json.dump(prefixes, file, indent=4)
    else:
        #If the category doesn't have a prefix, let the user know. They might have just misspelled it.
        return 'Category not found'
 

#Generate a list of project names from a two capital letters in the form of a string. These project names will be any words that start with the prefix. outputFileName should be a string.
#This will output a long list on names like Project PIANO and Project PICTRUEFRAME (in the case of a PI prefix for python)
def generateNameList(prefix, outputFileName):

    #Access the global variable words and open the output file in write/create a new file mode ('w+'). This means if the user already has an output file, it will just reuse it, otherwise
    #it will make a brand new output fle for them.
    global words
    f = open(outputFileName, 'w+')
    
    #Initialize a counter and an output dictionary.
    count = 0
    output = {}

    #Check that prefix is a string that is 2 letters long.
    if isinstance(prefix, str) and len(prefix) == 2:

        #For each word in the word_dictionary file, make that into a variable 'word'.
        for word in words:

            #Make a temporary variable to hold the lowercase version of the prefix.
            lowerPrefix = prefix.lower()

            #Check that the word is a string and the first two letters of the word match the lowercase prefix
            if isinstance(word, str) and word[0:2] == lowerPrefix[0:2]:

                #Count the amount of words
                count += 1

                #Put the word into all caps and cut off the first two letters, since we already have the prefix for that. (Alternatively, you could just not include the prefix.)
                caps = word.upper()
                append = caps[2:len(caps)]

                #Add a key, value pair in the output dictionary where the key is the number of the word(So the file will be numbered) and the value is Project PREFIXWORD
                output[count] = ("Project " + prefix + append)

    #Put the output dictionary into the file(f) and also indent it so that it looks nice, then close the file.
    json.dump(output, f, indent=4)
    f.close()


wordsFile.close
file.close()