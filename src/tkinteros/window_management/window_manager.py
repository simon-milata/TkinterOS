import logging

from tkinteros.window_management.window import Window
from tkinteros.window_management.app_config import app_config

class WindowManager:
    def __init__(self):
        self.screen_dims = (1920, 1080)
        self.os_window = None
        self.windows = []


    def create_window(self, name, custom_title: str | None = None):
        app = app_config[name]
        if custom_title: app.title = custom_title
        app_window = Window(self.os_window, app, self.close_window, self.screen_dims)
        self.windows.append(app_window)
        self.log_windows()
        return app_window


    def close_window(self, name: str):
        logging.debug(f"Closing window '{name}'.")
        for index, window in enumerate(self.windows):
            if window.name == name:
                self.windows.pop(index)
                self.log_windows()
                return
            

    def log_windows(self):
        message = "Open windows: " + ", ".join([window.name for window in self.windows])
        logging.debug(message)