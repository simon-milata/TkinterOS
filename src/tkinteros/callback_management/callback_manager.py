from tkinteros.callback_management.callbacks import Callback

class CallbackManager:
    def __init__(self, os_manager):
        self.os_manager = os_manager
        self.callbacks = self.create_callbacks()


    def create_callbacks(self):
        return {
            Callback.TOGGLE_START_MENU: self.os_manager.toggle_start_menu,
            Callback.TOGGLE_SYSTEM_TRAY_MENU: self.os_manager.toggle_system_tray_menu,
            Callback.TOGGLE_NETWORK: self.os_manager.toggle_network,
            Callback.QUIT: self.os_manager.quit,
            Callback.RESTART: self.os_manager.restart,
            Callback.PYBROWSE: lambda: self.os_manager.start_app("pybrowse"),
            Callback.PYTHON: lambda: self.os_manager.start_app("python"),
            Callback.TICTACTOE: lambda: self.os_manager.start_app("tictactoe"),
            Callback.CREATE_TXT_FILE: lambda n: self.os_manager.create_txt_file(n),
            Callback.VALIDATE_FILE_NAME: lambda n: self.os_manager.validate_file_name(n)
        }