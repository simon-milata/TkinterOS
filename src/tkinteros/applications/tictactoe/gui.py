from typing import Callable

import customtkinter as ctk

from tkinteros.theme import THEME_COLORS
from tkinteros.theme import THEME_FONTS


class TicTacToeGUI:
    def __init__(self, start_callback, replay_callback):
        self.create_variables()
        self.create_window()
        self.start_callback = start_callback
        self.replay_callback = replay_callback
        self.create_main_menu()
        self.create_game_frame()
        self.create_game_over_menu()
        self.hide_game_over_menu()
        
        
    def run(self):
        print("running")
        self.window.mainloop()


    def create_game_frame(self):
        self.game_frame = ctk.CTkFrame(self.window, width=self.window_width, 
                                            height=self.window_height, fg_color=THEME_COLORS.primary)

    
    def create_main_menu(self):
        self.main_menu_frame = ctk.CTkFrame(self.window, width=self.window_width, 
                                            height=self.window_height, fg_color=THEME_COLORS.primary)
        self.main_menu_frame.pack()
        header = ctk.CTkLabel(self.main_menu_frame, text="Tic Tac Toe", text_color=THEME_COLORS.font_color, 
                              font=(THEME_COLORS.font_color, THEME_FONTS.large))
        header.place(anchor="n", relx=0.5, rely=0.05)
        
        rows_label = ctk.CTkLabel(self.main_menu_frame, text="Grid Size", text_color=THEME_COLORS.font_color,
                                  font=(THEME_FONTS.family, THEME_FONTS.big))
        rows_label.place(anchor="center", relx=0.5, rely=0.52)
        row_input = ctk.CTkSegmentedButton(self.main_menu_frame, text_color=THEME_COLORS.button_font_color, 
                                            font=(THEME_FONTS.family, THEME_FONTS.big), 
                                            selected_hover_color=THEME_COLORS.button_hover, 
                                            fg_color=THEME_COLORS.button, unselected_color=THEME_COLORS.button, 
                                            selected_color=THEME_COLORS.button_hover, values=["3x3", "5x5"], 
                                            unselected_hover_color=THEME_COLORS.button)
        row_input.place(anchor="center", relx=0.5, rely=0.62)

        play_button = ctk.CTkButton(self.main_menu_frame, text="Play", text_color=THEME_COLORS.button_font_color, 
                                    fg_color=THEME_COLORS.button, command=lambda: self.start_callback(row_input.get()),
                                    font=(THEME_COLORS.font_color, THEME_FONTS.button_font_size), hover_color=THEME_COLORS.button_hover)
        play_button.place(anchor="center", relx=0.5, rely=0.8)


    def create_game_over_menu(self):
        self.game_over_frame = ctk.CTkFrame(self.window, width=400, height=400, fg_color=THEME_COLORS.primary)
        self.game_over_frame.pack()
        self.game_over_text = ctk.CTkLabel(self.game_over_frame, text="", text_color=THEME_COLORS.font_color,
                                      font=(THEME_FONTS.family_bold, THEME_FONTS.large))
        self.game_over_text.place(anchor="n", relx=0.5, rely=0.05)
        play_again_button = ctk.CTkButton(self.game_over_frame, text="Play Again", fg_color=THEME_COLORS.button, 
                                          text_color=THEME_COLORS.button_font_color, hover_color=THEME_COLORS.button_hover,
                                          font=(THEME_FONTS.family_bold, THEME_FONTS.button_font_size), command=self.replay_callback)
        play_again_button.place(anchor="center", relx=0.5, rely=0.7)


    def update_game_over_text(self, text: str):
        self.game_over_text.configure(text=text)


    def show_main_menu(self):
        self.main_menu_frame.pack()


    def show_game_frame(self):
        self.game_frame.pack()


    def show_game_over_menu(self):
        self.game_over_frame.pack()

    
    def hide_game_frame(self):
        self.game_frame.pack_forget()


    def hide_main_menu(self):
        self.main_menu_frame.pack_forget()


    def hide_game_over_menu(self):
        self.game_over_frame.pack_forget()


    def check_cell(self, row: int, column: int, player: str):
        self.buttons[row][column].configure(text=player, state="disabled")


    def create_variables(self):
        self.cell_size = 80
        self.window_width = 400
        self.window_height = 400
        

    def create_window(self) -> None:
        self.window = ctk.CTkToplevel()
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height))
        self.window.configure(fg_color="gray")
        self.window.title("Tic Tac Toe")
        self.window.attributes("-topmost", True)
        self.window.focus_force()
        self.window.resizable(False, False)
        # self.window.after(200, self.icon_setup)


    def create_board_grid(self, rows: int, columns: int, click_callback: Callable):
        self.buttons = []
        for row in range(rows):
            button_row = []
            for col in range(columns):
                color = self.get_color_for_cell(row, col)
                button = self.create_grid_button(color=color, row=row, column=col, 
                                            cell_size=self.cell_size, click_callback=click_callback)
                button_row.append(button)
            self.buttons.append(button_row)
        return self.buttons


    def get_color_for_cell(self, row: int, col: int) -> str:
        color1 = THEME_COLORS.highlight[0]
        color2 = THEME_COLORS.highlight[1]
        return color1 if (row + col) % 2 == 0 else color2


    def create_grid_button(self, color: str, row: int, column: int, cell_size: int, click_callback: Callable):
        button = ctk.CTkButton(
                    self.game_frame, width=cell_size, height=cell_size, 
                    corner_radius=0, text="", text_color="red", fg_color=color
                )
        button.configure(command=lambda r=row, c=column: click_callback(row=r, column=c))

        button.grid(row=row, column=column)

        return button
