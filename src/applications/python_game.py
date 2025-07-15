import random

import customtkinter as ctk
from playsound import playsound

from theme import THEME_COLORS, THEME_FONTS

python_blue = "#326c9b"
python_yellow = "#ffe66d"

class PythonGame:
    def __init__(self, os, os_window: ctk.CTk) -> None:
        self.OS = os
        self.OS_WINDOW = os_window
        self.create_game_variables()
        self.create_window()
        self.create_main_menu()


    def create_game_variables(self):
        self.grid_setup = False
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 400
        self.GRID_SIZE = 40
        self.base_color_1 = "green"
        self.base_color_2 = "darkgreen"
        self.berry_color = "#e03d3d"
        self.munch_sound = "src/Assets/python_game/munch_sound.mp3"

    
    def create_window(self) -> None:
        self.WINDOW = ctk.CTkToplevel()
        self.WINDOW.geometry(str(self.WINDOW_WIDTH) + "x" + str(self.WINDOW_HEIGHT))
        self.WINDOW.configure(fg_color=THEME_COLORS.primary)
        self.WINDOW.title("Python Game")
        self.WINDOW.attributes("-topmost", True)
        self.WINDOW.focus_force()
        self.WINDOW.resizable(False, False)
        self.WINDOW.after(200, self.icon_setup)

    
    def icon_setup(self):
        if self.OS.appearance_mode:
            self.WINDOW.iconbitmap("src/Assets/python_game/snake_yellow_icon.ico")
        else:
            self.WINDOW.iconbitmap("src/Assets/python_game/snake_blue_icon.ico")


    def create_main_menu(self):
        self.main_menu_frame = ctk.CTkFrame(self.WINDOW, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT, fg_color=THEME_COLORS.primary)
        self.main_menu_frame.pack()
        header = ctk.CTkLabel(self.main_menu_frame, text="PYTHON", text_color=THEME_COLORS.font_color, font=(THEME_COLORS.font_color, THEME_FONTS.large))
        header.place(anchor="n", relx=0.5, rely=0.05)
        
        rows_label = ctk.CTkLabel(self.main_menu_frame, text="Rows", text_color=THEME_COLORS.font_color, font=(THEME_FONTS.family, THEME_FONTS.big))
        rows_label.place(anchor="center", relx=0.5, rely=0.52)
        self.row_input = ctk.CTkSegmentedButton(self.main_menu_frame, text_color=THEME_COLORS.button_font_color, font=(THEME_FONTS.family, THEME_FONTS.big), selected_hover_color=THEME_COLORS.button_hover, 
                                                fg_color=THEME_COLORS.button, unselected_color=THEME_COLORS.button, selected_color=THEME_COLORS.button_hover, values=["5", "10", "15", "20"], unselected_hover_color=THEME_COLORS.button)
        self.row_input.place(anchor="center", relx=0.5, rely=0.62)

        columns_label = ctk.CTkLabel(self.main_menu_frame, text="Columns", text_color=THEME_COLORS.font_color, font=(THEME_FONTS.family, THEME_FONTS.big))
        columns_label.place(anchor="center", relx=0.5, rely=0.3)
        self.column_input = ctk.CTkSegmentedButton(self.main_menu_frame, text_color=THEME_COLORS.button_font_color, font=(THEME_FONTS.family, THEME_FONTS.big), selected_hover_color=THEME_COLORS.button_hover, 
                                                   fg_color=THEME_COLORS.button, unselected_color=THEME_COLORS.button, selected_color=THEME_COLORS.button_hover, values=["5", "10", "15", "20"], unselected_hover_color=THEME_COLORS.button)
        self.column_input.place(anchor="center", relx=0.5, rely=0.4)
        play_button = ctk.CTkButton(self.main_menu_frame, text="Play", text_color=THEME_COLORS.button_font_color, fg_color=THEME_COLORS.button, command=self.start_game,
                                    font=(THEME_COLORS.font_color, THEME_FONTS.button_font_size), hover_color=THEME_COLORS.button_hover)
        play_button.place(anchor="center", relx=0.5, rely=0.8)


    def create_grid(self):
        columns = int(self.WINDOW_WIDTH / self.GRID_SIZE)
        rows = int(self.WINDOW_HEIGHT / self.GRID_SIZE)

        x_pos = 0 - self.GRID_SIZE
        y_pos = 0 - self.GRID_SIZE

        color1 = self.base_color_2
        color2 = self.base_color_1

        for i in range(rows):
            y_pos += self.GRID_SIZE
            x_pos = 0 - self.GRID_SIZE

            color1, color2 = color2, color1

            for j in range(columns):
                x_pos += self.GRID_SIZE
                if j % 2 == 0:
                    ctk.CTkFrame(self.WINDOW, fg_color=color1, width=self.GRID_SIZE, height=self.GRID_SIZE, corner_radius=0).place(x=x_pos, y=y_pos)
                else:
                    ctk.CTkFrame(self.WINDOW, fg_color=color2, width=self.GRID_SIZE, height=self.GRID_SIZE, corner_radius=0).place(x=x_pos, y=y_pos)


    def create_python_variables(self) -> None:
        self.reduce_size_by = 0.05
        self.python_size = 1
        self.previous_head_pos = []
        self.direction_to_buffer = ""
        self.change_direction_lock = False
        self.python_head_color = python_blue
        self.game_over = False
        self.body_part_list = []
        self.python_coords = []
        self.DEFAULT_PYTHON_SPEED = 3
        self.DEFAULT_SPEED_INCREASE = 0.05
        self.python_speed = self.DEFAULT_PYTHON_SPEED
        self.direction = "up"
        self.berries = 0


    def create_binds(self) -> None:
        self.WINDOW.bind("w", lambda event: self.change_direction(event, "up"))
        self.WINDOW.bind("<Up>", lambda event: self.change_direction(event, "up"))
        self.WINDOW.bind("a", lambda event: self.change_direction(event, "left"))
        self.WINDOW.bind("<Left>", lambda event: self.change_direction(event, "left"))
        self.WINDOW.bind("s", lambda event: self.change_direction(event, "down"))
        self.WINDOW.bind("<Down>", lambda event: self.change_direction(event, "down"))
        self.WINDOW.bind("d", lambda event: self.change_direction(event, "right"))
        self.WINDOW.bind("<Right>", lambda event: self.change_direction(event, "right"))


    def change_direction(self, event, direction:str) -> None:
        #Prevent python head from being able to change direction towards it's body if it has one
        if len(self.body_part_list) > 1:
            if direction == "up" and self.python_coords[1][1] <  self.python_coords[0][1]:
                return
            elif direction == "down" and self.python_coords[1][1] > self.python_coords[0][1]:
                return
            elif direction == "left" and self.python_coords[1][0] < self.python_coords[0][0]:
                return
            elif direction == "right" and self.python_coords[1][0] > self.python_coords[0][0]:
                return
            
        #Prevent python head from turning 180 degrees if it doesn't have a body    
        else:
            if direction == "up" and self.previous_head_pos[1] <  self.python_coords[0][1]:
                return
            elif direction == "down" and self.previous_head_pos[1] > self.python_coords[0][1]:
                return
            elif direction == "left" and self.previous_head_pos[0] < self.python_coords[0][0]:
                return
            elif direction == "right" and self.previous_head_pos[0] > self.python_coords[0][0]:
                return
            
        #Buffer the next move
        if self.change_direction_lock and self.direction_to_buffer == "":
            self.direction_to_buffer = direction
            return

        self.direction = direction
        self.change_direction_lock = True


    def create_python(self):
        #Create python in the center of a grid
        python_start_pos_x = round((self.WINDOW_WIDTH / 2) / self.GRID_SIZE) * self.GRID_SIZE
        python_start_pos_y = round((self.WINDOW_HEIGHT / 2) / self.GRID_SIZE) * self.GRID_SIZE + self.GRID_SIZE

        self.python_coords = [[python_start_pos_x, python_start_pos_y]]

        self.python = ctk.CTkFrame(self.WINDOW, width=self.GRID_SIZE, height=self.GRID_SIZE, corner_radius=0)
        self.python.place(x=self.python_coords[0][0], y=self.python_coords[0][1])
        self.python_graphic = ctk.CTkFrame(self.python, fg_color=self.python_head_color, width=self.GRID_SIZE, height=self.GRID_SIZE)
        self.python_graphic.place(anchor="center", relx=0.5, rely=0.5)
        self.python_eye_1 = ctk.CTkFrame(self.python_graphic, fg_color="black", bg_color=self.python_head_color, corner_radius=self.GRID_SIZE/4, width=self.GRID_SIZE/4, height=self.GRID_SIZE/4)
        self.python_eye_1.place(anchor="n", relx=0.25, rely=0.25)
        self.python_eye_2 = ctk.CTkFrame(self.python_graphic, fg_color="black", bg_color=self.python_head_color, corner_radius=self.GRID_SIZE/4, width=self.GRID_SIZE/4, height=self.GRID_SIZE/4)
        self.python_eye_2.place(anchor="n", relx=0.75, rely=0.25)

        self.body_part_list = [self.python]


    def move(self) -> None:
        self.move_python_body()

        if self.direction_to_buffer != "":
            self.change_direction_lock = True
            self.direction = self.direction_to_buffer
            self.direction_to_buffer = ""

        self.previous_head_pos = self.python_coords[0].copy()

        match self.direction:
            case "up":
                self.python_coords[0][1] -= self.GRID_SIZE
            case "left":
                self.python_coords[0][0] -= self.GRID_SIZE
            case "down":
                self.python_coords[0][1] += self.GRID_SIZE
            case "right":
                self.python_coords[0][0] += self.GRID_SIZE

        self.check_if_self_eating()

        self.python.place(x=self.python_coords[0][0], y=self.python_coords[0][1])

        self.rotate_eyes()

        self.update_python_background()
        self.check_hitboxes()
        self.change_direction_lock = False

        if self.game_over:
            return
                
        self.WINDOW.after(int(1000 / self.python_speed), self.move)
        self.change_direction_lock = False


    def move_python_body(self):
        if len(self.python_coords) < 2:
            return
        
        for index in range(len(self.python_coords)-1, 0, -1):
            if index == 0:
                pass
            
            else:
                self.python_coords[index][0] = self.python_coords[index-1][0]
                self.python_coords[index][1] = self.python_coords[index-1][1]
                self.body_part_list[index].place(x=self.python_coords[index][0], y=self.python_coords[index][1])


    def update_python_background(self):
        """Updates the background color of each body part based on it's position"""
        for index, part in enumerate(self.body_part_list):
            if self.python_coords[index][0] / self.GRID_SIZE % 2 == 0:
                if self.python_coords[index][1] / self.GRID_SIZE % 2 == 0:
                    part.configure(bg_color=self.base_color_1, fg_color=self.base_color_1)
                else:
                    part.configure(bg_color=self.base_color_2, fg_color=self.base_color_2)
            else:
                if self.python_coords[index][1] / self.GRID_SIZE % 2 == 0:
                    part.configure(bg_color=self.base_color_2, fg_color=self.base_color_2)
                else:
                    part.configure(bg_color=self.base_color_1, fg_color=self.base_color_1)


    def create_berry(self):
        #Prevent berries spawning in the same position as any body part
        while True:
            self.berry_x_pos = random.randrange(0, self.WINDOW_WIDTH, self.GRID_SIZE)
            self.berry_y_pos = random.randrange(0, self.WINDOW_HEIGHT, self.GRID_SIZE)

            if [self.berry_x_pos, self.berry_y_pos] not in self.python_coords:
                break

        def get_background_color() -> str:
            if self.berry_x_pos / self.GRID_SIZE % 2 == 0:
                if self.berry_y_pos / self.GRID_SIZE % 2 == 0:
                    background_color = self.base_color_1
                else:
                     background_color = self.base_color_2
            else:
                if self.berry_y_pos / self.GRID_SIZE % 2 == 0:
                    background_color = self.base_color_2
                else:
                    background_color = self.base_color_1
            return background_color

        self.berry = ctk.CTkFrame(self.WINDOW, width=self.GRID_SIZE, height=self.GRID_SIZE, border_width=0, bg_color=get_background_color(), fg_color=get_background_color(), corner_radius=0)
        self.berry.place(x=self.berry_x_pos, y=self.berry_y_pos)
        berry_graphic = ctk.CTkFrame(self.berry, fg_color=self.berry_color, width=self.GRID_SIZE/1.5, height=self.GRID_SIZE/1.5, corner_radius=self.GRID_SIZE/1.5)
        berry_graphic.place(anchor="center", relx=0.5, rely=0.5)


    def check_hitboxes(self):
        if self.game_over:
            return
        
        #If position of snake head is the same as berry position
        if self.python_coords[0][0] == self.berry_x_pos and self.python_coords[0][1] == self.berry_y_pos:
            self.berry_hit()

        #If position of snake head is outside of window
        if self.python_coords[0][0] < 0 or self.python_coords[0][0] > self.WINDOW_WIDTH - self.GRID_SIZE or self.python_coords[0][1] < 0 or self.python_coords[0][1] > self.WINDOW_HEIGHT - self.GRID_SIZE:
            self.end_game()


    def check_if_self_eating(self):
        python_coords_copy = self.python_coords.copy()
        python_coords_copy.pop(0)

        if self.python_coords[0] in python_coords_copy:
            self.end_game()


    def berry_hit(self):
        playsound(self.munch_sound, block=False)

        self.berries += 1
        self.python_speed += self.DEFAULT_SPEED_INCREASE

        self.berry.destroy()
        self.grow_python()
        self.create_berry()

    
    def reduce_python_size(self):
        if self.python_size > 0.8:
            self.python_size -= self.reduce_size_by
        elif self.python_size > 0.6:
            self.python_size -= self.reduce_size_by / 2


    def grow_python(self):
        self.reduce_python_size()

        color = self.body_part_list[-1].cget("bg_color")

        if color == "green":
            color = "darkgreen"
        else:
            color = "green"

        if (len(self.body_part_list) + 1) % 2 == 0:
            python_body = ctk.CTkFrame(self.WINDOW, width=self.GRID_SIZE, height=self.GRID_SIZE, corner_radius=0, fg_color=color)
            python_graphic = ctk.CTkFrame(python_body, fg_color=python_yellow, width=self.GRID_SIZE * self.python_size, height=self.GRID_SIZE * self.python_size, bg_color=color)
            python_graphic.place(anchor="center", relx=0.5, rely=0.5)
        else:
            python_body = ctk.CTkFrame(self.WINDOW, width=self.GRID_SIZE, height=self.GRID_SIZE, corner_radius=0, fg_color=color)
            python_graphic = ctk.CTkFrame(python_body, fg_color=python_blue, width=self.GRID_SIZE * self.python_size, height=self.GRID_SIZE * self.python_size, bg_color=color)
            python_graphic.place(anchor="center", relx=0.5, rely=0.5)

        
        #Get the position of where to grow the next body part
        match self.direction:
            case "up":
                python_body_x_coord = self.python_coords[-1][0]
                python_body_y_coord = self.python_coords[-1][1] + self.GRID_SIZE
            case "left":
                python_body_x_coord = self.python_coords[-1][0] + self.GRID_SIZE
                python_body_y_coord = self.python_coords[-1][1]
            case "down":
                python_body_x_coord = self.python_coords[-1][0]
                python_body_y_coord = self.python_coords[-1][1] - self.GRID_SIZE
            case "right":
                python_body_x_coord = self.python_coords[-1][0] - self.GRID_SIZE
                python_body_y_coord = self.python_coords[-1][1]

        python_body.place(x=python_body_x_coord, y=python_body_y_coord)

        self.body_part_list.append(python_body)
        self.python_coords.append([python_body_x_coord, python_body_y_coord])


    def create_game_over_gui(self):
        self.WINDOW.geometry("400x400")
        self.game_over_frame = ctk.CTkFrame(self.WINDOW, width=400, height=400, fg_color=THEME_COLORS.primary)
        self.game_over_frame.pack()
        game_over_text = ctk.CTkLabel(self.game_over_frame, text="Game Over!", font=(THEME_FONTS.family_bold, THEME_FONTS.large), text_color=THEME_COLORS.font_color)
        game_over_text.place(anchor="n", relx=0.5, rely=0.05)
        berry_label = ctk.CTkLabel(self.game_over_frame, text="Berries", font=(THEME_FONTS.family_bold, THEME_FONTS.big), text_color=THEME_COLORS.font_color)
        berry_label.place(anchor="center", relx=0.5, rely=0.35)
        score_text = ctk.CTkLabel(self.game_over_frame, text=self.berries, font=(THEME_FONTS.family_bold, THEME_FONTS.large), text_color=THEME_COLORS.font_color)
        score_text.place(anchor="center", relx=0.5, rely=0.5)
        play_again_button = ctk.CTkButton(self.game_over_frame, text="Play Again", fg_color=THEME_COLORS.button, text_color=THEME_COLORS.button_font_color, 
                                          font=(THEME_FONTS.family_bold, THEME_FONTS.button_font_size), command=self.run, hover_color=THEME_COLORS.button_hover)
        play_again_button.place(anchor="center", relx=0.5, rely=0.7)
        

    def end_game(self):
        self.python_speed = 0
        self.game_over = True
        
        self.create_game_over_gui()


    def start_game(self):
        self.setup_grid()
        if self.grid_setup == False:
            return
        
        self.main_menu_frame.pack_forget()
        self.create_grid()
        self.run()


    def run(self):
        try:
            self.game_over_frame.destroy()
            self.berry.destroy()
            for part in self.body_part_list:
                part.destroy()
        except AttributeError:
            pass

        self.WINDOW.geometry(str(self.WINDOW_WIDTH) + "x" + str(self.WINDOW_HEIGHT))

        self.create_python_variables()
        self.create_binds()
        self.create_python()
        self.create_berry()

        self.move()


    def rotate_eyes(self):
        if self.direction == "up":
            self.python_eye_1.place(anchor="n", relx=0.25, rely=0.25)
            self.python_eye_2.place(anchor="n", relx=0.75, rely=0.25)
        elif self.direction == "left":
            self.python_eye_1.place(anchor="w", relx=0.25, rely=0.25)
            self.python_eye_2.place(anchor="w", relx=0.25, rely=0.75)
        elif self.direction == "right":
            self.python_eye_1.place(anchor="e", relx=0.75, rely=0.25)
            self.python_eye_2.place(anchor="e", relx=0.75, rely=0.75)
        else:
            self.python_eye_1.place(anchor="s", relx=0.25, rely=0.75)
            self.python_eye_2.place(anchor="s", relx=0.75, rely=0.75)


    def setup_grid(self):
        if self.column_input.get() == "":
            self.column_input.set("10")
        if self.row_input.get() == "":
            self.row_input.set("10")

        self.OS_WINDOW.update()

        if int(self.column_input.get()) > self.OS_WINDOW.winfo_width() or int(self.row_input.get()) > self.OS_WINDOW.winfo_height():
            return
        
        self.WINDOW_WIDTH = self.GRID_SIZE * int(self.column_input.get())
        self.WINDOW_HEIGHT = self.GRID_SIZE * int(self.row_input.get())
        self.WINDOW.geometry(str(self.WINDOW_WIDTH) + "x" + str(self.WINDOW_HEIGHT))

        self.grid_setup = True