'''Interfaces for geopy.gecoders.Nominatim'''
from geopy.geocoders import Nominatim
from geopy.location import Location

def geodata_to_location(lat, lon) -> str:
    '''
    Get location string from geodata
    '''
    # Intentionally don't specify input type to accept (int | float | str) for lat, lon
    lat = str(lat)
    lon = str(lon)

    coder = Nominatim(user_agent="cloudy")
    location = coder.reverse(f"{lat}, {lon}")

    if not location:
        return f"{lat}, {lon}"
    return str(location)

def location_to_displaylocation(location: str) -> str:
    '''
    Get full location display name from simple location strings
    '''
    coder = Nominatim(user_agent="cloudy")
    try:
        resp = coder.geocode(location)
        if isinstance(resp, Location):
            return resp.raw['display_name']
        raise RuntimeError(f"{resp} is {type(resp)}, should be geopy.location.Location")
    # pylint: disable=W0718
    # Regardless of the particular exception,
    except Exception:
        return location
