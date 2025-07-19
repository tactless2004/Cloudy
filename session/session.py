'''
Session state for Cloudy UIs
'''
from session.messages import Response
from weatherapi.core import NWSData, Weather
from weatherapi.util import from_geo, from_location
from weatherapi.exceptions import IllegalGeoLocation, InvalidLocation

class Session:
    '''
    Session object for Cloudy UIs
    '''
    def __init__(self):
        self._cached_nws_data: NWSData
        self._cached_weather_data: Weather

    @staticmethod
    def _validate_geodata(lat, lon) -> tuple[float, float]:
        return (float(lat), float(lon))

    @staticmethod
    def _generate_valid_response(weather: Weather):
        return Response(
            success = True,
            temperature = weather.temperature,
            percipitation_chance = weather.percipitation_chance,
            wind_speed = weather.wind_speed,
            wind_direction = weather.wind_direction,
            short_forecast = weather.short_forecast,
            detailed_forecast = weather.detailed_forecast
        )

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
            self._cached_nws_data = from_geo(lat, lon)
        except IllegalGeoLocation:
            return Response(
                success = False,
                err_message = "This location does not have data provided by api.weather.gov"
            )

        self._cached_weather_data = self._cached_nws_data.get_forecast()
        return self._generate_valid_response(self._cached_weather_data)

    def submit_location(self, location) -> Response:
        '''
        Session command to send location to WeatherAPI using geocoder.
        '''
        try:
            self._cached_nws_data = from_location(location)
        except IllegalGeoLocation:
            return Response(
                success = False,
                err_message = f"{location} is not supported by api.weather.gov"
            )
        except InvalidLocation:
            return Response(
                success = False,
                err_message = f"Geocoder could not resolve {location}"
            )

        self._cached_weather_data = self._cached_nws_data.get_forecast()
        return self._generate_valid_response(self._cached_weather_data)
