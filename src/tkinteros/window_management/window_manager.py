from src.tkinteros.window_management.window import Window

class WindowManager:
    def __init__(self):
        self.windows = []


    def create_window(self, master):
        self.windows.append(Window(master))
