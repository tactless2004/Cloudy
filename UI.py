from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Label
from textual.containers import HorizontalGroup, Center
from weatherapi import from_geo
from weatherapi.exceptions import IllegalGeoLocation
from TUI.widgets import DaySelector, GeodataInput

class InputApp(App):

    def compose(self) -> ComposeResult:
        DaySelector()
        GeodataInput()
        output_label = Label("", id = "output-label")
        output_label.styles.height = 20
        output_label.styles.width = 50
        output_label.styles.text_align = "center"
        yield output_label

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "weather-input-button":
            # Grab lat, lon values 
            # catch Value Error if the fields are left empty
            try:
                lat = float(self.query_one("#lat", Input).value)
                lon = float(self.query_one("#lon", Input).value)
            except ValueError:
                self.query_one(
                    "#weather-button-error-label",
                    Label
                ).update("Latitude, Longitude must be numeric")
                return

            # Grab NWS api data, and display
            try:
                nws = from_geo(
                    lat = lat,
                    lon = lon
                )
                w = nws.get_forecast()
                self.query_one("#output-label", Label).update(str(w))
            except IllegalGeoLocation:
                self.query_one(
                    "#weather-button-error-label",
                    Label
                ).update(f"{lat}, {lon} is not recognized by the NWS")


if __name__ == "__main__":
    app = InputApp()
    app.run()
