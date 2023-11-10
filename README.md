# datasci_7_geospatial
This is a repository for Assignment 7 in HHA507, Geospatial. 

## GCP Maps API

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

This code took the CSV file provided (assignment7_slim_hospital_addresses.csv) that had about 8000 addresses, and ran it through a function. I created a separate list that appended the addresses together as they were separate in the CSV file.
It was then put in a for loop that changed the address into a URL readable format to be added into a search term. The response is spit out in a json format, which we can then get the address, latitude, and longitude. 
Finally, it places the data into an empty dataframe. 

```
df2 = pd.DataFrame(google_response)
df2
```
This was the completed dataframe.

![](https://github.com/jas-tang/datasci_7_geospatial/blob/main/images/1.JPG)

I was curious as to how long it would take to go through the 8000+ addresses, but it took 12 minutes for approximately 3000. 


## GCP Maps API Reverse

The intention of this code was to take in coordinates and do the same thing as before.
```
df3 = pd.read_csv('/content/assignment7_slim_hospital_coordinates.csv')

google_response_reverse = []

for index, row in df3.head(100).iterrows():
    api_key = INSERT API KEY HERE 

    lat = row['X']
    lon = row['Y']

    search = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='

    url_request_part1 = f'{search}{lat},{lon}&key={api_key}'

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    if response_dictionary['status'] == 'OK':
        address = response_dictionary['results'][0]['formatted_address']
        final = {'latitude': lat, 'longitude': lon, 'address': address}
        google_response_reverse.append(final)
        print(f'Finished reverse geocoding for {lat}, {lon}')

df_reverse = pd.DataFrame(google_response_reverse)
```
This works similarly to the normal geospatial geocoding. 

I loaded up the provided dataset (assignment7_slim_hospital_coordinates.csv). 
For index is a variable that contains the current row. Itterrows itterates a fucntion over a dataframe as (index, Series) in pairs.
This time, since the assignment was to use 100 random coordinates, I just use .head to use the first 100. 
We then named the rows, which was in the dataframe, 'X', and 'Y'. 
WE then followed the exact same format as the code that precedes this. 

This was the result. 

![](https://github.com/jas-tang/datasci_7_geospatial/blob/main/images/2.JPG)

## Geopandas Data Processing and Visualization

I found five geospatial datasets to map out visually using geopandas. 

This map looked at Obesity by state.

![](https://github.com/jas-tang/datasci_7_geospatial/blob/main/images/3.JPG)

This map looked at the demographics of Lake County, specifically Asians.

![](https://github.com/jas-tang/datasci_7_geospatial/blob/main/images/4.JPG)

This map looked at the hospital discharge rates of Lake County Illinois.

![](https://github.com/jas-tang/datasci_7_geospatial/blob/main/images/5.JPG)

This map looked at the birth statistics of Lake Country, Illinois, specifically Birth rate.

![](https://github.com/jas-tang/datasci_7_geospatial/blob/main/images/6.JPG)

This map looked at Alleghory County's Air Quality, but I told it to look for the average temperatures. 
![](https://github.com/jas-tang/datasci_7_geospatial/blob/main/images/7.JPG)

This map looked off, so I tried to use matplotlib to make it more readable.

![](https://github.com/jas-tang/datasci_7_geospatial/blob/main/images/8.JPG)

However, it did not succeed. 

