import time
import logging
import random


class TicTacToeBot:
    def __init__(self, ai_symbol: str = "O", player_symbol: str = "X", random_start: bool = False,
                 empty_cell: str = " ", points_to_win: int = 4, max_depth: int | None = 4):
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol
        self.empty_cell = empty_cell
        self.points_to_win = points_to_win
        self.max_depth = max_depth
        self.random_start = random_start


    def move(self, board: list[list[str]]):
        self.times_ran = 0
        if self.random_start and self.get_move_count(board) < 3:
            while True:
                random_move = (random.randint(0, len(board) - 1), random.randint(0, len(board) - 1))
                if board[random_move[0]][random_move[1]] == " ":
                    return random_move

        return self.best_move(board)
    

    def get_move_count(self, board: list[list[str]]) -> int:
        count = 0
        for row in board:
            for cell in row:
                count += 1 if cell != self.empty_cell else 0
        return count
    

    def evaluate_winner(self, window: list[str]):
        window_set = set(window)
        if len(window_set) == 1 and list(window_set)[0] != self.empty_cell:
            return list(window_set)[0]
        return None
    

    def get_board_windows(self, board: list[list[str]]) -> list[list[str]]:
        board_size = len(board)
        window_size = self.points_to_win
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


    def evaluate_game_state(self, board: list[list[str]]) -> str:
        """
            Checks if the game is over and returns the symbol of the play that won.
            Returns None if the game is not over and returns "tie" if all cells are filled.
        """
        windows = self.get_board_windows(board)

        for window in windows:
            winner = self.evaluate_winner(window)
            if winner:
                return winner
            
        # Check if the board is full
        is_full = all(cell != self.empty_cell for row in board for cell in row)
        if is_full:
            return "tie"

        return None  # Game still in progress


    def heuristic(self, board: list[list[str]]):
        score = 0

        windows = self.get_board_windows(board=board)

        for window in windows:
            if window.count(self.ai_symbol) == self.points_to_win - 1 and window.count(self.empty_cell) == 1:
                score += 1
            if window.count(self.player_symbol) == self.points_to_win - 1 and window.count(self.empty_cell) == 1:
                score -= 1.0
            if window.count(self.ai_symbol) == self.points_to_win // 2 and window.count(self.empty_cell) == self.points_to_win // 2:
                score += 0.1
            if window.count(self.player_symbol) == self.points_to_win / 2 and window.count(self.empty_cell) == self.points_to_win // 2:
                score -= 0.1

        # Normalize to [-1, 1]
        if windows:
            score /= len(windows)

        score = max(-1, min(1, score))

        return score


    def minimax(self, board, is_maximizing: bool, depth: int = 0, 
                alpha: float = -float("inf"), beta: float = float("inf")):
        self.times_ran += 1
        result = self.evaluate_game_state(board)
        if result == self.ai_symbol:
            return 1 / (depth + 1)  # prefer quicker wins
        elif result == self.player_symbol:
            return -1 / (depth + 1)  # prefer later losses
        elif result == "tie":
            return 0

        if self.max_depth and depth >= self.max_depth:
            return self.heuristic(board)

        board_size = len(board)

        if is_maximizing:
            max_score = -float("inf")
            for row in range(board_size):
                for col in range(board_size):
                    if board[row][col] != self.empty_cell:
                        continue
                    board[row][col] = self.ai_symbol
                    score = self.minimax(board, False, depth + 1, alpha, beta)
                    board[row][col] = self.empty_cell
                    max_score = max(max_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        return max_score
            return max_score
        else:
            min_score = float("inf")
            for row in range(board_size):
                for col in range(board_size):
                    if board[row][col] != self.empty_cell:
                        continue
                    board[row][col] = self.player_symbol
                    score = self.minimax(board, True, depth + 1, alpha, beta)
                    board[row][col] = self.empty_cell
                    min_score = min(min_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        return min_score
            return min_score


    def best_move(self, board: list[list[str]]):
        board_size = len(board)
        best_score = -float("inf")
        move = None

        start_time = time.time()

        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == " ":
                    board[row][col] = self.ai_symbol
                    score = self.minimax(board, False)
                    board[row][col] = " "
                    # print(f"Move {(row, col)} has a score of {score}", end='\r')

                    if score == 1:
                        return (row, col)
                    
                    if score > best_score:
                        best_score = score
                        move = (row, col)

        logging.debug("")
        logging.debug(f"Finding the best move with a score {best_score} move took {(time.time() - start_time):.2f}s.")
        logging.debug(f"Minimax ran {self.times_ran} times.")
        
        return move
