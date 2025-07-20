'''
UI.py

Textual UI for Cloudy
'''
# pylint: disable=C0103
# Justification: making python files non-snake-case is poor form.
# I might change it later, but for now ignore
from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Static, TabbedContent, TabPane, Markdown
from textual.containers import Vertical, Center
from TUI.widgets import LocationInput, GeodataInput
from session import Session

OUTPUT_PLACEHOLDER = """☁️ No forecast yet…\n
Pick a place to see what the sky’s up to. 🌦️
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
                yield Markdown(
                    markdown = OUTPUT_PLACEHOLDER,
                    id = "output-markdown"
                )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        '''Behavior for button events'''
        # Define up here so its in the scope of the whole function
        response = None
        location = ""
        if event.button.id == "weather-input-button-geodata":
            # Grab lat, lon values
            lat = self.query_one("#latitude-input", Input).value
            lon = self.query_one("#longitude-input", Input).value
            location = f"{lat}, {lon}"
            response = self.session.submit_geodata(lat, lon)

            # If request is unsuccesful display the response err_message
            if not response.success and response.err_message:
                self.query_one(
                    "#weather-button-error-label",
                    Static
                ).update(response.err_message)
                return

            # On success reset error text
            self.query_one("#weather-button-error-label", Static).update("")

        elif event.button.id == "weather-input-button-location":
            location = self.query_one("#location-input", Input).value
            response = self.session.submit_location(location)

            # If request is unsuccesful display the response err_message
            if not response.success and response.err_message:
                self.query_one(
                    "#location-error-label",
                    Static
                ).update(response.err_message)
                return
            # On success reset error text
            self.query_one("#location-error-label", Static).update("")

        # Display Response data (on success)
        if response:
            self.query_one("#output-markdown", Markdown).update(
                f"""Weather Forecast\n
Location       : {location}\n
Temperature    : {response.temperature}°F\n
Conditions     : {response.short_forecast}\n
Precipitation  : {response.percipitation_chance}\n
Wind           :
{response.wind_speed}{" -> " + response.wind_direction if response.wind_direction else ""}\n
"""
            )

if __name__ == "__main__":
    app = InputApp()
    app.run()
