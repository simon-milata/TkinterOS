import time
import logging


class TicTacToeBot:
    def __init__(self, ai_symbol: str = "O", player_symbol: str = "X", 
                 empty_cell: str = " ", points_to_win: int = 4, max_depth: int | None = 4):
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol
        self.empty_cell = empty_cell
        self.points_to_win = points_to_win
        self.max_depth = max_depth


    def move(self, board_list: list[list[str]]):
        return self.best_move(board_list)
    

    def evaluate_winner(self, window: list[str]):
        window_set = set(window)
        if len(window_set) == 1 and list(window_set)[0] != self.empty_cell:
            return list(window_set)[0]
        return None


    def evaluate_game_state(self, board_list: list[list[str]]) -> str:
        """
            Checks if the game is over and returns the symbol of the play that won.
            Returns None if the game is not over and returns "tie" if all cells are filled.
        """
        board_size = len(board_list)
        window_size = self.points_to_win

        windows = []

        # Horizontal
        for row in range(board_size):
            for col in range(board_size - window_size + 1):
                windows.append(board_list[row][col:col+window_size])

        # Vertical
        for col in range(board_size):
            for row in range(board_size - window_size + 1):
                window = []
                for k in range(window_size):
                    window.append(board_list[row + k][col])
                windows.append(window)

        # Diagonal (\)
        for row in range(board_size - window_size + 1):
            for col in range(board_size - window_size + 1):
                window = []
                for k in range(window_size):
                    window.append(board_list[row + k][col + k])
                windows.append(window)

        # Diagonal (/)
        for row in range(window_size - 1, board_size):
            for col in range(board_size - window_size + 1):
                window = []
                for k in range(window_size):
                    window.append(board_list[row - k][col + k])
                windows.append(window)

        # Check if someone won
        for window in windows:
            winner = self.evaluate_winner(window)
            if winner:
                return winner
            
        # Check if the board is full
        is_full = all(cell != self.empty_cell for row in board_list for cell in row)
        if is_full:
            return "tie"

        return None  # Game still in progress


    def heuristic(self, board: list[list[str]]):
        # TODO
        return 0


    def minimax(self, board, is_maximizing: bool, depth: int = 0, 
                alpha: float = -float("inf"), beta: float = float("inf")):
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
                        break
                if beta <= alpha:
                    break
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
                        break
                if beta <= alpha:
                    break
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
                    logging.debug(f"Move {(row, col)} has score {score}")

                    if score == 1:
                        return (row, col)
                    
                    if score > best_score:
                        best_score = score
                        move = (row, col)

        logging.debug(f"Finding the best move with a score {best_score} move took {(time.time() - start_time):.2f}s")

        return move
