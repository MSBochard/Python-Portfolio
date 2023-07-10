'''
Algorithm:  Another variation of finding the count and sum of comments
            of users. Uses the json library to parse through json.
'''
#import URL and SSL libraries as well as XML Element Tree
import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #Ask for URL link and parse through url
    url = input('Enter location: ')
    if (len(url) < 1):
        break
    print('Retrieving', url)
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print('Retrieved', len(data), 'characters')
    
    #Catch errors when loading json data
    try:
        js = json.loads(data)
    except:
        js = None
    
    if js == None:
        print('----Failure To Retrieve Data----')
        exit()

    #Find all lines containing the comment count from within the json
    #Count up each line and sum up the comments
    comNumList = []
    comments = js['comments']

    for line in comments:
        comNumList.append(line['count'])

    #Print Comment count and sum
    print('Count', len(comNumList))
    print('Sum', sum(comNumList))
