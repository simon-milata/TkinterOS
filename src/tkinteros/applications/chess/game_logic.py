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
        possible_moves = get_move_range(piece_coords, opp_piece_col, board)
    
        
    while piece_coords in possible_moves:
        possible_moves.remove(piece_coords)
    
    return possible_moves


def move_piece(board: list[list[str]], init_pos: tuple[int, int], dest_pos: tuple[int, int]) -> list[list[str]]:
    piece = board[init_pos[0]][init_pos[1]]
    board[init_pos[0]][init_pos[1]] = "  "
    board[dest_pos[0]][dest_pos[1]] = piece
    return board


def get_move_range(piece_coords: tuple[int, int], opp_piece_col: str, board: list[list[str]]):
    piece_row, piece_col = piece_coords
    possible_moves = []

    directions = [
        (-1, 0), # down
        (1, 0), # up
        (0, 1), # right
        (0, -1), # left
    ]

    board_size = len(board)

    for y, x in directions:
        row, col = piece_row + y, piece_col + x

        while 0 <= row < board_size and 0 <= col < board_size:
            square = board[row][col]

            if square == "  ":
                possible_moves.append((row, col))
            else:
                if square[0] == opp_piece_col:
                    possible_moves.append((row, col))
                break

            row += y
            col += x
    return possible_moves