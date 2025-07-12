'''
Interface for the NWS API (api.weather.gov) to simplify use of freely available weather data.
'''
from weatherapi.nwsdata import NWSData
from weatherapi.data_utils import from_geo

__all__ = [NWSData, from_geo]