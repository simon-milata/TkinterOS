import customtkinter as ctk

from src.tkinteros.theme import ThemeColors, ThemeFonts


class Window:
    def __init__(self, master, name: str, close_callback):
        self.master = master
        self.name = name
        self.close_callback = close_callback
        self.create()


    def create(self):
        self.main_frame = ctk.CTkFrame(self.master, fg_color="red", width=300, height=320)
        self.main_frame.place(relx=0, rely=0)
        self.create_top_bar()
    

    def create_top_bar(self):
        top_bar = ctk.CTkFrame(self.main_frame, height=40, corner_radius=0, width=300)
        top_bar.place(relx=0, rely=0)
        button_zone = ctk.CTkFrame(top_bar, width=120, height=40, corner_radius=0, fg_color="green")
        button_zone.place(x=180, rely=0)
        button_zone.grid_propagate(False)
        close_button = ctk.CTkButton(
            button_zone, width=40, height=40, text="X", hover_color="red", fg_color="orange", 
            command=self.close_window
        )
        close_button.grid()

        top_bar.bind("<Button-1>", self.start_move)
        top_bar.bind("<B1-Motion>", self.move_window)


    def start_move(self, event):
        self.offset_x = event.x_root - self.main_frame.winfo_x()
        self.offset_y = event.y_root - self.main_frame.winfo_y()

    def move_window(self, event):
        x_pos = event.x_root - self.offset_x
        y_pos = event.y_root - self.offset_y

        self.main_frame.place(x=x_pos, y=y_pos)
        self.main_frame.lift()


    def close_window(self):
        self.close_callback(self.name)
        self.main_frame.destroy()