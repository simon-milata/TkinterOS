from tkinteros.applications.chess.gui import ChessGUI

class ChessController:
    def __init__(self):
        self.board = self.create_board()
        self.gui = ChessGUI()
        self.gui.draw_board(self.board)
        self.gui.draw_pieces(self.board)
        self.gui.show_game_frame()
        self.gui.run()


    def create_board(self):
        return [
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
            ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
            ["WR", "WN", "WW", "WQ", "WK", "WW", "WN", "WR"],
        ]
    

if __name__ == "__main__":
    ChessController()