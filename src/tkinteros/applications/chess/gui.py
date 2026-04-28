import customtkinter as ctk

from tkinteros.theme import THEME_COLORS, THEME_FONTS


class ChessGUI:
    def __init__(self):
        self.create_window()
        self.create_game_frame()


    def create_window(self) -> None:
        self.window = ctk.CTkToplevel()
        self.window.geometry(str(480) + "x" + str(480))
        self.window.update()
        self.window.title("Chess")
        self.window.attributes("-topmost", True)
        self.window.focus_force()
        self.window.resizable(False, False)


    def create_game_frame(self):
        self.border_frame = ctk.CTkFrame(
            master=self.window, bg_color=THEME_COLORS.primary, fg_color="black",
            border_color="white", border_width=1
        )
        self.board_container = ctk.CTkFrame(
            master=self.border_frame, bg_color=THEME_COLORS.primary, fg_color=THEME_COLORS.button
        )
            
    
    def show_game_frame(self):
        self.border_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.board_container.place(relx=0.5, rely=0.5, anchor="center")
    
    
    def draw_board(self, board: list[str]):
        self.board_buttons = []

        color, prev_color = THEME_COLORS.primary, THEME_COLORS.button
        hov_color, prev_hov_col = THEME_COLORS.highlight, THEME_COLORS.button_hover

        for i  in range(len(board)):
            self.board_buttons.append([])

            color, prev_color = prev_color, color
            hov_color, prev_hov_col = prev_hov_col, hov_color

            for j in range(len(board)):
                cell_button = ctk.CTkButton(
                    master=self.window, font=(THEME_FONTS.family, THEME_FONTS.small),
                    width=60, height=60, text_color="red",
                    border_color=color, bg_color=color,
                    fg_color=color, text="",
                    hover_color=hov_color
                )
                color, prev_color = prev_color, color
                hov_color, prev_hov_col = prev_hov_col, hov_color

                cell_button.grid(row=i, column=j)
                self.board_buttons[i].append(cell_button)
                
    
    def draw_pieces(self, board: list[str]):
        for i, row in enumerate(board):
            for j, cell_piece in enumerate(row):
                color = "black" if cell_piece.startswith("B") else "white"
                self.board_buttons[i][j].configure(
                    text_color=color, text=cell_piece
                )


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    ChessGUI().run()