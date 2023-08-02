'''
Algorithm:  This application will read audio track data from either an iTunes
            library file or the Library.xml file by default. A SQLite database
            will be made using the data and with the following schema:
            Table name: Genre Attributes: id, name
            Table name: Album Attributes: id, title, artist_id
            Table name: Artist Attributes: id, name
            Table name: Track Attributes: id, title, album_id, genre_id,
                                            len, rating, count
'''
#Import SQLite & XML Element Tree libraries
import sqlite3
import xml.etree.ElementTree as ET

#Connect to the tracksdb database
conn = sqlite3.connect('tracksdb.sqlite')
cur = conn.cursor()

#Make fresh tables by dropping tables if they exist and creating new ones
cur.executescript('''
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Track;


CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Artist(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    artist_id INTEGER
);
CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

#Ask the user for an audio track library xml file
#Opens 'Library.xml' by default if nothing is entered
fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'Library.xml'

#Function to parse through the key value pairs within dict tags
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

#Parse through the XML file and insert the data into the trackdb batabase
data = ET.parse(fname)
dicts = data.findall('dict/dict/dict')
for line in dicts:
    if (lookup(line, 'Track ID') is None):
        continue
    name = lookup(line, 'Name')
    artist = lookup(line, 'Artist')
    album = lookup(line, 'Album')
    genre = lookup(line, 'Genre')
    length = lookup(line, 'Total Time')
    rating = lookup(line, 'Rating')
    count = lookup(line, 'Play Count')

    if name is None or artist is None or album is None or genre is None:
        continue

    #Insert a new record into the Genre table if it doesn't already exist
    #Retrieve the genre_id
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cur.fetchone()[0]

    #Insert a new record into the Artist table if it doesn't already exist
    #Retrieve the artist_id
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    #Insert a new record into the Album table if it doesn't already exist
    #Retrieve the album_id
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
                VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    #Insert or Update a new record into the Track table
    cur.execute('''INSERT OR REPLACE INTO Track
                (title, album_id, genre_id, len, rating, count)
                VALUES (?, ?, ?, ?, ?, ?)''',
                (name, album_id, genre_id, length, rating, count))
    
#Commit SQL and close the connection to the database
conn.commit()
cur.close()
