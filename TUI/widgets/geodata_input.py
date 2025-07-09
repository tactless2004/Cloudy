from textual.app import ComposeResult, App
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Input, Label

class GeodataInput(App):
    CSS_PATH = "geodata_input.tcss"
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Input("lon", id = "longitude-input"),
                Input("lat", id = "latitude-input")
            ),
            Vertical(
                Button("Check Weather", id = "check-weather-button"),
                Label("placeholder")
            )
        )

if __name__ == "__main__":
    app = GeodataInput()
    app.run()
