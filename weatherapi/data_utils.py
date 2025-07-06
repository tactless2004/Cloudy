'''
Utilities for building NWSData objects.
'''
import requests
import json
from weatherapi.nwsdata import NWSData
from weatherapi.exceptions import IllegalGeoLocation

def from_geo(lat: float, lon: float) -> NWSData:
    '''
    Build an NWSData object from latitude, longitude geodata.
    '''
    r = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
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
