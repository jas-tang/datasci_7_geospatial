import requests
import pandas as pd
import numpy as np
import re
import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.parse
import os
from dotenv import load_dotenv

df = pd.read_csv('/home/jason_tang/datasci_7_geospatial/data/assignment7_slim_hospital_addresses.csv')
list_of_addresses = df['NAME'] + ', ' + df['ADDRESS'] + ', ' + df['CITY'] + ', ' + df['STATE']

for x in list_of_addresses:
    api_key = 'AIzaSyDa1RtZ5sr41GcZGP9Y5iC-ZCWnPHIKn3w'

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    location = x

    location_cleaned = urllib.parse.quote(location)

    url_request_part1 = search + location_cleaned + '&key=' + api_key

    response = requests.get(url_request_part1)
    
    json = response.json()

    lat_long = response['results'][0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']

    print(f'Address: {location}, Lat: {lat}, Lng: {lng} ')

