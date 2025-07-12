'''
TUI/widgets/geodata_input.py

Widget for inputing geodata, supports Geodata and Geocoding look.
'''
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, Center
from textual.widget import Widget
from textual.widgets import Button, Input, Label

class WeatherButton(Widget):
    '''
    Button for sending data to weather api, and text section for error handle response.
    '''
    DEFAULT_CSS = '''
        Button {
            margin-top: 1;
        }
    '''
    def compose(self) -> ComposeResult:
        yield Button(
            "Check Weather",
            id = "weather-input-button",
            variant = "success"
        )
        yield Label(
            "",
            id = "weather-button-error-label"
        )

class GeodataInput(Widget):
    '''Input form for selecting location.'''
    DEFAULT_CSS = """
    GeodataInput {
        height: 10;
    }
    Center {
        border: solid green;
    }
    """
    def compose(self) -> ComposeResult:
        with Center():
            with Horizontal():
                with Vertical():
                    yield Label("Latitude")
                    yield Input(
                        placeholder = "lat",
                        id = "latitude-input",
                        type = "number"
                    )

                    yield Label("Longitude")
                    yield Input(
                        placeholder="lon",
                        id = "longitude-input",
                        type = "number"
                    )
                with Vertical():
                    yield WeatherButton()
