from typing import Optional

def evaluate_winner(window: list[str], empty_cell: str = " ") -> Optional[str]:
    """
        Return winning symbol if all cells in window are equal and not empty
        otherwise return None.
    """
    window_set = set(window)
    if len(window_set) == 1 and list(window_set)[0] != empty_cell:
        return list(window_set)[0]
    return None


def get_move_count(board: list[list[str]], empty_cell: str = " ") -> int:
    """Count non-empty cells on the board."""
    count = 0
    for row in board:
        for cell in row:
            count += 1 if cell != empty_cell else 0
    return count


def get_points_to_win(board_size: int) -> int:
    """Return required points to win based on board size."""
    if board_size == 3:
        return 3
    elif board_size == 5:
        return 4
    return board_size - 1


def get_board_windows(board: list[list[str]]) -> list[list[str]]:
    """Return all rows, columns, and diagonals of board as windows."""
    board_size = len(board)
    window_size = get_points_to_win(board_size)
    windows = []

    # Horizontal
    for row in range(board_size):
        for col in range(board_size - window_size + 1):
            windows.append(board[row][col:col+window_size])

    # Vertical
    for col in range(board_size):
        for row in range(board_size - window_size + 1):
            window = []
            for k in range(window_size):
                window.append(board[row + k][col])
            windows.append(window)

    # Diagonal (\)
    for row in range(board_size - window_size + 1):
        for col in range(board_size - window_size + 1):
            window = []
            for k in range(window_size):
                window.append(board[row + k][col + k])
            windows.append(window)

    # Diagonal (/)
    for row in range(window_size - 1, board_size):
        for col in range(board_size - window_size + 1):
            window = []
            for k in range(window_size):
                window.append(board[row - k][col + k])
            windows.append(window)

    return windows


def evaluate_game_state(board: list[list[str]], empty_cell: str = " ") -> str:
    """Return winner symbol, "tie" if full board, or None if ongoing."""
    windows = get_board_windows(board)

    for window in windows:
        winner = evaluate_winner(window)
        if winner:
            return winner
        
    # Check if the board is full
    is_full = all(cell != empty_cell for row in board for cell in row)
    if is_full:
        return "tie"

    return None  # Game still in progress