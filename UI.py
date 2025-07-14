'''
UI.py

Textual UI for Cloudy
'''
# pylint: disable=C0103
from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Label, TabbedContent, TabPane
from textual.containers import Vertical, Center
from weatherapi import from_geo
from weatherapi.exceptions import IllegalGeoLocation
from TUI.widgets import DaySelector, GeodataInput
from session import Session, Response

OUTPUT_PLACEHOLDER = """Hello there!
The skies haven't spoken yet...
Hang tight while we check the clouds for you.
"""

class InputApp(App):
    '''textual UI for Cloudy'''
    DEFAULT_CSS = """
    Label {
        text-wrap: wrap;
    }
    Tabs{
        dock: top;
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
            with TabbedContent(initial="location-input-tab"):
                with TabPane("Geodata", id = "geodata-input-tab"):
                    yield GeodataInput()
                with TabPane("Location", id = "location-input-tab"):
                    yield Label("Placeholder")
            with Center():
                yield Label(
                    renderable = OUTPUT_PLACEHOLDER,
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

            # Display Response data (on success)
            self.query_one("#output-label", Label).update(
                f"{response.temperature}°F\n{response.wind_speed} -> {response.wind_direction}\n" +
                f"Precipitation {response.percipitation_chance}\n{response.short_forecast}"
            )

if __name__ == "__main__":
    app = InputApp()
    app.run()
