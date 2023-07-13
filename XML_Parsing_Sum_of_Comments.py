'''
Algorithm:  Parses through a url in the xml format to find comment tags
            containing the amount of comments of each user, then counting
            the number of comment tags found and summing the number of comments.
'''
#import URL and SSL libraries as well as XML Element Tree
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Ask for URL link and parse through url
url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

#Find all lines containing comment tags and pull out the comment
#count from within the comment tag tree
comNumList = []
tree = ET.fromstring(data)
counts = tree.findall('.//count')

for line in counts:
    num = line.text
    comNumList.append(int(num))

#Print Comment count and sum
print('Count', len(comNumList))
print('Sum', sum(comNumList))
