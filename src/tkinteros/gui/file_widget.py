import customtkinter as ctk

from PIL import Image


class TextFileWidget:
    def __init__(self, File: object, desktop_frame, on_click_callback, icon):
        self.icon = icon
        self.file = File
        self.on_click_callback = on_click_callback

        self.create_file_icon(desktop_frame)


    def create_file_icon(self, desktop_frame):
        """Creates the body/icon of the file"""
        file_body_frame = ctk.CTkFrame(desktop_frame, width=75, height=100)
        file_body_frame.place(x=self.file.x_pos, y=self.file.y_pos)
        file_body_button = ctk.CTkButton(
            file_body_frame, width=75, height=100, command=self.on_click, text="",
            image=ctk.CTkImage(self.icon, size=(50, 50)), fg_color="transparent"
        ) # TODO: replace placeholder image
        file_body_button.place(anchor="center", relx=0.5, rely=0.5)
        file_body_name_label = ctk.CTkLabel(file_body_frame, width=75, height=20, text=self.file.name)
        file_body_name_label.place(anchor="center", relx=0.5, rely=0.9)


    def on_click(self):
        self.on_click_callback(self.file.name)