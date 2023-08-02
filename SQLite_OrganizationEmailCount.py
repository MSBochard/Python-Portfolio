'''
Algorithm:  This application will read mailbox data from the mbox.txt file
            and count the number of email messages per organization using a
            SQLite database with the following schema to maintain the counts.
            Table name: Counts
            Attributes: org, count
'''

#import SQLite3 and regex
import sqlite3
import re

#Connect to the database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#Drop table Counts if it exists to ensure a clean table
cur.execute('DROP TABLE IF EXISTS Counts;')

#Create table Counts with attributes org and count
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#Open the text file that will populate the Counts table
fname = 'mbox.txt'
fh = open(fname)

#Find each line of the file starting with From then keep a count of each
#email from an organization by updating the database
loop = 0
for line in fh:
    if not line.startswith('From: '):
        continue
    org = re.findall('^From: \S+@(\S+)', line)
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org[0],))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org[0],))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org[0],))

#Commit the SQL changes to the database
conn.commit()

#Find and return the organization with the top email count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1'
for record in cur.execute(sqlstr):
    print(str(record[0]), record[1])

#Close the connection to the database
cur.close()
