'''
Algorithm:  Uses the Beautiful Soup 4 program to parse through html.
            Another variation of finding the count and sum of comments
            of users by looking for the comment tag within the html.
'''
#Import needed libraries - urllib, regex, and the Beautiful Soup 4 program
import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

#Asks the user for a url to parse, uses urllib to open and read the webpage,
#and uses beautiful soup to parse the html
url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Finds the span tag to locate comment counts to build the comNumList list
comNumList = []
tags = soup('span')
for tag in tags:
    #Uses regex to find numeric values within the span tag
    num = re.findall('>([0-9]+)<', str(tag))
    #Makes sure to grab a valid numeric number, then adds the num to comNumList
    if len(num) > 0:
        #This line is done in case multiple numeric values are retrieved
        for item in num:
            comNumList.append(int(item))

#Prints the count of the comment tags and the sum of all users' comments
print('Count', len(comNumList))
print('Sum', sum(comNumList))
