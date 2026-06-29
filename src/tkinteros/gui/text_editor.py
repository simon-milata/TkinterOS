from collections.abc import Callable

import customtkinter as ctk


class TextEditor:
    def __init__(
            self, name: str, file_content: str, on_close_callback: Callable[[str, str], None], 
            master_frame
        ):
        self.name = name
        self.file_content = file_content
        self.on_close_callback = on_close_callback
        self.master_frame = master_frame

        self.open_file()


    def open_file(self):
        self.file_textbox = ctk.CTkTextbox(self.master_frame, width=300, height=400, corner_radius=0)
        self.file_textbox.pack(expand=True, fill="both")
        self.file_textbox.insert(0.0, self.file_content)

        self.master_frame.protocol("WM_DELETE_WINDOW", self.close)


    def close(self):
        updated_content = self.file_textbox.get(0.0, "end-1c")
        self.on_close_callback(self.name, updated_content)
        