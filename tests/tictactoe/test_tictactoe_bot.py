from tkinteros.applications.tictactoe.bot import TicTacToeBot

def test_win_horizontal():
    board_list = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", "O", "O", "O", " "],
        [" ", " ", " ", " ", " "]
    ]
    assert TicTacToeBot().move(board_list) == (3, 4) or (4, 3)

    
def test_win_vertical():
    board_list = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "X"],
        ["O", " ", " ", " ", "X"],
        ["O", " ", "X", "X", " "],
        [" ", " ", " ", " ", " "]
    ]
    assert TicTacToeBot().move(board_list) == (1, 0)


def test_3_x_3_win_diagonal():
    board_list = [
        [" ", " ", " "],
        [" ", "O", " "],
        ["O", " ", " "]
    ]
    assert TicTacToeBot(points_to_win=3, max_depth=None).move(board_list) == (0, 2)


def test_3_x_3_block_diagonal():
    board_list = [
        [" ", " ", " "],
        [" ", "X", " "],
        ["X", " ", " "]
    ]
    assert TicTacToeBot(points_to_win=3, max_depth=None).move(board_list) == (0, 2)


def test_3_x_3_block_diagonal_space_inbetween():
    board_list = [
        [" ", " ", "X"],
        [" ", " ", " "],
        ["X", " ", " "]
    ]
    assert TicTacToeBot(points_to_win=3, max_depth=None).move(board_list) == (1, 1)


def test_3_x_3_last_cell():
    board_list = [
        ["O", "O", "X"],
        ["X", " ", "O"],
        ["X", "X", "O"]
    ]
    assert TicTacToeBot(points_to_win=3, max_depth=None).move(board_list) == (1, 1)


def test_3_x_3_second_move_middle_block():
    board_list = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", "X"]
    ]
    assert TicTacToeBot(points_to_win=3, max_depth=None).move(board_list) == (1, 1)


def test_block_horizontal():
    board_list = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "X", "X", " "],
            [" ", " ", " ", " ", " "]
        ]

    assert TicTacToeBot().move(board_list) == (3, 1) or (3, 4)
