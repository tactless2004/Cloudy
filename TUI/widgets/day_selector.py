'''
TUI/widgets/day_selector.py

Widget for selecting the day, dynamically changed based on the current day.
'''
from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Button

class DaySelector(Center):
    '''Textual Widget for selecting the day (WIP)'''
    DEFAULT_CSS = """
    Button {
        margin-right: 5;
    }
    """
    def compose(self) -> ComposeResult:
        yield Button(
            "Today",
            id = "day1-button",
            variant = "primary"
        )
        yield Button(
            "Tomorrow",
            id = "day2-button",
            variant = "primary"
        )
