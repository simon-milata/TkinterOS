from enum import Enum, auto


class Callback(Enum):
    TOGGLE_START_MENU = auto()
    TOGGLE_SYSTEM_TRAY_MENU = auto()
    TOGGLE_NETWORK = auto()
    QUIT = auto()
    RESTART = auto()
    PYBROWSE = auto()
    PYTHON = auto()