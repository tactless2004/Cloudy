'''
NWS Data is an interface for interacting with api.weather.gov data
'''
import json
import requests
from weatherapi.weather import Weather


class NWSData:
    '''
    National Weather Service data object.
    '''
    def __init__(self, gridx, gridy, wfo):
        self._gridx = gridx
        self._gridy = gridy
        self._wfo = wfo

    def __str__(self):
        '''
        str() overload, primarily used for debug.
        '''
        return f'WFO ID: {self._wfo}, GRID_X: {self._gridx}, GRID_Y: {self._gridy}'

    def get_forecast(self) -> Weather:
        '''
        Get current Weather data
        '''
        r = requests.get(
            f"https://api.weather.gov/gridpoints/{self._wfo}/{self._gridx},{self._gridy}/forecast",
            timeout = 5
        )
        return Weather(json.loads(r.text)['properties']['periods'])
