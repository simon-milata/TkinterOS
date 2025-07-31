import logging
import threading

from playsound import playsound

from tkinteros.applications.tictactoe.gui import TicTacToeGUI
from tkinteros.applications.tictactoe.bot import TicTacToeBot
import tkinteros.applications.tictactoe.game_logic as game_logic
from tkinteros.asset_management.asset_manager import AssetManager
from tkinteros.asset_management.assets import TictactoeAssets


class TicTacToeController:
    def __init__(self, asset_manager: AssetManager, appereance_mode):
        self.asset_manager = asset_manager
        self.appereance_mode = appereance_mode


    def run(self):
        self.create_variables()
        self.gui = TicTacToeGUI(start_callback=self.start_game, 
                                replay_callback=self.reset_game, 
                                asset_manager=self.asset_manager,
                                appereance_mode=self.appereance_mode)
        self.gui.run()


    def start_game(self, grid_size: int) -> None:
        logging.info("Game starting...")
        if grid_size:
            grid_size = int(grid_size.split("x")[0])
        else:
            grid_size = 3

        self.gui.hide_main_menu()
        self.gui.show_game_frame()
        self.bot = TicTacToeBot(random_start=False)
        self.gui.resize_game_border(grid_size=grid_size)
        self.create_board(rows=grid_size, columns=grid_size)


    def create_variables(self) -> None:
        self.bot_thinking = False
        self.player_1 = "X"
        self.player_2 = "O"
        self.current_player = self.player_1


    def on_click(self, row: int, column: int):
        if self.bot_thinking:
            return

        self.take_turn(row, column)
        playsound(self.asset_manager.get_sound(TictactoeAssets.PLAYER_MOVE_SOUND), block=False)

        self.bot_thinking = True
        self.gui.window.after(150, self.start_bot_move)


    def start_bot_move(self):
        threading.Thread(target=self.bot_turn, daemon=True).start()


    def bot_turn(self):
        row, column = self.bot.move(board=self.board_list)
        playsound(self.asset_manager.get_sound(TictactoeAssets.BOT_MOVE_SOUND), block=False)
        self.gui.window.after(0, lambda: self.finish_bot_turn(row, column))


    def finish_bot_turn(self, row, column):
        self.take_turn(row=row, column=column)
        self.bot_thinking = False


    def take_turn(self, row: int, column: int):
        self.board_list[row][column] = self.current_player
        self.gui.check_cell(row=row, column=column, player=self.current_player)
        
        self.print_board(self.board_list)

        winner = game_logic.evaluate_game_state(self.board_list)
        if winner:
            header = f"{winner.upper()} won!" if winner != "tie" else "Tie!"
            self.gui.hide_game_frame()
            self.gui.show_game_over_menu()
            self.gui.update_game_over_text(header)
            return
        
        self.switch_player()


    def reset_game(self):
        logging.info("Resetting game...")
        self.gui.hide_game_over_menu()
        self.gui.hide_game_frame()
        self.gui.show_main_menu()
        self.gui.destroy_board_buttons()

        self.current_player = self.player_1


    def bot_take_turn(self):
        row, column = self.bot.move(board=self.board_list)

        self.board_list[row][column] = self.current_player
        self.gui.check_cell(row=row, column=column, player=self.current_player)
        
        self.print_board(self.board_list)

        winner = game_logic.evaluate_game_state(self.board_list)
        if winner:
            header = f"{winner.upper()} won!" if winner != "tie" else "Tie!"
            self.gui.hide_game_frame()
            self.gui.show_game_over_menu()
            self.gui.update_game_over_text(header)
            return
        
        self.switch_player()
                

    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1
        

    def print_board(self, board: list):
        for row in board:
            logging.debug(row)
        logging.debug("")


    def create_board(self, rows=5, columns=5, empty_cell=" "):
        logging.info("Creating board...")
        self.board_list = [[empty_cell for _ in range(columns)] for _ in range(rows)]
        self.gui.create_board_grid(rows, columns, self.on_click)
