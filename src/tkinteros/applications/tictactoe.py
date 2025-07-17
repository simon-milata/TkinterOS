import customtkinter as ctk

#from theme import THEME_COLORS


class TicTacToe:
    def __init__(self):
        self.window_width = 400
        self.window_height = 400
        self.box_size = 40
        self.base_color1 = "#ffd36b"
        self.base_color2 = "#104b98"
        self.board_list = []
        self.player_1 = "X"
        self.player_2 = "O"
        self.empty_cell = " "
        self.current_player = self.player_1

        self.create_window()
        self.generate_board()
        self.window.mainloop()


    def create_window(self) -> None:
        self.window = ctk.CTkToplevel()
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height))
        self.window.configure(fg_color="gray")
        self.window.title("python game")
        self.window.attributes("-topmost", True)
        self.window.focus_force()
        self.window.resizable(False, False)
        # self.window.after(200, self.icon_setup)


    def on_click(self, button: ctk.CTkButton, row: int, column: int):
        button.configure(text=self.current_player, state="disabled")
        self.board_list[row][column] = self.current_player
        self.print_board(self.board_list)
        if self.evaluate_game_state(self.board_list):
            self.window.destroy()
        self.switch_player()


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
    

    def check_draw(self, board_list: list[list[str]]) -> bool:
        for row in board_list:
            for cell in row:
                if cell == self.empty_cell:
                    return False
        print("DRAW")
        return True


    def evaluate_game_state(self, board_list: list, board_size: int = 5):
        if self.check_draw(board_list):
            return "draw"
        
        # vertical
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size):
                current_cell = board_list[i][j]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("vertical")
                    return self.evaluate_winner(x_count, o_count)

        # parallel
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size):
                current_cell = board_list[j][i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("parallel")
                    return self.evaluate_winner(x_count, o_count)

        # diagonal \ up
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[j+i][j]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("diagonal \ up")
                    return self.evaluate_winner(x_count, o_count)

        # diagonal \ down
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[j][j+i]
                x_count, o_count = self.evaluate_cell(current_cell, x_count, o_count)

                if self.evaluate_winner(x_count, o_count):
                    print("diagonal \ down")
                    return self.evaluate_winner(x_count, o_count)
                
        # diagonal / left
        for i in range(board_size):
            x_count = 0
            o_count = 0
            for j in range(board_size-i):
                current_cell = board_list[board_size-j-1][j-i]
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


    def generate_board(self, rows: int = 5, columns: int = 5):
        x_pos = 0 - self.box_size
        y_pos = 0 - self.box_size

        color1 = self.base_color2
        color2 = self.base_color1

        for row in range(rows):
            self.board_list.append([])
            y_pos += self.box_size
            x_pos = 0 - self.box_size

            color1, color2 = color2, color1

            for column in range(columns):
                self.board_list[row].append(self.empty_cell)

                x_pos += self.box_size

                button = ctk.CTkButton(
                    self.window, width=self.box_size, height=self.box_size, 
                    corner_radius=0, text="", text_color="red"
                )
                button.configure(command=lambda b=button, r=row, c=column: self.on_click(button=b, row=r, column=c))

                # Alternate color
                if column % 2 == 0:
                    button.configure(fg_color=color1)
                else:
                    button.configure(fg_color=color2)

                button.place(x=x_pos, y=y_pos)

TicTacToe()