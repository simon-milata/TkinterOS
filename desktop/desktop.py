from PIL import Image

import customtkinter as ctk

from styles import desktop_blue, desktop_yellow

class DesktopGUI:
    def __init__(self, os) -> None:
        self.os = os
        self.window_setup()
        self.get_screen_size()
        self.icon_setup()
        self.create_gui()
        ctk.set_appearance_mode("light")

    
    def window_setup(self) -> None:
        self.WINDOW = ctk.CTk()
        self.WINDOW.attributes('-fullscreen', True)
        self.WINDOW.configure(fg_color=("white", "black"))
        self.WINDOW.update_idletasks()


    def get_screen_size(self) -> None:
        self.WINDOW.update()
        self.width = int(self.WINDOW.winfo_geometry().split("x")[0])
        self.height = int(self.WINDOW.winfo_geometry().split("x")[1].split("+")[0])


    def icon_setup(self) -> None:
        self.python_logo = ctk.CTkImage(Image.open("assets/desktop/python_logo.png"), size=(self.height/5, self.height/5))

    
    def create_gui(self) -> None:
        self.create_desktop()
        self.create_desktop_actions()
        self.create_new_action()


    def create_desktop(self) -> None:
        self.desktop_frame = ctk.CTkFrame(self.WINDOW, width=self.width, height=self.height-45, fg_color="transparent", corner_radius=0)
        self.desktop_frame.place(anchor="n", relx=0.5, rely=0)
        self.desktop_logo = ctk.CTkLabel(self.desktop_frame, image=self.python_logo, text="")
        self.desktop_logo.place(anchor="center", relx=0.5, rely=0.5)


    def create_desktop_actions(self) -> None:
        self.desktop_actions_frame = ctk.CTkFrame(self.desktop_frame)
        self.desktop_actions_frame.lift()
        self.new_button = ctk.CTkButton(self.desktop_actions_frame, text="New >")
        self.new_button.pack()


    def create_new_action(self) -> None:
        self.new_action_frame = ctk.CTkFrame(self.desktop_frame)

        self.create_new_folder = ctk.CTkButton(self.new_action_frame, text="Folder")
        self.create_new_folder.pack()
        self.create_new_text_document = ctk.CTkButton(self.new_action_frame, text="Text Document", command=self.os.create_text_document)
        self.create_new_text_document.pack()


    def create_text_document_gui(self, x, y) -> None:
        text_document_frame = ctk.CTkFrame(self.desktop_frame, width=75, height=100)
        text_document_frame.place(x=x, y=y)
        text_document_button = ctk.CTkButton(text_document_frame, width=75, height=100, command=self.os.open_text_document, text="Text Document.txt")
        text_document_button.place(anchor="center", relx=0.5, rely=0.5)


    def create_text_document_open_gui(self) -> None:
        text_document_open_window = ctk.CTkToplevel(self.WINDOW)
        text_document_open_window.attributes("-topmost", True)
        text_document_open_textbox = ctk.CTkTextbox(text_document_open_window)
        text_document_open_textbox.pack(expand=True, fill="both")


    def create_motion_area_gui(self, start_x, start_y, end_x, end_y):
        self.motion_frame = ctk.CTkFrame(self.desktop_frame, fg_color="lightblue", border_color="blue", border_width=2, corner_radius=0, height=end_y-start_y, width=end_x-start_x)
        self.motion_frame.place(x=start_x, y=start_y)


    def run(self) -> None:
        self.WINDOW.mainloop()