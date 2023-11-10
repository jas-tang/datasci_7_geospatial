import requests
import pandas as pd
import numpy as np
import geopandas as gpd
import urllib.parse
import os
from dotenv import load_dotenv

df = pd.read_csv('/home/jason_tang/datasci_7_geospatial/data/assignment7_slim_hospital_addresses.csv')
list_of_addresses = df['NAME'] + ', ' + df['ADDRESS'] + ', ' + df['CITY'] + ', ' + df['STATE']

google_response = []

for address in list_of_address: 
    api_key = os.getenv(api_key)

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


df2 = pd.DataFrame(google_response)
