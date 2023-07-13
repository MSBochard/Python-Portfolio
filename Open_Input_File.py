'''
Algorithm:  A simple script that opens a file and prints it line by line.
'''
#Asks the user for a file to open,
#then validates that the file is able to be opened
fname = input('Enter file name: ')
try:
    file = open(fname)
except:
    print('Invalid file name:', fname)
    quit()

#Parses through the file and prints each line
for line in file:
    line = line.upper()
    line = line.rstrip()
    print(line)
