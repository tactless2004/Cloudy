'''
Weather object holds data from a gridpoints/.../forecast request.
'''
import json

class Weather:
    def __init__(self, periods: list):
        self._periods = periods
        self.temperature = int(periods[0]['temperature'])
        self.wind_speed = periods[0]['windSpeed']
        self.wind_direction = periods[0]['windDirection']
        self.short_forecast = periods[0]['shortForecast']
        self.detailed_forecast = periods[0]['detailedForecast']

    def __str__(self):
        return f"{self.temperature}F, {self.wind_speed} -> {self.wind_direction}\n{self.detailed_forecast}"
        
    def test(self):
        for key in self._periods[0].keys():
            print(f"{key}:{self._periods[0][key]}")
        
