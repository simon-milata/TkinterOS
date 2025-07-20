import customtkinter as ctk


class TicTacToeGUI:
    def __init__(self):
        self.create_variables()
        self.create_window()
        
        
    def run(self):
        print("running")
        self.window.mainloop()


    def check_cell(self, cell_button: ctk.CTkButton, player: str):
        cell_button.configure(text=player, state="disabled")


    def create_variables(self):
        self.window_width = 400
        self.window_height = 400
        

    def create_window(self) -> None:
        self.window = ctk.CTkToplevel()
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height))
        self.window.configure(fg_color="gray")
        self.window.title("Tic Tac Toe")
        self.window.attributes("-topmost", True)
        self.window.focus_force()
        self.window.resizable(False, False)
        # self.window.after(200, self.icon_setup)


    def create_grid_button(self, color: str, row: int, column: int, x: int, y: int, cell_size: int, callback):
        button = ctk.CTkButton(
                    self.window, width=cell_size, height=cell_size, 
                    corner_radius=0, text="", text_color="red", fg_color=color
                )
        button.configure(command=lambda b=button, r=row, c=column: callback(button=b, row=r, column=c))

        button.place(x=x, y=y)

        return button
