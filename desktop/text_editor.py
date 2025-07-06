from collections.abc import Callable

import customtkinter as ctk


class TextEditor:
    def __init__(self, name: str, file_content: str, on_close_callback: Callable[[str, str], None]):
        self.name = name
        self.file_content = file_content
        self.on_close_callback = on_close_callback

        self.open_file()


    def open_file(self):
        self.file_window = ctk.CTkToplevel()
        self.file_window.attributes("-topmost", True)
        self.file_textbox = ctk.CTkTextbox(self.file_window)
        self.file_textbox.pack(expand=True, fill="both")
        self.file_textbox.insert(0.0, self.file_content)

        self.file_window.protocol("WM_DELETE_WINDOW", self.close)


    def close(self):
        updated_content = self.file_textbox.get(0.0, "end-1c")
        self.on_close_callback(self.name, updated_content)
        self.file_window.destroy()
        