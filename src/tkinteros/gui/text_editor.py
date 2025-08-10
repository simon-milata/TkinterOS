from collections.abc import Callable

import customtkinter as ctk


class TextEditor:
    def __init__(self, name: str, file_content: str, icon,
                 on_close_callback: Callable[[str, str], None]):
        self.name = name
        self.file_content = file_content
        self.on_close_callback = on_close_callback
        self.icon = icon

        self.open_file()


    def open_file(self):
        self.file_window = ctk.CTkToplevel()
        self.file_window.title(self.name)
        self.file_window.minsize(200, 100)
        self.file_window.attributes("-topmost", True)
        self.file_window.after(200, lambda: self.file_window.iconbitmap(self.icon))
        self.file_textbox = ctk.CTkTextbox(self.file_window, width=300, height=400)
        self.file_textbox.pack(expand=True, fill="both")
        self.file_textbox.insert(0.0, self.file_content)

        self.file_window.protocol("WM_DELETE_WINDOW", self.close)


    def close(self):
        updated_content = self.file_textbox.get(0.0, "end-1c")
        self.on_close_callback(self.name, updated_content)
        self.file_window.destroy()
        