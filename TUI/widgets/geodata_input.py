from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widget import Widget
from textual.widgets import Button, Input, Label

class WeatherButton(Widget):
    CSS = '''
        Button {
            margin-top: 10px;
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
    DEFAULT_CSS = """
    GeodataInput {
        height: 10;
    }
    """
    def compose(self) -> ComposeResult:
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
