from PIL import Image

import customtkinter as ctk

from styles import *


class TaskBarGUI:
    def __init__(self, desktop_window_details: dict[str], callbacks: dict) -> None:
        self.desktop_window_details = desktop_window_details
        self.callbacks = callbacks

        self.icon_setup()
        self.create_taskbar()
        self.create_start_menu()
        self.create_time_date()
        self.create_system_tray()
        self.create_system_tray_menu()
    

    def icon_setup(self) -> None:
        self.python_icon = ctk.CTkImage(light_image=Image.open("assets/desktop/python_icon_dark.png"), dark_image=Image.open("assets/desktop/python_icon.png"), size=(40, 40))
        self.snake_icon = ctk.CTkImage(light_image=Image.open("assets/desktop/snake_blue_icon.png"), dark_image=Image.open("assets/desktop/snake_yellow_icon.png"), size=(32, 32))
        self.no_network_icon = ctk.CTkImage(light_image=Image.open("assets/desktop/no_internet_icon_dark.png"), dark_image=Image.open("assets/desktop/no_internet_icon.png"), size=(20, 20))
        self.network_icon = ctk.CTkImage(light_image=Image.open("assets/desktop/wifi_icon_dark.png"), dark_image=Image.open("assets/desktop/wifi_icon.png"), size=(20, 20))
        self.network_icon_off = ctk.CTkImage(light_image=Image.open("assets/desktop/wifi_icon.png"), dark_image=Image.open("assets/desktop/wifi_icon_dark.png"), size=(32, 32))
        self.py_browse_icon = ctk.CTkImage(light_image=Image.open("assets/desktop/pybrowse_dark.png"), dark_image=Image.open("assets/desktop/pybrowse.png"), size=(32, 32))

    
    def create_taskbar(self) -> None:
        self.taskbar = ctk.CTkFrame(self.desktop_window_details["window"], height=46, width=self.desktop_window_details["width"], fg_color=desktop_colors, corner_radius=0)
        self.taskbar.place(anchor="s", relx=0.5, rely=1)
        self.taskbar.lift()

        self.taskbar_app_frame = ctk.CTkFrame(self.taskbar, fg_color="transparent")
        self.taskbar_app_frame.place(anchor="center", relx=0.5, rely=0.5)

        self.start_button = ctk.CTkButton(self.taskbar, text="", image=self.python_icon, width=45, height=45, fg_color="transparent", 
                                          command=self.callbacks["toggle_start_menu"], hover_color=desktop_highlight_colors)
        self.start_button.place(anchor="w", relx=0, rely=0.5)

        self.create_taskbar_apps()


    def create_start_menu(self) -> None:
        self.start_menu_frame = ctk.CTkFrame(self.desktop_window_details["window"], width=self.desktop_window_details["width"]/6, height=self.desktop_window_details["height"]/4, fg_color=desktop_off_colors)
        self.start_menu_frame.grid_propagate(False)
        self.start_menu_frame.lift()

        self.shut_down_button = ctk.CTkButton(self.start_menu_frame, width=self.desktop_window_details["width"]/20, height=self.desktop_window_details["height"]/20, text="Shut down", command=self.callbacks["quit"], 
                                              fg_color=button_color, font=(font_family, font_size_small), text_color=button_font_color, hover_color=button_hover_color)
        self.shut_down_button.grid(padx=self.desktop_window_details["height"] * 0.01, pady=self.desktop_window_details["height"] * 0.01)
        self.restart_button = ctk.CTkButton(self.start_menu_frame, width=self.desktop_window_details["width"]/20, height=self.desktop_window_details["height"]/20, text="Restart", command=self.callbacks["restart"], 
                                            fg_color=button_color, font=(font_family, font_size_small), text_color=button_font_color, hover_color=button_hover_color)
        self.restart_button.grid(padx=self.desktop_window_details["height"] * 0.01, pady=self.desktop_window_details["height"] * 0.01)


    def create_time_date(self) -> None:
        self.time_date_frame = ctk.CTkFrame(self.taskbar, width=self.desktop_window_details["width"]/20, height=45, fg_color="transparent")
        self.time_date_frame.place(anchor="e", relx=1, rely=0.5)
        self.clock = ctk.CTkLabel(self.time_date_frame, font=(font_family, font_size_xs), text_color=font_color, height=font_size_xs)
        self.clock.place(anchor="ne", relx=0.9, rely=0.1)
        self.date = ctk.CTkLabel(self.time_date_frame, font=(font_family, font_size_xs), text_color=font_color, height=font_size_xs)
        self.date.place(anchor="se", relx=0.9, rely=0.9)

    
    def update_date_time(self, time, date) -> None:
        """Updates the date and time every minute"""
        self.clock.configure(text=time)
        self.date.configure(text=date)

    
    def create_taskbar_apps(self) -> None:
        """Creates taskbar apps eg. browser, games..."""
        self.pybrowse = ctk.CTkButton(self.taskbar_app_frame, width=40, height=40, text="", command=lambda: self.callbacks["pybrowse"](),
                                                image=self.py_browse_icon, fg_color="transparent", hover_color=desktop_highlight_colors)
        self.pybrowse.grid(padx=self.desktop_window_details["width"]*0.005, row=0, column=0)

        self.python_game_button = ctk.CTkButton(self.taskbar_app_frame, command=lambda: self.callbacks["python"](), width=40, height=40, text="", 
                                                image=self.snake_icon, fg_color="transparent", hover_color=desktop_highlight_colors)
        self.python_game_button.grid(padx=self.desktop_window_details["width"]*0.005, row=0, column=1)


    def create_system_tray(self) -> None:
        """Creates icons for network etc"""
        self.system_tray_frame = ctk.CTkFrame(self.taskbar, height=45, width=self.desktop_window_details["width"] / 20, fg_color="transparent", bg_color="transparent")
        self.system_tray_frame.place(anchor="center", relx=0.95, rely=0.5)

        self.network = ctk.CTkButton(self.system_tray_frame, height=45, width=45, text="", image=self.no_network_icon, fg_color="transparent", 
                                      bg_color="transparent", hover_color=desktop_highlight_colors, command=self.callbacks["toggle_system_tray_menu"])
        self.network.grid()


    def create_system_tray_menu(self) -> None:
        """Creates a popup menu for network etc"""
        self.system_tray_menu_frame = ctk.CTkFrame(self.desktop_window_details["window"], width=self.desktop_window_details["width"]/6, height=self.desktop_window_details["height"]/4, fg_color=desktop_off_colors)
        self.system_tray_menu_frame.grid_propagate(False)
        
        self.network_frame = ctk.CTkFrame(self.system_tray_menu_frame, fg_color="transparent")
        self.network_frame.grid(padx=self.desktop_window_details["height"] * 0.01, pady=self.desktop_window_details["height"] * 0.01)
        self.network_button = ctk.CTkButton(self.network_frame, width=self.desktop_window_details["width"] * 0.05, height=self.desktop_window_details["height"] * 0.05, text="", hover_color=desktop_bright_colors, 
                                             command=self.callbacks["toggle_network"], fg_color=desktop_highlight_colors, image=self.network_icon_off)
        self.network_button.pack()
        self.network_label = ctk.CTkLabel(self.network_frame, text="Wi-Fi", font=(font_family, font_size_xs), text_color=font_color, fg_color="transparent")
        self.network_label.pack()


    def network_toggle(self, state: str):
        """Changes system tray and system tray menu icon and text of network"""
        match state:
            case "on":
                self.network_button.configure(fg_color=button_color, hover_color=button_hover_color)
                self.network.configure(image=self.network_icon)
                self.network_label.configure(text="Available")
            case "off":
                self.network_button.configure(fg_color=desktop_highlight_colors, hover_color=desktop_bright_colors)
                self.network.configure(image=self.no_network_icon)
                self.network_label.configure(text="Wi-Fi")
