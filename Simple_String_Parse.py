'''
Algorithm:  A simple script that parses the following string and
            returns the numeric value within it. This is the precursor
            to the File Parse python file.
            String: "X-DSPAM-Confidence:    0.8475
'''
#String to parse
text = "X-DSPAM-Confidence:    0.8475"

#Finds the numeric value within the string and prints it out
startpos = text.find(' ')
number = text[startpos : len(text)]

answer = float(number.lstrip())

print(answer)
