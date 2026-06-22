from typing import Literal
from dataclasses import dataclass

from tkinteros.asset_management.assets import PyBrowseAssets, SnakeGameAssets, TictactoeAssets


@dataclass
class App:
    name: str
    title: str
    app_type: Literal["Application", "Game", "File"]
    icon: str
    maximized: bool = False
    propagate: bool = True


@dataclass
class Apps:
    snake_game = App(name="python", title="Python", app_type="Game", icon=SnakeGameAssets.SNAKE_GAME_ICON)
    pybrowse = App(
        name="pybrowse", title="PyBrowse", app_type="Application", icon=PyBrowseAssets.PYBROWSE_ICON, 
        maximized=True, propagate=False
    )
    tictactoe = App(name="tictactoe", title="Tic Tac Toe", app_type="Game", icon=TictactoeAssets.ICON)

    app_list = [snake_game, pybrowse, tictactoe]


class AppConfig:
    def __init__(self):
        apps = Apps()
        app_list = apps.app_list

        self.mapping = {}

        for app in app_list:
            self.mapping[app.name] = app


app_config = AppConfig().mapping
