import logging

import customtkinter as ctk

from .pybrowse_game import PyBrowseGame
from theme import THEME_COLORS, THEME_FONTS

class PyBrowse:
    def __init__(self, os, os_window: ctk.CTk) -> None:
        self.OS = os
        self.OS_WINDOW = os_window
        self.create_variables()
        self.create_window()
        self.create_window_bar()
        self.create_no_internet_gui()
        self.create_internet_gui()


    def create_variables(self) -> None:
        self.OS_WINDOW.update()
        self.WINDOW_HEIGHT = self.OS_WINDOW.winfo_screenheight()
        self.WINDOW_WIDTH = self.OS_WINDOW.winfo_screenwidth()
        self.game_running = False


    def create_window(self) -> None:
        self.WINDOW = ctk.CTkToplevel()
        self.WINDOW.configure(fg_color=THEME_COLORS.primary)
        self.WINDOW.title("PyBrowse")
        self.maximize_window()
        self.WINDOW.focus_set()
        self.WINDOW.attributes("-topmost", True)
        self.WINDOW.resizable(False, False)

        self.WINDOW.after(200, self.icon_setup)


    def maximize_window(self):
        try:
            self.WINDOW.state("zoom")
        except Exception:
            try:
                self.WINDOW.attributes("-zoomed", True)
            except Exception:
                logging.debug("Fullscreen not supported.")
                self.WINDOW.geometry(f"{int(self.WINDOW_WIDTH//1.01)}x{int(self.WINDOW_HEIGHT//1.01)}+0+0")
                self.WINDOW.update_idletasks()

    
    def icon_setup(self):
        if self.OS.appearance_mode:
            self.WINDOW.iconbitmap("src/Assets/pybrowse/pybrowse.ico")
        else:
            self.WINDOW.iconbitmap("src/Assets/pybrowse/pybrowse_dark.ico")


    def create_window_bar(self) -> None:
        self.window_bar_frame = ctk.CTkFrame(self.WINDOW, fg_color=THEME_COLORS.font_color, corner_radius=0, width=self.WINDOW_WIDTH, height=50)
        self.window_bar_frame.place(anchor="n", relx=0.5, rely=0)

    
    def create_no_internet_gui(self) -> None:
        self.no_internet_frame = ctk.CTkFrame(self.WINDOW, fg_color="transparent")

        self.game_frame = ctk.CTkFrame(self.no_internet_frame, fg_color="transparent", width=int(self.WINDOW_WIDTH/2.5), height=int(self.WINDOW_HEIGHT * 0.2), border_color=THEME_COLORS.button, border_width=3)
        self.game_frame.grid()

        self.pybrowse_game = PyBrowseGame(self, self.WINDOW, self.game_frame)

        self.WINDOW.bind("<space>", self.start_pybrowse_game)

        no_internet_label = ctk.CTkLabel(self.no_internet_frame, text="No internet", font=(THEME_FONTS.family, THEME_FONTS.big), text_color=THEME_COLORS.font_color)
        no_internet_label.grid()


    def start_pybrowse_game(self, event) -> None:        
        self.WINDOW.unbind("<space>")
        self.pybrowse_game.start_game()

    def create_internet_gui(self) -> None:
        pass
    

