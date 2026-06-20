import logging

from tkinteros.window_management.window import Window

class WindowManager:
    def __init__(self):
        self.windows = []


    def create_window(self, master, name):
        app_window = Window(master, name, self.close_window)
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