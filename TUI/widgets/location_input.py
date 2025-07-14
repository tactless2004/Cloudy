'''Widget for location input'''
from textual.app import ComposeResult
from textual.widgets import Label, Button, Input
from textual.containers import Vertical, Horizontal
from textual.widget import Widget

class LocationInput(Widget):
    '''
    Textual widget for inputing
    '''
    DEFAULT_CSS = '''
        LocationInput {
            border: solid blue;
            height: 6;
        }
        Button {
            margin-top: 1;
            margin-left: 1;
        }
        Vertical {
            width: 1fr;
        }
        #location-error-label {
            margin-top: 1;
        }
    '''
    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield Label("Location", id = "location-label")
                yield Input(placeholder = "City, State, County", id = "location-input")
            with Vertical():
                yield Button(
                    "Check Weather",
                    id = "weather-input-button-location",
                    variant = "primary"
                )
            with Vertical():
                yield Label("", id = "location-error-label")
