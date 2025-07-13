'''
UI.py

Textual UI for Cloudy
'''
# pylint: disable=C0103
from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Label
from textual.containers import Vertical, Center
from weatherapi import from_geo
from weatherapi.exceptions import IllegalGeoLocation
from TUI.widgets import DaySelector, GeodataInput
from session import Session, Response

class InputApp(App):
    '''textual UI for Cloudy'''
    DEFAULT_CSS = """
    Label {
        text-wrap: wrap;
    }
    #output-label {
        border: solid green;
    }
    """

    def compose(self) -> ComposeResult:
        # It's bad to define self characteristics outside of __init__(),
        # but it makes sense here.
        self.session = Session()
        with Vertical():
            yield GeodataInput()
            yield DaySelector()
            with Center():
                yield Label(
                    renderable = "Hello there!\nThe skies haven't spoken yet..." +
                    "\nHang tight while we check the clouds for you.",
                    id = "output-label"
                )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        '''Behavior for button events'''
        if event.button.id == "weather-input-button":
            # Grab lat, lon values
            lat = self.query_one("#latitude-input", Input).value
            lon = self.query_one("#longitude-input", Input).value
            response: Response = self.session.submit_geodata(lat, lon)

            # If request is unsuccesful display the response err_message
            if not response.success and response.err_message:
                self.query_one(
                    "#weather-button-error-label",
                    Label
                ).update(response.err_message)
                return

            # Grab NWS api data, and display
            self.query_one("#output-label", Label).update(
                f"{response.temperature}°F\n{response.wind_speed} -> {response.wind_direction}\n" +
                f"Precipitation {response.percipitation_chance}\n{response.short_forecast}"
            )

if __name__ == "__main__":
    app = InputApp()
    app.run()
