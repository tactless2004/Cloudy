'''
UI.py

Textual UI for Cloudy
'''
# Justification: making python files non-snake-case is poor form.
#                I might change it later, but for now ignore
# pylint: disable=C0103
from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Label, TabbedContent, TabPane
from textual.containers import Vertical, Center
from TUI.widgets import LocationInput, GeodataInput
from session import Session

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
    #output-label {
        border: solid green;
    }
    """
    def __init__(self):
        self.session = Session()
        super().__init__()
    def compose(self) -> ComposeResult:
        # It's bad to define self characteristics outside of __init__(),
        # but it makes sense here.
        with Vertical():
            with TabbedContent(initial="location-input-tab"):
                with TabPane("Location", id = "location-input-tab"):
                    yield LocationInput()
                with TabPane("Geodata", id = "geodata-input-tab"):
                    yield GeodataInput()
            with Center():
                yield Label(
                    renderable = OUTPUT_PLACEHOLDER,
                    id = "output-label"
                )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        '''Behavior for button events'''
        # Define up here so its in the scope of the whole function
        response = None
        if event.button.id == "weather-input-button-geodata":
            # Grab lat, lon values
            lat = self.query_one("#latitude-input", Input).value
            lon = self.query_one("#longitude-input", Input).value
            response = self.session.submit_geodata(lat, lon)

            # If request is unsuccesful display the response err_message
            if not response.success and response.err_message:
                self.query_one(
                    "#weather-button-error-label",
                    Label
                ).update(response.err_message)
                return
        elif event.button.id == "weather-input-button-location":
            location = self.query_one("#location-input", Input).value
            response = self.session.submit_location(location)

            # If request is unsuccesful display the response err_message
            if not response.success and response.err_message:
                self.query_one(
                    "#location-error-label",
                    Label
                ).update(response.err_message)
                return

        # Display Response data (on success)
        if response:
            self.query_one("#output-label", Label).update(
                f"{response.temperature}°F\n{response.wind_speed} -> {response.wind_direction}\n" +
                f"Precipitation {response.percipitation_chance}\n{response.short_forecast}"
            )

if __name__ == "__main__":
    app = InputApp()
    app.run()
