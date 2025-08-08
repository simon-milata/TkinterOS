from typing import Callable

from PIL import Image
import customtkinter as ctk

from tkinteros.file_management.file import File
from tkinteros.theme import THEME_COLORS


class TextFileWidget:
    def __init__(
            self, file: File, desktop_frame: ctk.CTkFrame, on_click_callback: Callable, 
            hover_callback: Callable, hover_exit_callback: Callable, on_move_callback: Callable,
            light_icon: Image, dark_icon: Image):
        self.file = file
        self.on_click_callback = on_click_callback
        self.hover_callback = hover_callback
        self.hover_exit_callback = hover_exit_callback
        self.on_move_callback = on_move_callback
        self.light_icon = light_icon
        self.dark_icon = dark_icon

        self.create_file_widget(desktop_frame)
        self.create_hover_binds()
        self.create_callback_binds()


    def create_file_widget(self, desktop_frame):
        """Creates the body/icon of the file"""
        self.frame = ctk.CTkFrame(desktop_frame, width=80, height=100, fg_color="transparent")
        self.frame.place(x=self.file.x_pos, y=self.file.y_pos)
        self.frame.propagate(False)

        image = ctk.CTkImage(light_image=self.light_icon, dark_image=self.dark_icon, size=(50, 50))

        self.image_label = ctk.CTkLabel(
            master=self.frame, image=image, text="",
            fg_color="transparent", bg_color="transparent"
        )
        self.image_label.place(anchor="center", relx=0.5, rely=0.4)

        self.name_label = ctk.CTkLabel(
            self.frame, text=self.truncate_file_name(self.file.name), height=20, fg_color="transparent"
        )
        self.name_label.place(anchor="center", relx=0.5, rely=0.85)


    def truncate_file_name(self, file_name: str, char_limit=12) -> str:
        if len(file_name) > char_limit:
            return file_name[:char_limit - 3] + "..."
        return file_name


    def create_hover_binds(self):
        self.frame.bind("<Enter>", self.hover_enter)
        self.frame.bind("<Leave>", self.hover_exit)
        self.frame.bind("<B1-Motion>", self.on_drag)
        self.frame.bind("<ButtonRelease-1>", self.on_b1_release)

        self.image_label.bind("<Enter>", self.hover_enter)
        self.image_label.bind("<Leave>", self.hover_exit)
        self.image_label.bind("<B1-Motion>", self.on_drag)
        self.image_label.bind("<ButtonRelease-1>", self.on_b1_release)

        self.name_label.bind("<Enter>", self.name_hover)
        self.name_label.bind("<Motion>", self.name_hover)
        self.name_label.bind("<Leave>", self.hover_exit)
        self.name_label.bind("<B1-Motion>", self.on_drag)
        self.name_label.bind("<ButtonRelease-1>", self.on_b1_release)


    def create_callback_binds(self):
        self.frame.bind("<Double-1>", self.on_click)
        self.image_label.bind("<Double-1>", self.on_click)
        self.name_label.bind("<Double-1>", self.on_click)


    def hover_enter(self, event):
        self.frame.configure(fg_color=THEME_COLORS.highlight)


    def name_hover(self, event):
        self.hover_enter(event=None)
        self.hover_callback(event, self.file.name)


    def hover_exit(self, event=None):
        self.frame.configure(fg_color="transparent")
        self.hover_exit_callback()


    def on_drag(self, event):
        x_pos = event.x_root - 40
        y_pos = event.y_root - 50
        self.frame.place(x=x_pos, y=y_pos)


    def on_b1_release(self, event):
        print("AAAA")
        self.on_move_callback(file_name=self.file.name, x_pos=event.x_root, y_pos=event.y_root)


    def on_click(self, event=None):
        self.on_click_callback(self.file.name)