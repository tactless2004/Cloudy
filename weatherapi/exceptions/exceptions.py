'''
weatherapi/exceptions/exceptions.py

Exceptions for weatherapi project.
'''
class IllegalGeoLocation(Exception):
    '''
    IllegalGeoLocation is raised when (Longitude, Latitude) data is correct
    , but the location is not supported by api.weather.gov.
    '''

class InvalidLocation(Exception):
    '''
    InvalidLocation is raised when a location string passed to a geocoder is not
    recognized.
    '''
