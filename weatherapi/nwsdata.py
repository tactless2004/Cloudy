'''
NWS Data is an interface for interacting with api.weather.gov data
'''
import requests



class NWSData:
    '''
    National Weather Service data object.
    '''
    def __init__(self, gridx, gridy, wfo):
        self._gridx = gridx
        self._gridy = gridy
        self._wfo = wfo
    
    def __str__(self):
        return f'WFO ID: {self._wfo}, GRID_X: {self._gridx}, GRID_Y: {self._gridy}'

    def get_forecast(self):
        r = requests.get(f"https://api.weather.gov/gridpoints/{self._wfo}/{self._gridx},{self._gridy}/forecast")
        return r.text