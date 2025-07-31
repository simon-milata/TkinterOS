import tkinteros.applications.tictactoe.game_logic as game_logic


def test_none():
    """Nothing should be returned and the game should continue"""
    board = [
        ["X", "O", "X", " ", " "],
        [" ", "O", " ", "O", " "],
        [" ", " ", "X", " ", "O"],
        [" ", "X", "O", "O", "X"],
        ["O", " ", " ", "X", "X"],
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "ongoing"


def test_no_winner_with_reset_on_horizontal_windows():
    """Ensure counting resets correctly when scanning horizontal rows."""
    board = [
        [" ", " ", " ", "X", "X"],
        ["X", "X", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "ongoing"


def test_no_winner_with_reset_on_vertical_windows():
    """Ensure counting resets correctly when scanning vertical columns."""
    board = [
        [" ", "X", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        ["X", " ", " ", " ", " "],
        ["X", " ", " ", " ", " "],
        ["X", " ", " ", " ", " "],
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "ongoing"


def test_no_winner_with_reset_on_diagonal_windows():
    """Ensure counting resets correctly when scanning diagonal windows."""
    board = [
        [" ", " ", "X", " ", " "],
        [" ", "X", " ", " ", " "],
        [" ", "X", " ", " ", " "],
        ["X", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "ongoing"


def test_draw():
    board = [
        ["X", "O", "X", "O", "X"],
        ["O", "X", "X", "X", "O"],
        ["X", "O", "O", "O", "X"],
        ["O", "X", "O", "X", "O"],
        ["O", "X", "O", "X", "O"],
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "tie"


def test_x_win_horizontal():
    board = [
        [" ", " ", " ", " ", " "],
        [" ", "X", "X", "X", "X"],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "X"

def test_o_win_vertical():
    board = [
        [" ", " ", "O", " ", " "],
        [" ", " ", "O", " ", " "],
        [" ", " ", "O", " ", " "],
        [" ", " ", "O", " ", " "],
        [" ", " ", " ", " ", " "]
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "O"


def test_x_win_diagonal_top_right():
    board = [
        [" ", "X", " ", " ", " "],
        [" ", " ", "X", " ", " "],
        [" ", " ", " ", "X", " "],
        [" ", " ", " ", " ", "X"],
        [" ", " ", " ", " ", " "]
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "X"


def test_x_win_diagonal_bottom_left():
    board = [
        [" ", " ", " ", " ", " "],
        ["X", " ", " ", " ", " "],
        [" ", "X", " ", " ", " "],
        [" ", " ", "X", " ", " "],
        [" ", " ", " ", "X", " "]
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "X"


def test_o_win_anti_diagonal_top_left():
    board = [
        [" ", " ", " ", "O", " "],
        [" ", " ", "O", " ", " "],
        [" ", "O", " ", " ", " "],
        ["O", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "O"


def test_o_win_anti_diagonal_bottom_left():
    board = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "O"],
        [" ", " ", " ", "O", " "],
        [" ", " ", "O", " ", " "],
        [" ", "O", " ", " ", " "]
    ]
    assert game_logic.evaluate_game_state(board=board, empty_cell=" ")["status"] == "O"