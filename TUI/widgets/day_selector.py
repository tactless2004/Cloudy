'''
TUI/widgets/day_selector.py

Widget for selecting the day, dynamically changed based on the current day.
'''
from textual.app import ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Button

class DaySelector(HorizontalGroup):
    '''Textual Widget for selecting the day (WIP)'''
    DEFAULT_CSS = """
    GeodataInput {
        height: 1fr;
    }
    """
    def compose(self) -> ComposeResult:
        yield Button("Today", id = "day1-button")
        yield Button("Tomorrow", id = "day2-button")
        yield Button("Couple Days", id = "day3-button")
        yield Button("Few Days", id = "day4-button")
        yield Button("Several Days", id = "day5-button")
        yield Button("Almost Week", id = "day6-button")
        yield Button("In a Week", id = "day7-button")
