'''
Session state for Cloudy UIs
'''
from session.messages import Response
from weatherapi.core import NWSData, Weather
from weatherapi.util import from_geo
from weatherapi.exceptions import IllegalGeoLocation

class Session:
    '''
    Session object for Cloudy UIs
    '''
    def __init__(self):
        self._cached_nws_data = None
        self._cached_weather_data = None

    @staticmethod
    def _validate_geodata(lat, lon) -> tuple[float, float]:
        return (float(lat), float(lon))

    def submit_geodata(self, lat, lon) -> Response:
        '''
        Session command to send lon, lat to API.
        '''
        try:
            lat, lon = self._validate_geodata(lat ,lon)
        except ValueError:
            return Response(
                success = False,
                err_message = "Longitude, Latitude must be numeric"
            )

        try:
            self._cached_nws_data: NWSData = from_geo(lat, lon)
        except IllegalGeoLocation:
            return Response(
                success = False,
                err_message = "This location does not have data provided by api.weather.gov"
            )
        
        self._cached_weather_data: Weather = self._cached_nws_data.get_forecast()
        # aliased only because the lines are long and unreadable without it
        weather = self._cached_weather_data
        return Response(
            success = True,
            temperature = weather.temperature,
            percipitation_chance = weather.percipitation_chance,
            wind_speed = weather.wind_speed,
            wind_direction = weather.wind_direction,
            short_forecast = weather.short_forecast,
            detailed_forecast = weather.detailed_forecast
        )
