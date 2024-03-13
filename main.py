import sys, os
import time

from desktop import DesktopGUI
from task_bar import TaskBar
from python_game import PythonGame

class OS:
    def __init__(self) -> None:
        self.gui = DesktopGUI(self)
        self.task_bar = TaskBar(self, self.gui)
        self.create_variables()
        self.create_binds()
        self.run()

    
    def create_variables(self) -> None:
        self.start_menu_open = False
        self.document_list = []


    def create_binds(self) -> None:
        self.gui.desktop_frame.bind("<Button-1>", self.close_windows)
        self.gui.desktop_frame.bind("<Button-1>", self.get_click_position)
        self.gui.desktop_frame.bind("<Button-3>", self.open_desktop_actions)
        self.gui.desktop_logo.bind("<Button-3>", lambda event: self.open_desktop_actions(event, widget="logo"))
        self.gui.new_button.bind("<Enter>", self.open_create_new_action)

        self.gui.desktop_frame.bind("<B1-Motion>", self.create_motion_area)
        self.gui.desktop_frame.bind("<ButtonRelease-1>", self.delete_motion_area)


    def run(self) -> None:
        self.gui.run()

    
    def quit(self) -> None:
        sys.exit()

    
    def restart(self) -> None:
        os.execl(sys.executable, sys.executable, *sys.argv)


    def close_windows(self, event) -> None:
        self.close_start_menu()
        self.close_new_action()

    
    def start_menu_mechanism(self) -> None:
        if not self.start_menu_open:
            self.task_bar.start_menu_frame.place(anchor="sw", relx=0, rely=0.96)
        else:
            self.task_bar.start_menu_frame.place_forget()
        self.start_menu_open = not self.start_menu_open

    
    def close_start_menu(self) -> None:
        self.task_bar.start_menu_frame.place_forget()
        self.start_menu_open = False

        self.gui.desktop_actions_frame.place_forget()

    
    def open_desktop_actions(self, event, widget = None) -> None:
        self.close_start_menu()
        self.close_new_action()
        if widget == "logo":
            self.gui.desktop_actions_frame.place(x=event.x+self.gui.width/2.29, y=event.y+self.gui.height/2.63)
        else:
            self.gui.desktop_actions_frame.place(x=event.x, y=event.y)


    def open_create_new_action(self, event) -> None:
        self.desktop_actions_frame_x = self.gui.desktop_actions_frame.winfo_rootx()
        self.desktop_actions_frame_y = self.gui.desktop_actions_frame.winfo_rooty()
        self.gui.new_action_frame.place(x=self.desktop_actions_frame_x + self.gui.desktop_actions_frame.winfo_width(), y=self.desktop_actions_frame_y - self.gui.desktop_actions_frame.winfo_height())

    
    def close_new_action(self) -> None:
        self.gui.new_action_frame.place_forget()


    def create_text_document(self) -> None:

        self.gui.create_text_document_gui(self.desktop_actions_frame_x, self.desktop_actions_frame_y)
        self.close_windows(None)


    def open_text_document(self) -> None:
        self.gui.create_text_document_open_gui()


    def get_click_position(self, event):
        self.x_click_pos = event.x
        self.y_click_pos = event.y


    def create_motion_area(self, event) -> None:
        try:
            self.gui.motion_frame.destroy()
        except:
            pass
        
        if self.y_click_pos < event.y and self.x_click_pos < event.x:
            self.gui.create_motion_area_gui(self.x_click_pos, self.y_click_pos, event.x, event.y)

        elif self.y_click_pos > event.y and self.x_click_pos > event.x:
            self.gui.create_motion_area_gui(event.x, event.y, self.x_click_pos, self.y_click_pos)

        elif self.y_click_pos > event.y and self.x_click_pos < event.x:
            self.gui.create_motion_area_gui(self.x_click_pos, event.y, event.x, self.y_click_pos)

        elif self.y_click_pos < event.y and self.x_click_pos > event.x:
            self.gui.create_motion_area_gui(event.x, self.y_click_pos, self.x_click_pos, event.y)


    def delete_motion_area(self, event) -> None:
        try:
            self.gui.motion_frame.destroy()
        except:
            pass


    def play_game(self, game:str) -> None:
        match game:
            case "python":
                PythonGame(self.gui.WINDOW)


    def get_time(self) -> str:
        current_time = time.localtime(time.time())
        current_time = time.strftime("%H:%M", current_time)
        return current_time
    
    
    def get_date(self) -> str:
        current_date = time.localtime(time.time())
        current_date = time.strftime("%d/%m/%Y", current_date)
        return current_date


if __name__ == "__main__":
    OS().run()
