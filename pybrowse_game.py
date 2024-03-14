from PIL import Image
import random

import customtkinter as ctk

from styles import button_color, button_font_color, font_family, font_size_small

class PyBrowseGame:
    def __init__(self, pybrowse_window: ctk.CTkToplevel, game_frame: ctk.CTkFrame) -> None:
        self.PYBROWSE_WINDOW = pybrowse_window
        self.PYBROWSE_WINDOW.update()
        self.game_frame = game_frame
        
        self.create_icons()
        self.create_variables()
        self.create_python()


    def create_icons(self) -> None:
        self.python_icon = ctk.CTkImage(light_image=Image.open("Assets/pybrowse/anaconda_blue.png"), dark_image=Image.open("Assets/pybrowse/anaconda_yellow.png"), size=(64, 64))


    def create_python(self) -> None:
        self.python_spawn_pos_x = int(self.game_frame.winfo_width() * 0.1)
        self.python_spawn_pos_y = int(self.game_frame.winfo_height() * 0.7)
        self.python = ctk.CTkLabel(self.game_frame, image=self.python_icon, fg_color="transparent", text="")
        self.python.place(x=self.python_spawn_pos_x, y=self.python_spawn_pos_y)


    def start_game(self) -> None:
        self.game_frame.after(1000, self.spawn_objects)


    def create_variables(self):
        self.game_over = False
        self.spawn_frequency = 0.5
        self.error_list = ["ValueError", "IndexError", "ZeroDivisionError", "SyntaxError", "IndentationError", "TypeError", "NameError"]
        self.game_frame.update()
        self.spawn_pos_x = int(self.game_frame.winfo_width())
        self.spawn_pos_y = 0
        self.spawn_pos_y_low = int(self.game_frame.winfo_height() * 0.8)
        self.barrier_speed = 5


    def spawn_objects(self) -> None:
        if self.game_over:
            return
        
        up_or_down = random.choice(["up", "down"])
        
        if up_or_down == "down":
            barrier = ctk.CTkLabel(self.game_frame, height=self.game_frame.winfo_height() / 3, text=random.choice(self.error_list), fg_color=button_color, 
                                   text_color=button_font_color, font=(font_family, font_size_small))
            barrier.place(x=self.spawn_pos_x, y=self.spawn_pos_y_low)
        else:
            barrier = ctk.CTkLabel(self.game_frame, text=random.choice(self.error_list), fg_color=button_color, text_color=button_font_color, 
                                   font=(font_family, font_size_small))
            barrier.place(x=self.spawn_pos_x, y=self.spawn_pos_y)

        self.move_object(barrier)

        if self.game_over:
            return

        self.game_frame.after(int(1000 / self.spawn_frequency), self.spawn_objects)

        if self.barrier_speed > 1:
            self.barrier_speed -= 0.1

    
    def move_object(self, blockade: ctk.CTkLabel):
        blockade.update()
        x_pos = blockade.winfo_x()
        x_pos -= 1
        y_pos = blockade.winfo_y()
        blockade.place(x=x_pos, y=y_pos)
        
        if x_pos <= 0:
            blockade.destroy()
            return
        
        

        blockade.after(int(self.barrier_speed), lambda: self.move_object(blockade))
