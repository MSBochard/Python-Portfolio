'''
Algorithm:  Finds how many emails were recieved each hour. Based on the 24hr
            clock. Does not include seperating by day. Two emails recieved at
            2pm on different days will still count as two emails recieved at 14:00.
'''
#Opens the mbox-short.txt file
fhand = open('mbox-short.txt')

#Sets up initial list variable, then parses through the mbox-short.txt file
hours = []
for line in fhand:
    line = line.strip()

    #Skips lines that do not start with From
    if not line.startswith('From '):
        continue

    #Grabs the timestamp of the email header, splits it by :,
    #and appends the hour timestamp to the hours list
    emailHead = line.split()
    time = emailHead[5].split(':')
    hours.append(time[0])

#Creates a dictionary that makes key:value pairs of
#hours of the day and the count of emails recieved in that hour
counts = {}
for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1

#Sorts the dictionary keys in ascending order,
#then prints the hour and the emails recieved that hour
for hr, cnt in sorted(counts.items()):
    print(hr, cnt)
