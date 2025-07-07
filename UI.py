from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Label
from textual.containers import HorizontalGroup
from weatherapi import from_geo

class InputApp(App):
    def compose(self) -> ComposeResult:
        yield Button(
            "Check Weather",
            id = "weather-input-button",
            variant = "success"
        )
        yield Input(
            placeholder = "Latitude",
            id = "lat",
            type = "number"
        )
        yield Input(
            placeholder = "Longitude",
            id = "lon",
            type = "number"
        )
        yield Label("Placeholder", id = "output-label")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "weather-input-button":
            lat = float(self.query_one("#lat", Input).value)
            lon = float(self.query_one("#lon", Input).value)
            nws = from_geo(
                lat = lat,
                lon = lon
            )
            w = nws.get_forecast()
            self.query_one("#output-label", Label).update(str(w))
            

if __name__ == "__main__":
    app = InputApp()
    app.run()
