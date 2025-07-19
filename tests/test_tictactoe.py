from tkinteros.applications.tictactoe.tictactoe import TicTacToe


def test_none():
    """Nothing should be returned and the game should continue"""
    game = TicTacToe()
    board_list = [
        ['X', 'O', 'X', ' ', ' '],
        [' ', 'O', ' ', 'O', ' '],
        [' ', ' ', 'X', ' ', 'O'],
        [' ', 'X', 'O', 'O', 'X'],
        ['O', ' ', ' ', 'X', 'X'],
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") is None


def test_none_3_with_space():
    """
        Nothing should be returned and the game should continue. 
        Counts should reset when going to the second list.
    """
    game = TicTacToe()
    board_list = [
        [' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") is None


def test_none_3_with_space():
    """Nothing should be returned and the game should continue"""
    game = TicTacToe()
    board_list = [
        ['X', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") is None


def test_draw():
    game = TicTacToe()
    board_list = [
        ['X', 'O', 'X', 'O', 'X'],
        ['O', 'X', 'O', 'X', 'O'],
        ['X', 'O', 'X', 'O', 'X'],
        ['O', 'X', 'O', 'X', 'O'],
        ['X', 'O', 'X', 'O', 'X']
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") == "draw"


def test_x_win_horizontal():
    game = TicTacToe()
    board_list = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', 'X', 'X', 'X', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") == "X"

def test_o_win_vertical():
    game = TicTacToe()
    board_list = [
        [' ', ' ', 'O', ' ', ' '],
        [' ', ' ', 'O', ' ', ' '],
        [' ', ' ', 'O', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") == "O"


def test_x_win_diagonal_top_right():
    game = TicTacToe()
    board_list = [
        [' ', ' ', 'X', ' ', ' '],
        [' ', ' ', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', 'X'],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") == "X"


def test_x_win_diagonal_bottom_left():
    game = TicTacToe()
    board_list = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['X', ' ', ' ', ' ', ' '],
        [' ', 'X', ' ', ' ', ' '],
        [' ', ' ', 'X', ' ', ' ']
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") == "X"


def test_o_win_anti_diagonal_top_left():
    game = TicTacToe()
    board_list = [
        [' ', ' ', 'O', ' ', ' '],
        [' ', 'O', ' ', ' ', ' '],
        ['O', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") == "O"


def test_o_win_anti_diagonal_bottom_left():
    game = TicTacToe()
    board_list = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'O'],
        [' ', ' ', ' ', 'O', ' '],
        [' ', ' ', 'O', ' ', ' ']
    ]
    assert game.evaluate_game_state(board_list=board_list, board_size=5, empty_cell=" ") == "O"