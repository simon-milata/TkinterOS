from PIL import Image
from typing import Callable
from callback_management.callbacks import Callback

import customtkinter as ctk

from theme import THEME_COLORS, THEME_FONTS
from asset_management.asset_manager import AssetManager
from asset_management.assets import DesktopAssets


class TaskbarGUI:
    def __init__(self, desktop_window_details: dict[str, any], callbacks: dict[str, Callable], asset_manager: AssetManager) -> None:
        self.asset_manager = asset_manager
        self.desktop_window_details = desktop_window_details
        self.callbacks = callbacks

        self.icon_setup()
        self.create_taskbar()
        self.create_start_menu()
        self.create_time_date()
        self.create_system_tray()
        self.create_system_tray_menu()
    

    def icon_setup(self) -> None:
        self.python_icon = ctk.CTkImage(
            light_image=self.asset_manager.get_image(DesktopAssets.START_LOGO_DARK),
            dark_image=self.asset_manager.get_image(DesktopAssets.START_LOGO_LIGHT),
            size=(40, 40)
        )

        self.snake_icon = ctk.CTkImage(
            light_image=self.asset_manager.get_image(DesktopAssets.SNAKE_GAME_DARK),
            dark_image=self.asset_manager.get_image(DesktopAssets.SNAKE_GAME_LIGHT),
            size=(32, 32)
        )

        self.no_network_icon = ctk.CTkImage(
            light_image=self.asset_manager.get_image(DesktopAssets.NO_INTERNET_DARK),
            dark_image=self.asset_manager.get_image(DesktopAssets.NO_INTERNET_LIGHT),
            size=(20, 20)
        )

        self.network_icon = ctk.CTkImage(
            light_image=self.asset_manager.get_image(DesktopAssets.WIFI_ICON_DARK),
            dark_image=self.asset_manager.get_image(DesktopAssets.WIFI_ICON_LIGHT),
            size=(20, 20)
        )

        self.network_icon_off = ctk.CTkImage(
            light_image=self.asset_manager.get_image(DesktopAssets.WIFI_ICON_LIGHT),
            dark_image=self.asset_manager.get_image(DesktopAssets.WIFI_ICON_DARK),
            size=(32, 32)
        )

        self.py_browse_icon = ctk.CTkImage(
            light_image=self.asset_manager.get_image(DesktopAssets.PYBROWSE_DARK),
            dark_image=self.asset_manager.get_image(DesktopAssets.PYBROWSE_LIGHT),
            size=(32, 32)
        )

    
    def create_taskbar(self) -> None:
        self.taskbar = ctk.CTkFrame(self.desktop_window_details["window"], height=46, width=self.desktop_window_details["width"], fg_color=THEME_COLORS.primary, corner_radius=0)
        self.taskbar.place(anchor="s", relx=0.5, rely=1)
        self.taskbar.lift()

        self.taskbar_app_frame = ctk.CTkFrame(self.taskbar, fg_color="transparent")
        self.taskbar_app_frame.place(anchor="center", relx=0.5, rely=0.5)

        self.start_button = ctk.CTkButton(self.taskbar, text="", image=self.python_icon, width=45, height=45, fg_color="transparent", 
                                          command=self.callbacks[Callback.TOGGLE_START_MENU], hover_color=THEME_COLORS.highlight)
        self.start_button.place(anchor="w", relx=0, rely=0.5)

        self.create_taskbar_apps()


    def create_start_menu(self) -> None:
        self.start_menu_frame = ctk.CTkFrame(self.desktop_window_details["window"], width=self.desktop_window_details["width"]/6, height=self.desktop_window_details["height"]/4, fg_color=THEME_COLORS.off)
        self.start_menu_frame.grid_propagate(False)
        self.start_menu_frame.lift()

        self.shut_down_button = ctk.CTkButton(self.start_menu_frame, width=self.desktop_window_details["width"]/20, height=self.desktop_window_details["height"]/20, text="Shut down", command=self.callbacks[Callback.QUIT], 
                                              fg_color=THEME_COLORS.button, font=(THEME_FONTS.family, THEME_FONTS.small), text_color=THEME_COLORS.button_font_color, hover_color=THEME_COLORS.button_hover)
        self.shut_down_button.grid(padx=self.desktop_window_details["height"] * 0.01, pady=self.desktop_window_details["height"] * 0.01)
        self.restart_button = ctk.CTkButton(self.start_menu_frame, width=self.desktop_window_details["width"]/20, height=self.desktop_window_details["height"]/20, text="Restart", command=self.callbacks[Callback.RESTART], 
                                            fg_color=THEME_COLORS.button, font=(THEME_FONTS.family, THEME_FONTS.small), text_color=THEME_COLORS.button_font_color, hover_color=THEME_COLORS.button_hover)
        self.restart_button.grid(padx=self.desktop_window_details["height"] * 0.01, pady=self.desktop_window_details["height"] * 0.01)


    def create_time_date(self) -> None:
        self.time_date_frame = ctk.CTkFrame(self.taskbar, width=self.desktop_window_details["width"]/20, height=45, fg_color="transparent")
        self.time_date_frame.place(anchor="e", relx=1, rely=0.5)
        self.clock = ctk.CTkLabel(self.time_date_frame, font=(THEME_FONTS.family, THEME_FONTS.extra_small), text_color=THEME_COLORS.font_color, height=THEME_FONTS.extra_small)
        self.clock.place(anchor="ne", relx=0.9, rely=0.1)
        self.date = ctk.CTkLabel(self.time_date_frame, font=(THEME_FONTS.family, THEME_FONTS.extra_small), text_color=THEME_COLORS.font_color, height=THEME_FONTS.extra_small)
        self.date.place(anchor="se", relx=0.9, rely=0.9)

    
    def update_date_time(self, time, date) -> None:
        """Updates the date and time every minute"""
        self.clock.configure(text=time)
        self.date.configure(text=date)

    
    def create_taskbar_apps(self) -> None:
        """Creates taskbar apps eg. browser, games..."""
        self.pybrowse = ctk.CTkButton(self.taskbar_app_frame, width=40, height=40, text="", command=lambda: self.callbacks[Callback.PYBROWSE](),
                                                image=self.py_browse_icon, fg_color="transparent", hover_color=THEME_COLORS.highlight)
        self.pybrowse.grid(padx=self.desktop_window_details["width"]*0.005, row=0, column=0)

        self.python_game_button = ctk.CTkButton(self.taskbar_app_frame, command=lambda: self.callbacks[Callback.PYTHON](), width=40, height=40, text="", 
                                                image=self.snake_icon, fg_color="transparent", hover_color=THEME_COLORS.highlight)
        self.python_game_button.grid(padx=self.desktop_window_details["width"]*0.005, row=0, column=1)


    def create_system_tray(self) -> None:
        """Creates icons for network etc"""
        self.system_tray_frame = ctk.CTkFrame(self.taskbar, height=45, width=self.desktop_window_details["width"] / 20, fg_color="transparent", bg_color="transparent")
        self.system_tray_frame.place(anchor="center", relx=0.95, rely=0.5)

        self.network = ctk.CTkButton(self.system_tray_frame, height=45, width=45, text="", image=self.no_network_icon, fg_color="transparent", 
                                      bg_color="transparent", hover_color=THEME_COLORS.highlight, command=self.callbacks[Callback.TOGGLE_SYSTEM_TRAY_MENU])
        self.network.grid()


    def create_system_tray_menu(self) -> None:
        """Creates a popup menu for network etc"""
        self.system_tray_menu_frame = ctk.CTkFrame(self.desktop_window_details["window"], width=self.desktop_window_details["width"]/6, height=self.desktop_window_details["height"]/4, fg_color=THEME_COLORS.off)
        self.system_tray_menu_frame.grid_propagate(False)
        
        self.network_frame = ctk.CTkFrame(self.system_tray_menu_frame, fg_color="transparent")
        self.network_frame.grid(padx=self.desktop_window_details["height"] * 0.01, pady=self.desktop_window_details["height"] * 0.01)
        self.network_button = ctk.CTkButton(self.network_frame, width=self.desktop_window_details["width"] * 0.05, height=self.desktop_window_details["height"] * 0.05, text="", hover_color=THEME_COLORS.bright, 
                                             command=self.callbacks[Callback.TOGGLE_NETWORK], fg_color=THEME_COLORS.highlight, image=self.network_icon_off)
        self.network_button.pack()
        self.network_label = ctk.CTkLabel(self.network_frame, text="Wi-Fi", font=(THEME_FONTS.family, THEME_FONTS.extra_small), text_color=THEME_COLORS.font_color, fg_color="transparent")
        self.network_label.pack()


    def network_toggle(self, state: str):
        """Changes system tray and system tray menu icon and text of network"""
        match state:
            case "on":
                self.network_button.configure(fg_color=THEME_COLORS.button, hover_color=THEME_COLORS.button_hover)
                self.network.configure(image=self.network_icon)
                self.network_label.configure(text="Available")
            case "off":
                self.network_button.configure(fg_color=THEME_COLORS.highlight, hover_color=THEME_COLORS.bright)
                self.network.configure(image=self.no_network_icon)
                self.network_label.configure(text="Wi-Fi")
