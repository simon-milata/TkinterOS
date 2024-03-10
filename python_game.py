import random

import customtkinter as ctk

class PythonGame:
    def __init__(self) -> None:
        self.create_gui()
        self.create_variables()
        self.create_binds()
        self.create_python()
        self.create_berry()
        self.check_hitboxes()

        self.move()


    def create_gui(self) -> None:
        self.WINDOW = ctk.CTkToplevel()
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 400
        self.WINDOW.geometry(str(self.WINDOW_WIDTH) + "x" + str(self.WINDOW_HEIGHT))
        self.WINDOW.title("Python.exe")
        self.WINDOW.attributes("-topmost", True)
        self.WINDOW.grab_set()


    def create_variables(self) -> None:
        self.game_over = False
        self.body_part_list = []
        self.python_coords = []
        self.GRID_SIZE = 20
        self.DEFAULT_PYTHON_SPEED = 2
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
        if [direction, self.direction] in [["right", "left"], ["left", "right"], ["up", "down"], ["down", "up"]]:
            return

        self.direction = direction


    def create_python(self):
        self.python_coords = [[180, 180]]

        self.python = ctk.CTkFrame(self.WINDOW, width=self.GRID_SIZE, height=self.GRID_SIZE, fg_color="blue")
        self.python.place(x=self.python_coords[0][0], y=self.python_coords[0][1])

        self.body_part_list = [self.python]


    def move(self) -> None:

        self.move_python_body()

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

        if self.game_over == False:
            self.python.place(x=self.python_coords[0][0], y=self.python_coords[0][1])
                
            self.WINDOW.after(int(1000 / self.python_speed), self.move)


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


    def create_berry(self):
        self.berry_x_pos = random.randrange(0, self.WINDOW_WIDTH, self.GRID_SIZE)
        self.berry_y_pos = random.randrange(0, self.WINDOW_HEIGHT, self.GRID_SIZE)
        self.berry = ctk.CTkFrame(self.WINDOW, fg_color="red", width=self.GRID_SIZE, height=self.GRID_SIZE)
        self.berry.place(x=self.berry_x_pos, y=self.berry_y_pos)


    def check_hitboxes(self):
        if self.python_coords[0][0] == self.berry_x_pos and self.python_coords[0][1] == self.berry_y_pos:
            self.berry_hit()

        if self.python_coords[0][0] < 0 or self.python_coords[0][0] > self.WINDOW_WIDTH or self.python_coords[0][1] < 0 or self.python_coords[0][1] > self.WINDOW_HEIGHT:
            self.end_game()

        if self.game_over == False:
            self.WINDOW.after(10, self.check_hitboxes)


    def check_if_self_eating(self):
        python_coords_copy = self.python_coords.copy()
        python_coords_copy.pop(0)

        if self.python_coords[0] in python_coords_copy:
            self.end_game()


    def berry_hit(self):
        self.berries += 1
        self.python_speed = self.berries / 1.5 + self.DEFAULT_PYTHON_SPEED

        self.berry.destroy()
        self.grow_python()
        self.create_berry()


    def grow_python(self):
        if (len(self.body_part_list) + 1) % 2 == 0:
            python_body = ctk.CTkFrame(self.WINDOW, width=self.GRID_SIZE, height=self.GRID_SIZE, fg_color="yellow")
        else:
            python_body = ctk.CTkFrame(self.WINDOW, width=self.GRID_SIZE, height=self.GRID_SIZE, fg_color="blue")
        
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
        

    def end_game(self):
        self.python_speed = 0
        self.game_over = True
        for part in self.body_part_list:
            part.destroy()

        print("GAME OVER")
    