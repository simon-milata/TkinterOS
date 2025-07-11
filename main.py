import sys, os
import time
import datetime

from desktop.desktop import DesktopGUI
from desktop.file_manager import FileManager
from desktop.task_bar import TaskBarGUI
from applications.python_game import PythonGame
from applications.pybrowse import PyBrowse
from desktop.text_editor import TextEditor
from desktop.file_widget import TextFileWidget


class OS:
    def __init__(self) -> None:
        self.appearance_mode = "dark"
        self.start_menu_open = False
        self.system_tray_menu_open = False
        self.network_on = False

        self.file_manager = FileManager()
        self.desktop_gui = DesktopGUI(self)

        self.callbacks = self.create_callbacks()
        self.desktop_window_details = self.create_desktop_window_details()

        self.task_bar = TaskBarGUI(self.desktop_window_details, self.callbacks)
        self.create_binds()
        self.load_files()
        self.update_taskbar_time()
        self.run()
        

    def create_binds(self) -> None:
        self.desktop_gui.desktop_frame.bind("<Button-1>", self.close_windows)
        self.desktop_gui.desktop_frame.bind("<Button-1>", self.get_click_position)
        self.desktop_gui.desktop_frame.bind("<Button-3>", self.create_desktop_context_menu_frame)
        self.desktop_gui.desktop_logo.bind("<Button-3>", lambda event: self.create_desktop_context_menu_frame(event, widget="logo"))
        self.desktop_gui.new_button.bind("<Enter>", self.creates_desktop_context_menu)

        self.desktop_gui.desktop_frame.bind("<B1-Motion>", self.create_selection_box)
        self.desktop_gui.desktop_frame.bind("<ButtonRelease-1>", self.delete_motion_area)


    def run(self) -> None:
        self.desktop_gui.run()

    
    def quit(self) -> None:
        sys.exit()

    
    def restart(self) -> None:
        # TODO: not working -> fix
        os.execl(sys.executable, sys.executable, *sys.argv)


    def create_desktop_window_details(self):
        return {
            "window": self.desktop_gui.WINDOW, 
            "width": self.desktop_gui.width,
            "height": self.desktop_gui.height
        }


    def create_callbacks(self):
        return {
            "toggle_start_menu": self.toggle_start_menu,
            "toggle_system_tray_menu": self.toggle_system_tray_menu,
            "toggle_network": self.toggle_network,
            "quit": self.quit,
            "restart": self.restart,
            "pybrowse": lambda: self.start_app("pybrowse"),
            "python": lambda: self.start_app("python")
        }


    def update_taskbar_time(self):
        now = datetime.datetime.now()
        self.task_bar.update_date_time(now.strftime("%H:%M"), now.strftime("%d.%m.%Y"))

        # Calculate milliseconds until the next full minute
        seconds_until_next_minute = 60 - now.second
        delay = seconds_until_next_minute * 1000

        self.desktop_gui.WINDOW.after(delay, self.update_taskbar_time)


    def close_windows(self, event) -> None:
        self.close_start_menu()
        self.close_utils_menu()
        self.close_desktop_context_menu()

    
    def toggle_start_menu(self) -> None:
        """Shows/hides start menu"""
        if not self.start_menu_open:
            self.task_bar.start_menu_frame.place(anchor="sw", relx=0, rely=0.96)
        else:
            self.task_bar.start_menu_frame.place_forget()
        self.start_menu_open = not self.start_menu_open

    
    def close_start_menu(self) -> None:
        """Hides start menu"""
        self.task_bar.start_menu_frame.place_forget()
        self.start_menu_open = False

        self.desktop_gui.desktop_actions_frame.place_forget()

    
    def create_desktop_context_menu_frame(self, event, widget = None) -> None:
        self.close_windows(None)
        if widget == "logo":
            self.desktop_gui.desktop_actions_frame.place(x=event.x+self.desktop_gui.width/2.29, y=event.y+self.desktop_gui.height/2.63)
        else:
            self.desktop_gui.desktop_actions_frame.place(x=event.x, y=event.y)


    def creates_desktop_context_menu(self, event) -> None:
        """Opens context menu when you right click on the desktop"""
        self.desktop_actions_frame_x = self.desktop_gui.desktop_actions_frame.winfo_rootx()
        self.desktop_actions_frame_y = self.desktop_gui.desktop_actions_frame.winfo_rooty()
        self.desktop_gui.new_action_frame.place(x=self.desktop_actions_frame_x + self.desktop_gui.desktop_actions_frame.winfo_width(), y=self.desktop_actions_frame_y - self.desktop_gui.desktop_actions_frame.winfo_height())

    
    def close_desktop_context_menu(self) -> None:
        """Closes context menu when you left click on the desktop"""
        self.desktop_gui.new_action_frame.place_forget()

    
    def load_files(self):
        """Creates icons for files"""
        for file in self.file_manager.file_objects:
            TextFileWidget(file, self.desktop_gui.WINDOW, self.open_file)


    def open_file(self, name):
        content = self.file_manager.get_file_content(name)
        TextEditor(name, content, self.close_file)


    def close_file(self, name, updated_content):
        self.file_manager.save_file_content(name, updated_content)


    def get_click_position(self, event):
        self.x_click_pos = event.x
        self.y_click_pos = event.y


    def create_selection_box(self, event) -> None:
        """Creates a selection box on left click drag on the desktop"""
        try:
            self.desktop_gui.motion_frame.destroy()
        except:
            pass
        
        if self.y_click_pos < event.y and self.x_click_pos < event.x:
            self.desktop_gui.create_selection_box_gui(self.x_click_pos, self.y_click_pos, event.x, event.y)

        elif self.y_click_pos > event.y and self.x_click_pos > event.x:
            self.desktop_gui.create_selection_box_gui(event.x, event.y, self.x_click_pos, self.y_click_pos)

        elif self.y_click_pos > event.y and self.x_click_pos < event.x:
            self.desktop_gui.create_selection_box_gui(self.x_click_pos, event.y, event.x, self.y_click_pos)

        elif self.y_click_pos < event.y and self.x_click_pos > event.x:
            self.desktop_gui.create_selection_box_gui(event.x, self.y_click_pos, self.x_click_pos, event.y)


    def delete_motion_area(self, event) -> None:
        try:
            self.desktop_gui.motion_frame.destroy()
        except:
            pass


    def start_app(self, game:str) -> None:
        match game:
            case "python":
                PythonGame(self, self.desktop_gui.WINDOW)
            case "pybrowse":
                self.py_browse = PyBrowse(self, self.desktop_gui.WINDOW)
                self.show_pybrowse_gui()


    def get_time(self) -> str:
        current_time = time.localtime(time.time())
        current_time = time.strftime("%H:%M", current_time)
        return current_time
    
    
    def get_date(self) -> str:
        current_date = time.localtime(time.time())
        current_date = time.strftime("%d/%m/%Y", current_date)
        return current_date
    

    def toggle_system_tray_menu(self) -> None:
        """Shows/hides system try menu"""
        if not self.system_tray_menu_open:
            self.task_bar.system_tray_menu_frame.place(anchor="se", relx=1, rely=0.96)
        else:
            self.task_bar.system_tray_menu_frame.place_forget()
        self.system_tray_menu_open = not self.system_tray_menu_open


    def toggle_network(self) -> None:
        """Changes system tray and system tray menu icon and text of network"""
        if not self.network_on:
            self.task_bar.network_toggle("on")
        else:
            self.task_bar.network_toggle("off")
        self.network_on = not self.network_on

    
    def close_utils_menu(self) -> None:
        self.task_bar.system_tray_menu_frame.place_forget()
        self.system_tray_menu_open = False


    def show_pybrowse_gui(self) -> None:
        if not self.network_on:
            self.py_browse.no_internet_frame.place(anchor="center", relx=0.5, rely=0.5)
        else:
            pass


if __name__ == "__main__":
    OS().run()
