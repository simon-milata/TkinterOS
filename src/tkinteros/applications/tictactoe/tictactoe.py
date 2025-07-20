from copy import deepcopy

import customtkinter as ctk

from tkinteros.applications.tictactoe.tictactoe_gui import TicTacToeGUI
from tkinteros.applications.tictactoe.tictactoe_bot import TicTacToeBot
#from theme import THEME_COLORS


class TicTacToe:
    def __init__(self):
        pass


    def run(self):
        self.create_variables()
        self.gui = TicTacToeGUI()
        self.bot = TicTacToeBot()
        self.create_board()
        self.gui.run()


    def create_variables(self):
        self.board_list = []
        self.button_list = []
        self.box_size = 40
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

        self.print_board(self.board_list)

        if self.evaluate_game_state(self.board_list, self.empty_cell):
            # TODO: end game
            self.gui.window.destroy()
        self.switch_player()
        self.bot_take_turn()


    def bot_take_turn(self):
        row, column = self.bot.move(board_list=self.board_list)

        print(row, column)

        self.board_list[row][column] = self.current_player
        button = self.button_list[row][column]
        self.gui.check_cell(cell_button=button, player=self.current_player)
        self.switch_player()
        self.print_board(self.board_list)
        self.evaluate_game_state(board_list=self.board_list)


    def evaluate_winner(self, x_count: int, o_count: int, points_to_win: int = 3):
        if x_count >= points_to_win:
            print("X WON")
            return "X"
            
        elif o_count >= points_to_win:
            print("O WON")
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
        print("DRAW")
        return True


    def evaluate_game_state(self, board_list: list, empty_cell: str = " ", board_size: int = 5):
        if self.is_draw(board_list, empty_cell):
            return "draw"
        
        # horizontal
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size):
                current_cell = board_list[i][j]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("horizontal")
                    return self.evaluate_winner(x_count, o_count)

        # vertical
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size):
                current_cell = board_list[j][i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("vertical")
                    return self.evaluate_winner(x_count, o_count)

        # diagonal \\ up
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[j+i][j]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("diagonal \\ up")
                    return self.evaluate_winner(x_count, o_count)

        # diagonal \ down
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[j][j+i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("diagonal \\ down")
                    return self.evaluate_winner(x_count, o_count)
                
        # diagonal / left
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[board_size-j-i-1][j-i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("diagonal / up")
                    return self.evaluate_winner(x_count, o_count)

        # diagonal / right
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[board_size-j-1][j+i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("diagonal / down")
                    return self.evaluate_winner(x_count, o_count)
                

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
        print("Creating board")
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
    TicTacToe().run()