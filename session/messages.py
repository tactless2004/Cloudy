'''
Message definitions for communication between Cloudy UIs and Cloudy API Session
'''
# pylint: disable=R0902
from dataclasses import dataclass
from typing import Optional
@dataclass
class Response:
    '''
    Response message for Cloudy Session
    '''
    success: bool
    err_message: Optional[str] = None
    temperature: Optional[int] = None
    percipitation_chance: Optional[str] = None
    wind_speed: Optional[int] = None
    wind_direction: Optional[str] = None
    short_forecast: Optional[str] = None
    detailed_forecast: Optional[str] = None
