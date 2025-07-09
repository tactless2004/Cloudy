from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import Button

class DaySelector(Widget):
    CSS_PATH = "day_selector.tcss"
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("Today", id = "day1-button"),
            Button("Tomorrow", id = "day2-button"),
            Button("Couple Days", id = "day3-button"),
            Button("Few Days", id = "day4-button"),
            Button("Several Days", id = "day5-button"),
            Button("Almost Week", id = "day6-button"),
            Button("In a Week", id = "day7-button")
        )
