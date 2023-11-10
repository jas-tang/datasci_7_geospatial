# datasci_7_geospatial
This is a repository for Assignment 7 in HHA507, Geospatial. 

# GCP Maps API

I initially ran my code on Google Cloud Shell, but it wasn't working there for unknown reasons. The way that Google Shell Platform read functions was not working for me, so I swapped to Google Colab. 

I ran this code:
```
import requests
import urllib.parse
import json
import pandas as pd


df = pd.read_csv('/content/assignment7_slim_hospital_addresses.csv')
list_of_addresses = df['NAME'] + ', ' + df['ADDRESS'] + ', ' + df['CITY'] + ', ' + df['STATE']

google_response = []

for address in list_of_addresses:
    api_key = API KEY HERE

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    print(f'....finished with {address}')
```

This code took the CSV file provided that had about 8000 addresses, and ran it through a function. I created a separate list that appended the addresses together as they were separate in the CSV file.
It was then put in a for loop that changed the address into a URL readable format to be added into a search term. The response is spit out in a json format, which we can then get the address, latitude, and longitude. 
Finally, it places the data into an empty dataframe. 

```
df2 = pd.DataFrame(google_response)
df2
```
```

