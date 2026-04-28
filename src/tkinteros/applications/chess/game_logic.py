def get_possible_moves(board: list[list[str]], piece_coords: tuple[int, int]) -> list[tuple[int, int]]:
    piece_row, piece_col = piece_coords
    piece = board[piece_row][piece_col]
    piece_color = "B" if piece.startswith("B") else "W"
    opp_piece_color = "B" if piece.startswith("W") else "W"
    piece_type = piece[1]

    if not piece:
        return []
    
    possible_moves = []
    
    if piece_type == "P":
        possible_moves = [(piece_row + 1, piece_col) if piece_color == "B" else (piece_row - 1, piece_col)]

    if piece_type == "R":
        # DOWN
        i = 0
        while True:
            i += 1
            if piece_row - i < 0:
                break
            if board[piece_row - i][piece_col][0] == opp_piece_color:
                possible_moves.append((piece_row - i, piece_col))
                break
            if board[piece_row - i][piece_col] != "  " or board[piece_row - i][piece_col][0] == piece_color:
                break
            
            possible_moves.append((piece_row - i, piece_col))
        # UP
        i = 0
        while True:
            i += 1
            if piece_row + i >= len(board):
                break
            if board[piece_row + i][piece_col].startswith(opp_piece_color):
                possible_moves.append((piece_row + i, piece_col))
                break
            if board[piece_row + 1][piece_col] != "  " or board[piece_row + i][piece_col][0] == piece_color:
                break
            possible_moves.append((piece_row + i, piece_col))
        # RIGHT
        i = 0
        while True:
            i += 1
            if piece_col + i >= len(board):
                break
            if board[piece_row][piece_col + i][0] == opp_piece_color:
                possible_moves.append((piece_row, piece_col + 1))
                break
            if board[piece_row][piece_col + i] != "  " or board[piece_row][piece_col + i][0] == piece_color:
                break
            possible_moves.append((piece_row, piece_col + i))
        # LEFT
        i = 0
        while True:
            i += 1
            if piece_col - i < 0:
                break
            if board[piece_row][piece_col - i][0] == opp_piece_color:
                possible_moves.append((piece_row, piece_col - 1))
                break
            if board[piece_row][piece_col - i] != "  " or board[piece_row][piece_col - i][0] == piece_color:
                break
            possible_moves.append((piece_row, piece_col - i))
    
        
    while piece_coords in possible_moves:
        possible_moves.remove(piece_coords)
    
    return possible_moves


def move_piece(board: list[list[str]], init_pos: tuple[int, int], dest_pos: tuple[int, int]) -> list[list[str]]:
    piece = board[init_pos[0]][init_pos[1]]
    board[init_pos[0]][init_pos[1]] = "  "
    board[dest_pos[0]][dest_pos[1]] = piece
    return board