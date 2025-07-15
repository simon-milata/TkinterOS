from PIL import Image
import random

import customtkinter as ctk

from theme import THEME_COLORS, THEME_FONTS

class PyBrowseGame:
    def __init__(self, pybrowse: object, pybrowse_window: ctk.CTkToplevel, game_frame: ctk.CTkFrame) -> None:
        self.pybrowse = pybrowse
        self.PYBROWSE_WINDOW = pybrowse_window
        self.PYBROWSE_WINDOW.update()
        self.game_frame = game_frame
        
        self.create_icons()

        self.create_python()


    def create_icons(self) -> None:
        self.python_icon = ctk.CTkImage(light_image=Image.open("src/Assets/pybrowse/anaconda_blue.png"), dark_image=Image.open("src/Assets/pybrowse/anaconda_yellow.png"), size=(64, 64))


    def create_python(self) -> None:
        self.game_frame.update()

        self.python_spawn_pos_x = int(self.game_frame.winfo_width() * 0.1)
        self.python_spawn_pos_y = int(self.game_frame.winfo_height() * 0.7)
        self.python = ctk.CTkLabel(self.game_frame, image=self.python_icon, fg_color="transparent", text="")
        self.python.place(x=self.python_spawn_pos_x, y=self.python_spawn_pos_y)

        self.python_x = self.python_spawn_pos_x
        self.python_y = self.python_spawn_pos_y
        self.python_width = 64
        self.python_height = 64


    def start_game(self) -> None:
        try:
            self.score_counter.destroy()
        except AttributeError:
            pass

        self.create_variables()

        self.game_frame.grab_set()
        self.game_frame.focus_set()
        self.create_binds()
        self.start_counter()
        self.game_frame.after(1000, self.spawn_barrier)


    def create_variables(self):
        self.game_frame.update()
        self.game_over = False
        self.barrier_list = []
        self.barrier_frequency = 1
        self.spawn_pos_x = int(self.game_frame.winfo_width())
        self.spawn_pos_y = 0
        self.spawn_pos_y_low = int(self.game_frame.winfo_height() * 0.7)
        self.barrier_speed = 3
        self.mid_air = False
        self.score = 0
        self.score_counter = ctk.CTkLabel(self.game_frame, text=0, fg_color="transparent", text_color=THEME_COLORS.font_color, font=(THEME_FONTS.family, THEME_FONTS.small))
        self.score_counter.place(anchor="center", relx=0.5, rely=0.5)
        


    def spawn_barrier(self) -> None:
        if self.game_over:
            return
        
        up_or_down = random.choice(["up", "down", "down", "down"])
        
        if up_or_down == "down":
            spawn_pos_y = self.spawn_pos_y_low
        else:
            spawn_pos_y = self.spawn_pos_y

        if self.barrier_speed > 2:
            self.barrier_speed -= 0.01

        Blockade(self, self.game_frame, self.spawn_pos_x, spawn_pos_y, self.barrier_speed)

        if self.barrier_frequency > 0.3:
            self.barrier_frequency -= 0.01

        self.game_frame.after(int(1000 * self.barrier_frequency), self.spawn_barrier)


    def jump(self, event) -> None:
        if self.mid_air:
            return
        
        self.mid_air = True

        self.move_up()


    def move_up(self) -> None:
        if self.python_y > 5:
            self.python_y -= 2
            self.python.place(x=self.python_x, y=self.python_y)
        else:
            self.python.after(150, self.move_down)
            return
            
        self.python.after(3, self.move_up)


    def move_down(self) -> None:
        if self.python_y < self.python_spawn_pos_y:
            self.python_y += 2
            self.python.place(x=self.python_x, y=self.python_y)
        else:
            self.mid_air = False
            return
        
        self.python.after(3, self.move_down)


    def create_binds(self) -> None:
        self.game_frame.bind("<Button-1>", self.jump)

    
    def end_game(self) -> None:
        self.game_over = True
        self.game_frame.unbind("<Button-1>")
        self.PYBROWSE_WINDOW.bind("<space>", self.pybrowse.start_pybrowse_game)
        
        for barrier in self.barrier_list:
            barrier.destroy()

        
    def start_counter(self) -> None:
        if self.game_over:
            return
        
        self.score_counter.after(1, self.increase_counter)

    
    def increase_counter(self) -> None:
        self.score += 1
        self.score_counter.configure(text=self.score)
        self.start_counter()


class Blockade:
    def __init__(self, game: PyBrowseGame, game_frame: ctk.CTkFrame, x_pos: int, y_pos: int, speed: int) -> None:
        self.game = game
        self.game_frame = game_frame
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed

        self.error_list = ["ValueError", "IndexError", "ZeroDivisionError", "SyntaxError", "IndentationError", "TypeError", "NameError"]

        self.create_barrier()
        self.get_params()
        self.move_barrier()


    def create_barrier(self) -> ctk.CTkLabel:
        self.barrier = ctk.CTkLabel(self.game_frame, height=self.game_frame.winfo_height() / 3, text=random.choice(self.error_list), fg_color=THEME_COLORS.button, 
                                   text_color=THEME_COLORS.button_font_color, font=(THEME_FONTS.family, THEME_FONTS.extra_small))
        self.barrier.place(x=self.x_pos, y=self.y_pos)

        self.game.barrier_list.append(self.barrier)
    

    def get_params(self) -> None:
        self.barrier.update()
        self.width = self.barrier.winfo_width()
        self.height = self.barrier.winfo_height()
        self.barrier_x = self.x_pos
        self.barrier_y = self.y_pos


    def move_barrier(self):
        self.barrier_x -= 1
        self.barrier.place(x=self.barrier_x, y=self.barrier_y)
            
        if self.barrier_x <= -self.width:
            self.game.barrier_list.pop(0)
            self.barrier.destroy()
            return
        
        if (self.game.python_x < self.barrier_x + self.width and
            self.game.python_x + self.game.python_width > self.barrier_x and
            self.game.python_y < self.barrier_y + self.height and
            self.game.python_y + self.game.python_height > self.barrier_y):
            if not self.game.game_over:
                self.game.end_game()
                return
                
            
        self.barrier.after(int(self.speed), self.move_barrier)