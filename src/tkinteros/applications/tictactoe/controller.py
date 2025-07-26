import logging

import customtkinter as ctk

from tkinteros.applications.tictactoe.gui import TicTacToeGUI
from tkinteros.applications.tictactoe.bot import TicTacToeBot
#from theme import THEME_COLORS


class TicTacToe:
    def __init__(self):
        pass


    def setup(self):
        self.create_variables()
        self.gui = TicTacToeGUI(start_callback=self.start_game, replay_callback=self.reset_game)
        self.gui.run()


    def start_game(self, grid_size):
        grid_size = int(grid_size.split("x")[0])

        self.gui.hide_main_menu()
        self.bot = TicTacToeBot(random_start=True, points_to_win=self.get_points_to_win(grid_size))
        self.create_board(rows=grid_size, columns=grid_size)


    def get_points_to_win(self, grid_size: int) -> int:
        if grid_size == 3:
            return 3
        elif grid_size == 5:
            return 4


    def create_variables(self):
        self.board_list = []
        self.button_list = []
        self.base_color1 = "#ffd36b"
        self.base_color2 = "#104b98"
        self.cell_size = 40
        self.player_1 = "X"
        self.player_2 = "O"
        self.empty_cell = " "
        self.current_player = self.player_1


    def on_click(self, button: ctk.CTkButton, row: int, column: int):
        self.gui.check_cell(cell_button=button, player=self.current_player)
        self.board_list[row][column] = self.current_player

        # self.print_board(self.board_list)

        grid_size = len(self.board_list)

        winner = self.evaluate_game_state(self.board_list, self.empty_cell, self.get_points_to_win(grid_size))
        if winner:
            header = f"{winner.upper()} won!" if winner != "tie" else "Tie!"
            self.gui.create_game_over_menu(header)
            return

        self.switch_player()
        self.bot_take_turn()


    def reset_game(self):
        self.gui.hide_game_over_menu()
        self.gui.show_main_menu()

        for row in self.button_list:
            for button in row:
                button.destroy()

        self.board_list = []
        self.button_list = []
        self.current_player = self.player_1


    def bot_take_turn(self):
        row, column = self.bot.move(board=self.board_list)

        self.board_list[row][column] = self.current_player
        button = self.button_list[row][column]
        self.gui.check_cell(cell_button=button, player=self.current_player)
        self.switch_player()
        # self.print_board(self.board_list)

        winner = self.evaluate_game_state(self.board_list, self.empty_cell, points_to_win=(self.get_points_to_win(len(self.board_list))))
        if winner:
            header = f"{winner.upper()} won!" if winner != "tie" else "Tie!"
            self.gui.create_game_over_menu(header)
            return


    def evaluate_winner(self, x_count: int, o_count: int, points_to_win: int = 4):
        if x_count >= points_to_win:
            return "X"
            
        elif o_count >= points_to_win:
            return "O"

        return None
    

    def evaluate_cell(self, cell: str, x_count: int, o_count: int):
        if cell == "X":
            return x_count + 1, 0
        if cell == "O":
            return 0, o_count + 1
        
        return 0, 0
    

    def is_draw(self, board_list: list[list[str]], empty_cell: str) -> bool:
        for row in board_list:
            for cell in row:
                if cell == empty_cell:
                    return False
        return True


    def evaluate_game_state(self, board_list: list, empty_cell: str = " ", points_to_win: int = 4):
        board_size = len(board_list)

        if self.is_draw(board_list, empty_cell):
            return "tie"
        
        # horizontal
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size):
                current_cell = board_list[i][j]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                winner = self.evaluate_winner(x_count, o_count, points_to_win)
                if winner:
                    return winner

        # vertical
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size):
                current_cell = board_list[j][i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                winner = self.evaluate_winner(x_count, o_count, points_to_win)
                if winner:
                    return winner

        # diagonal \\ up
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[j+i][j]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                winner = self.evaluate_winner(x_count, o_count, points_to_win)
                if winner:
                    return winner

        # diagonal \ down
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[j][j+i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                winner = self.evaluate_winner(x_count, o_count, points_to_win)
                if winner:
                    return winner
                
        # diagonal / left
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[board_size-j-i-1][j-i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                winner = self.evaluate_winner(x_count, o_count, points_to_win)
                if winner:
                    return winner

        # diagonal / right
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[board_size-j-1][j+i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                winner = self.evaluate_winner(x_count, o_count, points_to_win)
                if winner:
                    return winner
                

    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1
        

    def print_board(self, board: list):
        for row in board:
            print(row)
        print()    


    def create_board(self, rows: int = 5, columns: int = 5):
        logging.debug("Creating tictactoe board")
        x_pos = 0 - self.cell_size
        y_pos = 0 - self.cell_size

        color1 = self.base_color2
        color2 = self.base_color1

        for row in range(rows):
            self.board_list.append([])
            self.button_list.append([])

            y_pos += self.cell_size
            x_pos = 0 - self.cell_size

            color1, color2 = color2, color1

            for column in range(columns):
                self.board_list[row].append(self.empty_cell)

                x_pos += self.cell_size

                # Alternate color
                if column % 2 == 0:
                    color = color1
                else:
                    color = color2

                button = self.gui.create_grid_button(
                    color=color, row=row, column=column, x=x_pos, y=y_pos, 
                    cell_size=self.cell_size, callback=self.on_click)
                
                self.button_list[row].append(button)


if __name__ == "__main__":
    TicTacToe().setup()