'''
Algorithm:  Finds the place id of a given address using a branch of
            the Geocoding API from Google. This branch of the API does
            not have search limits.
'''
#Import libraries for URL and JSON
import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Variable for target API endpoint and API key
apiURL = 'http://py4e-data.dr-chuck.net/json?'
apiKey = 42

#Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#While loop to allow multiple searches
while True:
    #Prompt user for a location to search in the geocoding API
    location = input('Enter location: ')
    if (len(location) < 1):
        break
    
    #Request and retrieve the JSON of the geocoding API using
    #the inputted location and the API key
    params = {}
    params['address'] = location
    params['key'] = apiKey
    url = apiURL + urllib.parse.urlencode(params)
    print('Retrieving', url)
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print('Retrieved', len(data), 'characters')

    #Catch errors loading JSON data
    try:
        js = json.loads(data)
    except:
        js = None

    if js == None or 'No address' in js or js['status'] != 'OK':
        print('-----Failure To Retrieve-----')
        continue

    #Retrieve and print the first 'place_id'
    placeID = js['results'][0]['place_id']
    print('Place id', placeID)
