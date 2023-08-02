'''
Algorithm:  This application will read User and Course data from the
            roster_data.json file. A SQLite database will be made using the
            data and with the following schema:
            Table name: User Attributes: id, name
            Table name: Course Attributes: id, title
            Table name: Member Attributes: user_id, course_id, role
'''
#Import JSON and SQLite3 libraries
import json
import sqlite3

#Connect to the rosterdb database
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#Make fresh tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);
CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

#Open the file that contains the data to populate the database
fname = 'roster_data.json'
fileData = open(fname).read()
data = json.loads(fileData)

#Parse through the file and add the data to the database
for line in data:
    name = line[0]
    title = line[1]
    role = line[2]

    #Insert a new record into the User table if it doesn't already exist
    #Retrieve the user_id
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    #Insert a new record into the Course table if it doesn't already exist
    #Retrieve the course_id
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    #Insert or Update a new record into the Member table
    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
                VALUES (?, ?, ?)''',(user_id, course_id, role))

#Commit SQL and close the connection to the database
conn.commit()
cur.close()
