from textual.app import ComposeResult, App
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Button, Input, Label

class WeatherButton(Widget):
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
    CSS_PATH = "geodata_input.tcss"
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Input("lon", id = "longitude-input"),
                Input("lat", id = "latitude-input")
            ),
            Vertical(
                WeatherButton()
            )
        )
