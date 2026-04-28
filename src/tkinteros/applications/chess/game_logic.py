def get_possible_moves(board: list[list[str]], piece_coords: tuple[int, int]) -> list[tuple[int, int]]:
    piece_row, piece_col = piece_coords
    piece = board[piece_row][piece_col]
    possible_moves = []
    if not piece:
        return []
    piece_color = "black" if piece.startswith("B") else "white"
    piece_type = piece[1]
    if piece_type == "P":
        possible_moves = [(piece_row + 1, piece_col) if piece_color == "black" else (piece_row - 1, piece_col)]
    return possible_moves


def move_piece(board: list[list[str]], init_pos: tuple[int, int], dest_pos: tuple[int, int]) -> list[list[str]]:
    piece = board[init_pos[0]][init_pos[1]]
    board[init_pos[0]][init_pos[1]] = "  "
    board[dest_pos[0]][dest_pos[1]] = piece
    return board