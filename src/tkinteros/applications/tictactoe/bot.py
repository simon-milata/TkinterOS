import time
import logging
import random

import tkinteros.applications.tictactoe.game_logic as game_logic


class TicTacToeBot:
    def __init__(self, ai_symbol: str = "O", player_symbol: str = "X", random_start: bool = False, max_depth: int | None = 3):
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol
        self.max_depth = max_depth
        self.random_start = random_start


    def move(self, board: list[list[str]]):
        self.times_ran = 0
        # if self.random_start and game_logic.get_move_count(board) < 3:
        #     while True:
        #         random_move = (random.randint(0, len(board) - 1), random.randint(0, len(board) - 1))
        #         if board[random_move[0]][random_move[1]] == " ":
        #             return random_move

        return self.best_move(board)


    def heuristic(self, board: list[list[str]], empty_cell: str = " "):
        score = 0

        windows = game_logic.get_board_windows(board=board)
        points_to_win = game_logic.get_points_to_win(board_size=len(board))

        for window in windows:
            if window.count(self.ai_symbol) == points_to_win - 1 and window.count(empty_cell) == 1:
                score += 1.0
            if window.count(self.player_symbol) == points_to_win - 1 and window.count(empty_cell) == 1:
                score -= 1.0
            if window.count(self.ai_symbol) == points_to_win // 2 and window.count(empty_cell) == points_to_win // 2:
                score += 0.1
            if window.count(self.player_symbol) == points_to_win // 2 and window.count(empty_cell) == points_to_win // 2:
                score -= 0.1

        # Normalize to [-1, 1]
        if windows:
            score /= len(windows)

        score = max(-1, min(1, score))

        return score


    def minimax(self, board, is_maximizing: bool, depth: int = 0, empty_cell: str = " ",
                alpha: float = -float("inf"), beta: float = float("inf")):
        self.times_ran += 1
        result = game_logic.evaluate_game_state(board)["status"]
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
                    if board[row][col] != empty_cell:
                        continue
                    board[row][col] = self.ai_symbol
                    score = self.minimax(board, False, depth + 1, " ", alpha, beta)
                    board[row][col] = empty_cell
                    max_score = max(max_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        return max_score
            return max_score
        else:
            min_score = float("inf")
            for row in range(board_size):
                for col in range(board_size):
                    if board[row][col] != empty_cell:
                        continue
                    board[row][col] = self.player_symbol
                    score = self.minimax(board, True, depth + 1, " ", alpha, beta)
                    board[row][col] = empty_cell
                    min_score = min(min_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        return min_score
            return min_score
        

    def best_move(self, board: list[list[str]], empty_cell: str = " "):
        logging.info("Finding the best move...")
        board_size = len(board)
        best_score = -float("inf")
        move = None

        start_time = time.time()

        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == empty_cell:
                    board[row][col] = self.ai_symbol
                    score = self.minimax(board, False)
                    board[row][col] = empty_cell
                    logging.debug(f"Move {(row, col)} has a score of {score}.")

                    if score == 1:
                        return (row, col)
                    
                    if score > best_score:
                        best_score = score
                        move = (row, col)

        logging.info(f"Finding the best move with a score {best_score:.4f} move took {(time.time() - start_time):.2f}s.")
        logging.info(f"Minimax ran {self.times_ran} times.")
        
        return move
    

if __name__ == "__main__":
    logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(filename)s | %(message)s",
    datefmt="%H:%M:%S"
    )
    board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", "X"]
        ]
    TicTacToeBot(ai_symbol="O", player_symbol="X", max_depth=None).move(board)