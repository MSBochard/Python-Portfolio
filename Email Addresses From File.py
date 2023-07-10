'''
Algorithm:  Parses through an email inbox text file and prints out each email
            address that an email was recieved from. Keeps count of the number
            of emails recieved.
'''
#Sets up initial count variable, then parses through the mbox-short.txt file
count = 0
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()

    #Skips lines that do not start with From
    if not line.startswith('From '):
        continue

    #Prints and counts email address for each From line
    emailHead = line.split()
    print(emailHead[1])
    count = count + 1

#Prints the number of email addresses found
print("There were", count, "lines in the file with From as the first word")
