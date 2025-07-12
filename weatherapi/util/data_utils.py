'''
Utilities for building NWSData objects.
'''
import json
import requests
from geopy.geocoders import Nominatim
from geopy.location import Location
from weatherapi.core.nwsdata import NWSData
from weatherapi.exceptions import IllegalGeoLocation, InvalidLocation

def from_geo(lat: float, lon: float) -> NWSData:
    '''
    Build an NWSData object from latitude, longitude geodata.
    '''
    r = requests.get(f"https://api.weather.gov/points/{lat},{lon}", timeout = 5)
    if r.status_code == 404:
        raise IllegalGeoLocation(f"({lon}, {lat}) is not recognized by api.weather.gov")

    r_body = json.loads(r.text)
    wfo = r_body['properties']['cwa']
    gridx = r_body['properties']['gridX']
    gridy = r_body['properties']['gridY']

    return NWSData(
        gridx = gridx,
        gridy = gridy,
        wfo = wfo
    )

def from_location(location: str) -> NWSData:
    '''Build a NWSData object from location string using Geocoder Nominatim.'''
    geolocator = Nominatim(user_agent = "Cloudy")
    geocoder_result = geolocator.geocode(location)

    if not isinstance(geocoder_result, Location):
        raise InvalidLocation(f"{geocoder_result} is not recognized by Nominatim")

    return from_geo(
        lat = geocoder_result.latitude,
        lon = geocoder_result.longitude
    )
