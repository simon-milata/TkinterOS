import customtkinter as ctk

from tkinteros.theme import THEME_COLORS, THEME_FONTS
from tkinteros.asset_management.asset_manager import AssetManager
from tkinteros.window_management.app_config import App


am = AssetManager("src/tkinteros/asset_management/assets")

class Window:
    def __init__(self, master, app: App, close_callback):
        self.master = master
        self.name = app.name
        self.title = app.title
        self.close_callback = close_callback
        self.icon = app.icon
        self.create()


    def create(self):
        self.main_frame = ctk.CTkFrame(self.master, fg_color=THEME_COLORS.bright, width=500, height=520)
        self.main_frame.place(x=100, y=100)
        self.inside_frame = ctk.CTkFrame(self.main_frame)
        self.inside_frame.pack(padx=2, pady=2, fill="both", expand=True)
        self.create_top_bar()
        self.content_frame = ctk.CTkFrame(self.inside_frame, fg_color="blue")
        self.content_frame.pack(fill="both", expand=True)
    

    def create_top_bar(self):
        top_bar = ctk.CTkFrame(
            self.inside_frame, height=40, corner_radius=0, width=300, fg_color=THEME_COLORS.bright,
            bg_color=THEME_COLORS.bright
        )
        top_bar.pack(fill="x")
        top_bar.pack_propagate(False)
        app_icon = ctk.CTkImage(
            light_image=am.get_image(self.icon, THEME_COLORS.primary[1]), 
            dark_image=am.get_image(self.icon, THEME_COLORS.primary[0]), size=(20, 20)
        )
        app_icon_label = ctk.CTkLabel(top_bar, width=40, height=40, text="", image=app_icon)
        app_icon_label.pack(side="left")
        title = ctk.CTkLabel(top_bar, text=self.title, font=(THEME_FONTS.family, THEME_FONTS.small))
        title.pack(side="left", padx=10)
        
        button_zone = ctk.CTkFrame(top_bar, width=120, height=40, corner_radius=0, fg_color=THEME_COLORS.bright)
        button_zone.pack(side="right")
        button_zone.grid_propagate(False)
        close_button = ctk.CTkButton(
            button_zone, width=40, height=32, text="X", hover_color=THEME_COLORS.highlight, 
            fg_color=THEME_COLORS.off, corner_radius=5, font=(THEME_FONTS.family_bold, THEME_FONTS.small),
            text_color=THEME_COLORS.font_color, bg_color=THEME_COLORS.bright, command=self.close_window
        )
        close_button.pack(side="left", padx=10)

        top_bar.bind("<Button-1>", self.start_move)
        top_bar.bind("<B1-Motion>", self.move_window)
        button_zone.bind("<Button-1>", self.start_move)
        button_zone.bind("<B1-Motion>", self.move_window)
        title.bind("<Button-1>", self.start_move)
        title.bind("<B1-Motion>", self.move_window)
        app_icon_label.bind("<Button-1>", self.start_move)
        app_icon_label.bind("<B1-Motion>", self.move_window)


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