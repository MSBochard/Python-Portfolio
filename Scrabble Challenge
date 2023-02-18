"""
Algorithm:     Creates a scrabble cheat that returns the words possible out
               of the user's letters and the points the words are worth.
"""

# Asks for the scrabble rack and validates the rack, reads the .txt containing Scrabble words and points
def main():
    rack = input("Enter your 7 letter Scrabble rack: ")

    while (len(rack) != 7) or (rack.isalpha() == 'False'):
        print("Invalid input. Your Scrabble rack must contain only " +\
              "7 alphabetical letters.", end = " ")
        rack = input("Enter your 7 letter Scrabble rack: ")

    file = open("c:\\TestData\\CROSSWD.txt")
    content = file.readlines()
    file.close()

    wordsWithSameLetters(rack.lower(), content)

# Finds words that use the letters available in the Scrabble rack
def wordsWithSameLetters(letters, data):
    rackList = []
    lettersList = list(letters)
    validWord = True
    
    for line in data:
        record = line.strip()
        if len(record) < 8:
            for ch in record:
                if ch in lettersList:
                    lettersList.remove(ch)
                    validWord = True
                else:
                    validWord = False
                    break
            if validWord == True:
                rackList.append(record)
        lettersList = list(letters)

    valueOfWords(rackList)

# Finds the value of all of the possible words
def valueOfWords(wordsList): 
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4,
              "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1,
              "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1,
              "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
    wordSum = 0
    rackDict = {}

    for word in wordsList:
        for ch in word:
            wordSum += scores[ch]
        rackDict[word] = wordSum
        wordSum = 0

    sortScrabbleCheats(rackDict)

# Sorts the list of possible words by word value
def sortScrabbleCheats(cheatDict):
    sortedDict = {}
    scoreList = []
    
    for key in cheatDict:
        scoreList.append(cheatDict[key])

    scoreList = sorted(scoreList, reverse = True)

    
    for i in range(len(cheatDict) - 1):
        for key in cheatDict:
            if cheatDict[key] == scoreList[i]:
                sortedDict[key] = scoreList[i]

    print("The words available from your rack are...")
    for key in  sortedDict:
        print(sortedDict[key], " ", key)
    
main()
