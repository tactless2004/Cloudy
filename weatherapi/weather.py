'''
Weather object holds data from a gridpoints/.../forecast request.
'''

class Weather:
    '''
    Weather data for a single point in time.
    WARNING: These should be generated with NWSData.get_forecast()
    '''
    def __init__(self, periods: list):
        self._periods = periods
        self.temperature = int(periods[0]['temperature'])
        self.wind_speed = periods[0]['windSpeed']
        self.wind_direction = periods[0]['windDirection']
        self.short_forecast = periods[0]['shortForecast']
        self.detailed_forecast = periods[0]['detailedForecast']
        self.percipitation_chance = str(periods[0]['probabilityOfPrecipitation']['value']) + "%"

    def __str__(self):
        '''
        Brief summary of weather data encapsulated in the object.
        '''
        return (
            f"{self.temperature}F, " +
            f"{self.wind_speed} -> {self.wind_direction}\n" +
            f"Precipitation: {self.percipitation_chance}\n" +
            f"{self.detailed_forecast}"
        )

    def get_raw(self, period: int) -> dict:
        '''
        Get raw['properties']['periods'] data (mostly for debug)
        '''
        return self._periods[period]
