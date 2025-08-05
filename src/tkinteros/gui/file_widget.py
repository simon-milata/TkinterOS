from typing import Callable

from PIL import Image
import customtkinter as ctk

from tkinteros.file_management.file import File
from tkinteros.theme import THEME_COLORS


class TextFileWidget:
    def __init__(
            self, file: File, desktop_frame: ctk.CTkFrame, on_click_callback: Callable, 
            light_icon: Image, dark_icon: Image):
        self.icon = ctk.CTkImage(light_image=light_icon, dark_image=dark_icon, size=(50, 50))
        self.file = file
        self.on_click_callback = on_click_callback

        self.create_file_icon(desktop_frame)
        self.create_binds()


    def create_file_icon(self, desktop_frame):
        """Creates the body/icon of the file"""
        self.file_body_frame = ctk.CTkFrame(desktop_frame, width=75, height=100, fg_color="transparent")
        self.file_body_frame.place(x=self.file.x_pos, y=self.file.y_pos)

        self.file_body_button = ctk.CTkButton(
            self.file_body_frame, width=75, height=100, command=self.on_click, text="",
            image=self.icon, fg_color="transparent", bg_color="transparent", hover=False
        )
        self.file_body_button.place(anchor="center", relx=0.5, rely=0.5)

        self.file_body_name_label = ctk.CTkLabel(self.file_body_frame, width=75, height=20, text=self.file.name)
        self.file_body_name_label.place(anchor="center", relx=0.5, rely=0.9)


    def create_binds(self):
        self.file_body_frame.bind("<Enter>", self.hover_enter)
        self.file_body_frame.bind("<Leave>", self.hover_exit)
        self.file_body_button.bind("<Enter>", self.hover_enter)
        self.file_body_button.bind("<Leave>", self.hover_exit)
        self.file_body_name_label.bind("<Enter>", self.hover_enter)
        self.file_body_name_label.bind("<Leave>", self.hover_exit)


    def hover_enter(self, event=None):
        self.file_body_frame.configure(fg_color=THEME_COLORS.highlight)


    def hover_exit(self, event=None):
        self.file_body_frame.configure(fg_color="transparent")


    def on_click(self):
        self.on_click_callback(self.file.name)