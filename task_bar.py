from datetime import datetime
from PIL import Image

import customtkinter as ctk

from styles import desktop_colors, desktop_highlight_colors

class TaskBar:
    def __init__(self, os, gui) -> None:
        self.os = os
        self.gui = gui

        self.create_variables()
        self.icon_setup()
        self.create_taskbar()
        self.create_start_menu()
        self.create_time_date()
        

    def create_variables(self):
        self.WINDOW = self.gui.WINDOW
        self.width = self.gui.width
        self.height = self.gui.height

    
    def icon_setup(self) -> None:
        self.python_icon = ctk.CTkImage(Image.open("assets/python_icon.png"), size=(40, 40))
        self.snake_icon = ctk.CTkImage(light_image=Image.open("assets/snake_blue_icon.png"), dark_image=Image.open("assets/snake_yellow_icon.png"), size=(32, 32))

    
    def create_taskbar(self) -> None:
        self.taskbar = ctk.CTkFrame(self.WINDOW, height=45, width=self.width, fg_color=desktop_colors, corner_radius=0)
        self.taskbar.place(anchor="s", relx=0.5, rely=1)

        self.taskbar_app_frame = ctk.CTkFrame(self.taskbar, fg_color="transparent")
        self.taskbar_app_frame.place(anchor="center", relx=0.5, rely=0.5)

        self.start_button = ctk.CTkButton(self.taskbar, text="", image=self.python_icon, width=45, height=45, fg_color="transparent", 
                                          command=self.os.start_menu_mechanism, hover_color=desktop_highlight_colors)
        self.start_button.place(anchor="w", relx=0, rely=0.5)

        self.create_default_taskbar_apps()


    def create_start_menu(self) -> None:
        self.start_menu_frame = ctk.CTkFrame(self.WINDOW, width=self.width/6, height=self.height/4)
        self.start_menu_frame.pack_propagate(False)

        self.shut_down_button = ctk.CTkButton(self.start_menu_frame, width=self.width/20, height=self.height/20, text="Shut down", command=self.os.quit)
        self.shut_down_button.pack()
        self.restart_button = ctk.CTkButton(self.start_menu_frame, width=self.width/20, height=self.height/20, text="Restart", command=self.os.restart)
        self.restart_button.pack()


    def create_time_date(self):
        self.time_date_frame = ctk.CTkFrame(self.taskbar, width=self.width/20, height=45, fg_color="transparent")
        self.time_date_frame.place(anchor="e", relx=1, rely=0.5)

    
    def create_default_taskbar_apps(self):
        self.python_game_frame = ctk.CTkFrame(self.taskbar_app_frame, fg_color="transparent")
        self.python_game_frame.pack(padx=self.width/30)
        self.python_game_button = ctk.CTkButton(self.python_game_frame, command=lambda: self.os.play_game("python"), width=45, height=45, text="", 
                                                image=self.snake_icon, fg_color="transparent", hover_color=desktop_highlight_colors)
        self.python_game_button.place(anchor="center", relx=0.5, rely=0.5)