from tkinteros.applications.chess.game_logic import get_possible_moves, move_piece
from tkinteros.applications.chess.gui import ChessGUI

class ChessController:
    def __init__(self):
        self.board = self.create_board()
        self.gui = ChessGUI()
        self.gui.draw_board(self.board)
        self.gui.draw_pieces(self.board, self.display_possible_moves)
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
    

    def move_piece(self, dest_pos: tuple[int, int]):
        self.board = move_piece(self.board, self.selected_piece_pos, dest_pos)
        self.gui.clear_highlights()
        self.gui.draw_pieces(self.board, self.display_possible_moves)
    

    def display_possible_moves(self, board: list[list[str]], piece_coords: tuple[int, int]):
        self.selected_piece_pos = piece_coords
        self.gui.clear_highlights()
        possible_moves = get_possible_moves(board, piece_coords)
        self.gui.highlight_possible_moves(possible_moves, self.move_piece)

    

if __name__ == "__main__":
    ChessController()