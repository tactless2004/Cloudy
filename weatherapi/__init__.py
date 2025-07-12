'''
Interface for the NWS API (api.weather.gov) to simplify use of freely available weather data.
'''
from weatherapi.core.nwsdata import NWSData
from weatherapi.util.data_utils import from_geo

__all__ = ["NWSData", "from_geo"]
