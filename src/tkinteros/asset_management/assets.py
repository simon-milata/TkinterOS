from enum import StrEnum

class DesktopAssets(StrEnum):
    NO_INTERNET = "desktop/no_internet_icon.png"
    PYBROWSE = "desktop/pybrowse_icon.png"
    START_LOGO = "desktop/python_icon.png"
    BACKGROUND_LOGO = "desktop/python_logo.png"
    SNAKE_GAME = "desktop/snake_icon.png"
    WIFI_ICON = "desktop/wifi_icon.png"
    TEXT_FILE = "desktop/text_file_icon.png"
    TICTACTOE = "desktop/tictactoe_icon.png"
    ERROR_SOUND = "desktop/error_sound.mp3"
    TEXT_FILE_ICON = "desktop/text_file_icon.ico"


class PyBrowseAssets(StrEnum):
    PYBROWSE_GAME_SNAKE = "pybrowse/snake.png"
    PYBROWSE_ICON = "pybrowse/pybrowse.ico"


class SnakeGameAssets(StrEnum):
    MUNCH_SOUND = "python_game/munch_sound.mp3"
    SNAKE_GAME_ICON = "python_game/snake_icon.ico"


class TictactoeAssets(StrEnum):
    ICON = "tictactoe/icon.ico"
    PLAYER_MOVE_SOUND = "tictactoe/player_move.mp3"
    BOT_MOVE_SOUND = "tictactoe/bot_move.mp3"