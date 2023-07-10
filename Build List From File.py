'''
Algorithm:  Builds a list of all the words found in the romeo.txt file.
'''
#Sets up initial list variable
wordlist = []

#Opens the romeo.txt file, then parses the file
fhand = open('romeo.txt')
for line in fhand:
    line = line.strip()

    #Takes each line and splits it up into single words,
    #then adds each word into the list if it doesn't already exist
    words = line.split()
    for word in words:
        if word not in wordlist:
            wordlist.append(word)

#Sorts the list alphabetically, then returns the list of words
wordlist.sort()
print(wordlist)
    
