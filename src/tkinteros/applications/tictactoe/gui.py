from typing import Callable
import random

import customtkinter as ctk

from tkinteros.theme import THEME_COLORS
from tkinteros.theme import THEME_FONTS
from tkinteros.asset_management.assets import TictactoeAssets


class TicTacToeGUI:
    def __init__(self, asset_manager, start_callback, replay_callback, appereance_mode):
        self.asset_manager = asset_manager
        self.appereance_mode = appereance_mode
        self.start_callback = start_callback
        self.replay_callback = replay_callback
        self.create_variables()
        self.create_window()
        self.create_background()
        self.create_main_menu()
        self.create_game_frame()
        self.create_game_over_menu()
        self.window.after(100, self.show_main_menu)
        
        
    def run(self):
        self.window.mainloop()


    def icon_setup(self):
        if self.appereance_mode:
            self.window.iconbitmap(self.asset_manager.get_icon(TictactoeAssets.ICON_LIGHT))
        else:
            self.window.iconbitmap(self.asset_manager.get_icon(TictactoeAssets.ICON_LIGHT))


    def create_game_frame(self):
        self.board_container = ctk.CTkFrame(
            master=self.window, bg_color=THEME_COLORS.primary, fg_color=THEME_COLORS.primary
        )

    
    def create_main_menu(self):
        self.main_menu_header = ctk.CTkLabel(
            self.window, text="Tic Tac Toe", 
            text_color=THEME_COLORS.font_color, 
            font=(THEME_FONTS.family_bold, THEME_FONTS.extra_large), 
            fg_color=THEME_COLORS.primary, bg_color=THEME_COLORS.primary
        )

        self.main_menu_subheader = ctk.CTkLabel(
            self.window, text_color=THEME_COLORS.font_color,
            font=(THEME_FONTS.family_bold, THEME_FONTS.small), text="❌⭕",
            fg_color=THEME_COLORS.primary, bg_color=THEME_COLORS.primary
        )
        
        self.main_menu_rows_label = ctk.CTkLabel(
            self.window, text="Grid Size", text_color=THEME_COLORS.font_color,
            font=(THEME_FONTS.family, THEME_FONTS.medium), 
            fg_color=THEME_COLORS.primary, bg_color=THEME_COLORS.primary
        )
        
        self.main_menu_row_input = ctk.CTkSegmentedButton(
            self.window, text_color=THEME_COLORS.button_font_color,  
            font=(THEME_FONTS.family, THEME_FONTS.medium), width=80,
            selected_hover_color=THEME_COLORS.button_hover, height=40,
            fg_color=THEME_COLORS.button, unselected_color=THEME_COLORS.button, 
            selected_color=THEME_COLORS.button_hover, values=["3x3", "5x5"], 
            unselected_hover_color=THEME_COLORS.button, bg_color=THEME_COLORS.primary
        )

        self.main_menu_play_button = ctk.CTkButton(
            self.window, text="▶ Play", text_color=THEME_COLORS.button_font_color, 
            fg_color=THEME_COLORS.button, bg_color=THEME_COLORS.primary,
            command=lambda: self.start_callback(self.main_menu_row_input.get()),
            font=(THEME_COLORS.font_color, THEME_FONTS.button_font_size), 
            hover_color=THEME_COLORS.button_hover, width=150, height=50
        )


    def create_game_over_menu(self):
        self.game_over_text = ctk.CTkLabel(
            self.window, text="", text_color=THEME_COLORS.font_color,
            font=(THEME_FONTS.family_bold, THEME_FONTS.large), 
            bg_color=THEME_COLORS.primary, fg_color=THEME_COLORS.primary
        )
        
        self.play_again_button = ctk.CTkButton(
            self.window, text="Play Again", fg_color=THEME_COLORS.button, bg_color=THEME_COLORS.primary,
            text_color=THEME_COLORS.button_font_color, hover_color=THEME_COLORS.button_hover,
            font=(THEME_FONTS.family_bold, THEME_FONTS.button_font_size), command=self.replay_callback
        )
        

    def update_game_over_text(self, text: str):
        self.game_over_text.configure(text=text)


    def show_main_menu(self):
        self.main_menu_header.place(anchor="n", relx=0.5, rely=0.05)
        self.main_menu_subheader.place(anchor="n", relx=0.5, rely=0.25)
        self.main_menu_rows_label.place(anchor="center", relx=0.5, rely=0.52)
        self.main_menu_row_input.place(anchor="center", relx=0.5, rely=0.65)
        self.main_menu_play_button.place(anchor="center", relx=0.5, rely=0.85)


    def show_game_frame(self):
        self.board_container.place(relx=0.5, rely=0.5, anchor="center")


    def show_game_over_menu(self):
        self.game_over_text.place(anchor="n", relx=0.5, rely=0.05)
        self.play_again_button.place(anchor="center", relx=0.5, rely=0.7)

    
    def hide_game_frame(self):
        self.board_container.place_forget()


    def hide_main_menu(self):
        self.main_menu_header.place_forget()
        self.main_menu_subheader.place_forget()
        self.main_menu_rows_label.place_forget()
        self.main_menu_row_input.place_forget()
        self.main_menu_play_button.place_forget()


    def hide_game_over_menu(self):
        self.game_over_text.place_forget()
        self.play_again_button.place_forget()


    def check_cell(self, row: int, column: int, player: str):
        self.buttons[row][column].configure(text=player, state="disabled")


    def create_variables(self):
        self.cell_size = 60
        self.window_width = 400
        self.window_height = 400
        

    def create_window(self) -> None:
        self.window = ctk.CTkToplevel(fg_color=THEME_COLORS.primary)
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height))
        self.window.title("Tic Tac Toe")
        self.window.attributes("-topmost", True)
        self.window.focus_force()
        self.window.resizable(False, False)
        self.window.after(200, self.icon_setup)


    def create_background(self):
        cell_size = self.window_width // 10
        delay = 0

        for row in range(10):
            for col in range(10):
                delay += row * 8
                x = col * cell_size
                y = row * cell_size

                cell = ctk.CTkButton(
                    master=self.window, font=(THEME_FONTS.family, THEME_FONTS.small),
                    width=cell_size, height=cell_size, text_color=THEME_COLORS.off,
                    border_color=THEME_COLORS.primary, bg_color=THEME_COLORS.primary,
                    fg_color=THEME_COLORS.primary, text=random.choice(["X", "O"])
                )

                self.window.after(
                    delay,
                    lambda c=cell, x=x, y=y: self.place_background_button(cell=c, x=x, y=y)
                )


    def place_background_button(self, cell, x, y):
        cell.place(x=x, y=y)


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
                    master=self.board_container, width=cell_size, height=cell_size, 
                    text_color_disabled="black", fg_color=color, corner_radius=0,
                    text="", font=(THEME_FONTS.family_bold, THEME_FONTS.medium)
                )
        button.configure(command=lambda r=row, c=column: click_callback(row=r, column=c))

        button.grid(row=row, column=column)

        return button
    

    def destroy_board_buttons(self):
        for row in self.buttons:
            for button in row:
                button.destroy()