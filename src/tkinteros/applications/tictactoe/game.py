from tkinteros.applications.tictactoe.controller import TicTacToeController
from tkinteros.asset_management.asset_manager import AssetManager


class TicTacToe:
    def __init__(self, asset_manager, appereance_mode: str = "light"):
        TicTacToeController(asset_manager=asset_manager, appereance_mode=appereance_mode).run()


if __name__ == "__main__":
    TicTacToe(AssetManager("src/tkinteros/asset_management/assets"))