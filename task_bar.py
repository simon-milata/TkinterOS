from PIL import Image

import customtkinter as ctk

from styles import desktop_colors, desktop_highlight_colors, font_size_xs, font_family, font_color, desktop_off_colors, desktop_bright_colors, button_color, button_font_color, font_size_small

class TaskBar:
    def __init__(self, os, gui) -> None:
        self.os = os
        self.gui = gui

        self.create_variables()
        self.icon_setup()
        self.create_taskbar()
        self.create_start_menu()
        self.create_time_date()
        self.create_utils()
        self.create_utils_menu()
        

    def create_variables(self):
        self.WINDOW = self.gui.WINDOW
        self.width = self.gui.width
        self.height = self.gui.height

    
    def icon_setup(self) -> None:
        self.python_icon = ctk.CTkImage(light_image=Image.open("assets/python_icon_dark.png"), dark_image=Image.open("assets/python_icon.png"), size=(40, 40))
        self.snake_icon = ctk.CTkImage(light_image=Image.open("assets/snake_blue_icon.png"), dark_image=Image.open("assets/snake_yellow_icon.png"), size=(32, 32))
        self.no_internet_icon = ctk.CTkImage(light_image=Image.open("assets/no_internet_icon_dark.png"), dark_image=Image.open("assets/no_internet_icon.png"), size=(20, 20))
        self.internet_icon = ctk.CTkImage(light_image=Image.open("assets/wifi_icon_dark.png"), dark_image=Image.open("assets/wifi_icon.png"), size=(20, 20))
        self.internet_icon_off = ctk.CTkImage(light_image=Image.open("assets/wifi_icon.png"), dark_image=Image.open("assets/wifi_icon_dark.png"), size=(32, 32))

    
    def create_taskbar(self) -> None:
        self.taskbar = ctk.CTkFrame(self.WINDOW, height=45, width=self.width, fg_color=desktop_colors, corner_radius=0)
        self.taskbar.place(anchor="s", relx=0.5, rely=1)

        self.taskbar_app_frame = ctk.CTkFrame(self.taskbar, fg_color="transparent")
        self.taskbar_app_frame.place(anchor="center", relx=0.5, rely=0.5)

        self.start_button = ctk.CTkButton(self.taskbar, text="", image=self.python_icon, width=45, height=45, fg_color="transparent", 
                                          command=self.os.start_menu_mechanism, hover_color=desktop_highlight_colors)
        self.start_button.place(anchor="w", relx=0, rely=0.5)

        self.create_default_taskbar_apps()


    def create_start_menu(self) -> None:
        self.start_menu_frame = ctk.CTkFrame(self.WINDOW, width=self.width/6, height=self.height/4, fg_color=desktop_off_colors)
        self.start_menu_frame.grid_propagate(False)

        self.shut_down_button = ctk.CTkButton(self.start_menu_frame, width=self.width/20, height=self.height/20, text="Shut down", command=self.os.quit, 
                                              fg_color=button_color, font=(font_family, font_size_small), text_color=button_font_color)
        self.shut_down_button.grid(padx=self.height * 0.01, pady=self.height * 0.01)
        self.restart_button = ctk.CTkButton(self.start_menu_frame, width=self.width/20, height=self.height/20, text="Restart", command=self.os.restart, 
                                            fg_color=button_color, font=(font_family, font_size_small), text_color=button_font_color)
        self.restart_button.grid(padx=self.height * 0.01, pady=self.height * 0.01)


    def create_time_date(self) -> None:
        self.time_date_frame = ctk.CTkFrame(self.taskbar, width=self.width/20, height=45, fg_color="transparent")
        self.time_date_frame.place(anchor="e", relx=1, rely=0.5)
        self.clock = ctk.CTkLabel(self.time_date_frame, text=self.os.get_time(), font=(font_family, font_size_xs), text_color=font_color, height=font_size_xs)
        self.clock.place(anchor="ne", relx=0.9, rely=0.1)
        self.date = ctk.CTkLabel(self.time_date_frame, text=self.os.get_date(), font=(font_family, font_size_xs), text_color=font_color, height=font_size_xs)
        self.date.place(anchor="se", relx=0.9, rely=0.9)

        self.clock.after(1000 * 60, self.update_time)
        self.date.after(1000 * 60 * 10, self.update_date)

    
    def update_time(self) -> None:
        self.clock.configure(text=self.os.get_time())

        self.clock.after(1000 * 60, self.update_time)

    
    def update_date(self) -> None:
        self.date.configure(text=self.os.get_date())

        self.date.after(1000 * 60 * 10, self.update_date)

    
    def create_default_taskbar_apps(self) -> None:
        self.python_game_frame = ctk.CTkFrame(self.taskbar_app_frame, fg_color="transparent")
        self.python_game_frame.pack(padx=self.width/30)
        self.python_game_button = ctk.CTkButton(self.python_game_frame, command=lambda: self.os.play_game("python"), width=45, height=45, text="", 
                                                image=self.snake_icon, fg_color="transparent", hover_color=desktop_highlight_colors)
        self.python_game_button.place(anchor="center", relx=0.5, rely=0.5)


    def create_utils(self) -> None:
        self.util_frame = ctk.CTkFrame(self.taskbar, height=45, width=self.width / 20, fg_color="transparent", bg_color="transparent")
        self.util_frame.place(anchor="center", relx=0.95, rely=0.5)

        self.internet = ctk.CTkButton(self.util_frame, height=45, width=45, text="", image=self.no_internet_icon, fg_color="transparent", 
                                      bg_color="transparent", hover_color=desktop_highlight_colors, command=self.os.utils_menu_mechanism)
        self.internet.grid()


    def create_utils_menu(self) -> None:
        self.utils_menu_frame = ctk.CTkFrame(self.WINDOW, width=self.width/6, height=self.height/4, fg_color=desktop_off_colors)
        self.utils_menu_frame.grid_propagate(False)
        
        self.internet_frame = ctk.CTkFrame(self.utils_menu_frame, fg_color="transparent")
        self.internet_frame.grid(padx=self.height * 0.01, pady=self.height * 0.01)
        self.internet_button = ctk.CTkButton(self.internet_frame, width=self.width * 0.05, height=self.height * 0.05, text="", hover_color=desktop_bright_colors, 
                                             command=self.os.internet_mechanism, fg_color=desktop_highlight_colors, image=self.internet_icon_off)
        self.internet_button.pack()
        self.internet_label = ctk.CTkLabel(self.internet_frame, text="Wi-Fi", font=(font_family, font_size_xs), text_color=font_color, fg_color="transparent")
        self.internet_label.pack()