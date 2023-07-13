'''
Algorithm:  Parses through a file to find the X-DSPAM-Confidence values
            and return the average of the values. Continuation of the
            Simple String Parse python script.

Note:       This code was intended to find the X-DSPAM-Confidence values
            found in email details. Use the mbox-short.txt file for testing.
'''
#Asks the user for a file to open,
#then validates that the file is able to be opened
fname = input('Enter file name: ')
try:
    file = open(fname)
except:
    print('Invalid file name:', fname)
    quit()

#Sets up initial values for the count and total variables
count = 0
total = 0

#Parses through the file, finding each line that contains
#X-DSPAM-Confidence, counting how many times a numeric value is found,
#and totalling the numeric values
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        lineStart = line.find(' ')
        lineNum = line[lineStart:]
        total = total + float(lineNum.strip())

#Finds the average of the numeric values and prints it
avg = total / count
print("Average spam confidence:", avg)
        
