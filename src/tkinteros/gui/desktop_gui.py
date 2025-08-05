import math

from PIL import Image
import customtkinter as ctk

from tkinteros.callback_management.callbacks import Callback
from tkinteros.theme import THEME_COLORS, THEME_FONTS
from tkinteros.asset_management.asset_manager import AssetManager
from tkinteros.asset_management.assets import DesktopAssets
from tkinteros.gui.file_widget import TextFileWidget


class DesktopGUI:
    def __init__(self, appearance_mode, callbacks, asset_manager: AssetManager) -> None:
        self.asset_manager = asset_manager
        self.callbacks = callbacks
        self.window_setup()
        self.get_screen_size()
        self.icon_setup()
        self.create_gui()
        ctk.set_appearance_mode(appearance_mode)

        self.shaking = False

    
    def window_setup(self) -> None:
        self.WINDOW = ctk.CTk()
        self.WINDOW.attributes('-fullscreen', True)
        self.WINDOW.configure(fg_color=THEME_COLORS.primary)
        self.WINDOW.update_idletasks()


    def get_screen_size(self) -> None:
        self.WINDOW.update()
        self.width = int(self.WINDOW.winfo_geometry().split("x")[0])
        self.height = int(self.WINDOW.winfo_geometry().split("x")[1].split("+")[0])


    def icon_setup(self) -> None:
        self.python_logo = ctk.CTkImage(self.asset_manager.get_image(DesktopAssets.BACKGROUND_LOGO, resize=False), size=(self.height/5, self.height/5))

    
    def create_gui(self) -> None:
        self.create_desktop()
        self.create_desktop_actions()
        self.create_new_action()
        self.create_file_name_input()


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

        self.create_new_text_document = ctk.CTkButton(
            self.new_action_frame, text="Text Document", 
            command=self.create_file_name_input_window
        )
        self.create_new_text_document.pack()


    def create_file_name_input_window(self):
        self.desktop_actions_frame.update()
        x_pos = self.desktop_actions_frame.winfo_rootx()
        y_pos = self.desktop_actions_frame.winfo_rooty() + self.desktop_actions_frame.winfo_height()

        self.file_name_input.place(x=x_pos, y=y_pos)

        self.file_name_input.focus()

        self.file_name_input.bind("<Return>", self.create_new_file)


    def create_file_name_input(self):
        self.file_name_input = ctk.CTkEntry(
            self.WINDOW
        )


    def hide_file_name_input_window(self):
        self.file_name_input.delete(0, "end")
        self.file_name_input.place_forget()


    def hide_desktop_actions_frame(self):
        self.desktop_actions_frame.place_forget()
        self.new_action_frame.place_forget()

    
    def create_new_file(self, event):
        name = self.file_name_input.get()
        validation_succesful = self.callbacks[Callback.VALIDATE_FILE_NAME](name)

        if not validation_succesful:
            if not self.shaking:
                self.shake_placed_widget(self.file_name_input, 20)
            return "break"

        self.callbacks[Callback.CREATE_TXT_FILE](name)
        self.hide_file_name_input_window()
        self.hide_desktop_actions_frame()
        return "break"


    def create_text_file_widget(self, file_object, open_file_callback):
        TextFileWidget(
            file=file_object, desktop_frame=self.WINDOW, on_click_callback=open_file_callback,
            light_icon=self.asset_manager.get_image(DesktopAssets.TEXT_FILE, THEME_COLORS.primary[1]),
            dark_icon=self.asset_manager.get_image(DesktopAssets.TEXT_FILE, THEME_COLORS.primary[0])
        )


    def shake_placed_widget(self, widget, pixel_amount: int, times_shaken: int = 3):
        widget.update()
        initial_x = widget.winfo_x()
        initial_y = widget.winfo_y()

        self.shaking = True

        steps_per_shake = 8
        total_steps = steps_per_shake * times_shaken
        delay = 10

        for step in range(total_steps):
            # Calculate an offset using a sine wave pattern for smooth motion
            angle = step / steps_per_shake * math.pi
            offset = int(math.sin(angle) * pixel_amount)

            widget.after(step * delay, lambda dx=offset: widget.place(x=initial_x + dx, y=initial_y))

        widget.after(total_steps * delay, lambda: self.reset_shaken_widget(widget=widget, initial_x=initial_x, initial_y=initial_y))

        
    def reset_shaken_widget(self, widget, initial_x: int, initial_y: int):
        widget.place(x=initial_x, y=initial_y)
        self.shaking = False


    def create_selection_box_gui(self, start_x, start_y, end_x, end_y):
        self.motion_frame = ctk.CTkFrame(self.desktop_frame, fg_color="lightblue", border_color="blue", border_width=2, corner_radius=0, height=end_y-start_y, width=end_x-start_x)
        self.motion_frame.place(x=start_x, y=start_y)


    def run(self) -> None:
        self.WINDOW.mainloop()