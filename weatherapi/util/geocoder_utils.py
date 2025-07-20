from geopy.geocoders import Nominatim

def geodata_to_location(lat, lon) -> str:
    '''
    Get location string
    '''
    # Intentionally don't specify input type to accept (int | float | str) for lat, lon
    lat = str(lat)
    lon = str(lon)

    coder = Nominatim(user_agent="cloudy")
    location = coder.reverse(f"{lat}, {lon}")

    if not location:
        return f"{lat}, {lon}"
    return str(location)
