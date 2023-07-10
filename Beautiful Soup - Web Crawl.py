'''
Algorithm:  Uses the Beautiful Soup 4 program to make a simple web crawler.
            Asks for a starting url, the position of the next url to go to,
            and the number of urls to jump through.
'''

#Import libraries and Beautiful Soup
import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

#Function that parses through the html links and returns the anchor tags
def parse_html(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchor = soup('a')
    return anchor

#Function that takes the inputted position of the desired html links and the
#tags from the parse_html function to find and return the next html link
def find_next_html(pos, tagList):
    spot = 0
    for tag in tagList:
        spot = spot + 1
        if pos == spot:
            nextHTML = tag.get('href', None)
            print('Retrieving:', nextHTML)
            break
    return nextHTML

#Function that controls how many times the program jumps to the next link
#based on the user's inputted jump count
def html_jumping():
    print('Retrieving:', startURL)
    tags = parse_html(startURL)
    
    num = 1
    while num <= numJumps:
        newHTML = find_next_html(htmlPos, tags)
        tags = parse_html(newHTML)
        num = num + 1
    return

#Takes user's input for the starting html link, how many times to jump links,
#and what position to look for the link at. Then calls the html_jumping
#function to initiate the web crawler
startURL = input('Enter URL: ')
numJumps = int(input('Enter count: '))
htmlPos = int(input('Enter position: '))

html_jumping()
