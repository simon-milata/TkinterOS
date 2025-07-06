import customtkinter as ctk

from PIL import Image


class TextFileWidget:
    def __init__(self, File: object, desktop_frame, on_click_callback):
        self.file = File
        self.on_click_callback = on_click_callback

        self.create_file_icon(desktop_frame)


    def create_file_icon(self, desktop_frame):
        """Creates the body/icon of the file"""
        file_body_frame = ctk.CTkFrame(desktop_frame, width=75, height=100)
        file_body_frame.place(x=self.file.pos_x, y=self.file.pos_y)
        file_body_button = ctk.CTkButton(
            file_body_frame, width=75, height=100, command=self.on_click, text="",
            image=ctk.CTkImage(Image.open("assets/desktop/python_logo.png"), size=(50, 50)), fg_color="transparent"
        ) # TODO: replace placeholder image
        file_body_button.place(anchor="center", relx=0.5, rely=0.5)
        file_body_name_label = ctk.CTkLabel(file_body_frame, width=75, height=20, text=self.file.name)
        file_body_name_label.place(anchor="center", relx=0.5, rely=0.9)


    def on_click(self):
        self.on_click_callback(self.file.name)


    # def open_file(self, desktop_frame):
    #     file_window = ctk.CTkToplevel(desktop_frame)
    #     file_window.attributes("-topmost", True)
    #     file_textbox = ctk.CTkTextbox(file_window)
    #     file_textbox.pack(expand=True, fill="both")
    #     file_textbox.insert(0.0, self.content)

    #     file_window.protocol("WM_DELETE_WINDOW", lambda: self.on_file_close(file_textbox.get(0.0, "end"), file_window))
        
    
    # def on_file_close(self, content: str, window: ctk.CTkToplevel):
    #     self.on_close_callback(content)
    #     window.destroy()