from tkinteros.applications.chess.config import PieceDirections

def get_possible_moves(board: list[list[str]], piece_coords: tuple[int, int]) -> list[tuple[int, int]]:
    piece_row, piece_col = piece_coords
    piece = board[piece_row][piece_col]
    piece_color = "B" if piece.startswith("B") else "W"
    opp_piece_col = "B" if piece.startswith("W") else "W"
    piece_type = piece[1]

    if not piece:
        return []
    
    possible_moves = []
    
    if piece_type == "P":
        possible_moves = [(piece_row + 1, piece_col) if piece_color == "B" else (piece_row - 1, piece_col)]

    if piece_type == "R":
        possible_moves = get_move_range(piece_coords, opp_piece_col, board, PieceDirections.ROOK)
    if piece_type == "B":
        possible_moves = get_move_range(piece_coords, opp_piece_col, board, PieceDirections.BISHOP)
    if piece_type == "K":
        possible_moves = get_move_range(piece_coords, opp_piece_col, board, PieceDirections.ALL, 1)
    if piece_type == "Q":
        possible_moves = get_move_range(piece_coords, opp_piece_col, board, PieceDirections.ALL)
    if piece_type == "N":
        possible_moves = get_move_range(piece_coords, opp_piece_col, board, PieceDirections.KNIGHT, 2)
        
    while piece_coords in possible_moves:
        possible_moves.remove(piece_coords)
    
    return possible_moves


def move_piece(board: list[list[str]], init_pos: tuple[int, int], dest_pos: tuple[int, int]) -> list[list[str]]:
    piece = board[init_pos[0]][init_pos[1]]
    board[init_pos[0]][init_pos[1]] = "  "
    board[dest_pos[0]][dest_pos[1]] = piece
    return board


def get_move_range(
        piece_coords: tuple[int, int], opp_piece_col: str, board: list[list[str]], 
        directions: list[tuple[int, int]], square_limit: int | None = None
    ):
    piece_row, piece_col = piece_coords
    possible_moves = []

    board_size = len(board)
    if not square_limit:
        square_limit = board_size

    for y, x in directions:
        row, col = piece_row + y, piece_col + x

        while 0 <= row < board_size and 0 <= col < board_size:
            square = board[row][col]

            if row > piece_row + square_limit or col > piece_col + square_limit or \
                row < piece_row - square_limit or col < piece_col - square_limit:
                break
            if square == "  ":
                possible_moves.append((row, col))
            else:
                if square[0] == opp_piece_col:
                    possible_moves.append((row, col))
                break

            row += y
            col += x
    return possible_moves