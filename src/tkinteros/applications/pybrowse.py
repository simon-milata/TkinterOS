import logging

import customtkinter as ctk

from tkinteros.applications.pybrowse_game import PyBrowseGame
from tkinteros.theme import THEME_COLORS, THEME_FONTS
from tkinteros.asset_management.asset_manager import AssetManager
from tkinteros.asset_management.assets import PyBrowseAssets

class PyBrowse:
    def __init__(self, os, master_frame: ctk.CTkFrame, asset_manager: AssetManager) -> None:
        self.OS = os
        self.asset_manager = asset_manager
        self.app_frame = master_frame
        self.create_variables()
        self.create_window()
        self.create_window_bar()
        self.create_no_internet_gui()
        self.create_internet_gui()


    def create_variables(self) -> None:
        self.app_frame.update()
        self.WINDOW_HEIGHT = self.app_frame.winfo_screenheight()
        self.WINDOW_WIDTH = self.app_frame.winfo_screenwidth()
        self.game_running = False


    def create_window(self) -> None:
        self.app_frame.configure(fg_color=THEME_COLORS.primary)

    
    def icon_setup(self):
        if self.OS.appearance_mode:
            self.app_frame.iconbitmap(self.asset_manager.get_icon(PyBrowseAssets.PYBROWSE_ICON))
        else:
            self.app_frame.iconbitmap(self.asset_manager.get_icon(PyBrowseAssets.PYBROWSE_ICON))


    def create_window_bar(self) -> None:
        self.window_bar_frame = ctk.CTkFrame(self.app_frame, fg_color=THEME_COLORS.font_color, corner_radius=0, width=self.WINDOW_WIDTH, height=50)
        self.window_bar_frame.place(anchor="n", relx=0.5, rely=0)

    
    def create_no_internet_gui(self) -> None:
        self.no_internet_frame = ctk.CTkFrame(self.app_frame, fg_color="transparent")

        self.game_frame = ctk.CTkFrame(self.no_internet_frame, fg_color="transparent", width=int(self.WINDOW_WIDTH/2.5), height=int(self.WINDOW_HEIGHT * 0.2), border_color=THEME_COLORS.button, border_width=3)
        self.game_frame.grid()

        self.pybrowse_game = PyBrowseGame(self, self.app_frame, self.game_frame, self.asset_manager)

        self.OS.desktop_gui.WINDOW.bind("<space>", self.start_pybrowse_game)

        no_internet_label = ctk.CTkLabel(self.no_internet_frame, text="No internet", font=(THEME_FONTS.family, THEME_FONTS.big), text_color=THEME_COLORS.font_color)
        no_internet_label.grid()


    def start_pybrowse_game(self, event) -> None:        
        self.OS.desktop_gui.WINDOW.unbind("<space>")
        self.pybrowse_game.start_game()

    def create_internet_gui(self) -> None:
        pass
    

