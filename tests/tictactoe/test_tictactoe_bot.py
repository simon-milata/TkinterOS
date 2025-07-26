from tkinteros.applications.tictactoe.bot import TicTacToeBot

def test_win_horizontal():
    board = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", "O", "O", "O", " "],
        [" ", " ", " ", " ", " "]
    ]
    assert TicTacToeBot().move(board) == (3, 4) or (4, 3)

    
def test_win_vertical():
    board = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "X"],
        ["O", " ", " ", " ", "X"],
        ["O", " ", "X", "X", " "],
        [" ", " ", " ", " ", " "]
    ]
    assert TicTacToeBot().move(board) == (1, 0)


def test_3_x_3_win_diagonal():
    board = [
        [" ", " ", " "],
        [" ", "O", " "],
        ["O", " ", " "]
    ]
    assert TicTacToeBot(max_depth=None).move(board) == (0, 2)


def test_3_x_3_block_diagonal():
    board = [
        [" ", " ", " "],
        [" ", "X", " "],
        ["X", " ", " "]
    ]
    assert TicTacToeBot(max_depth=None).move(board) == (0, 2)


def test_3_x_3_block_diagonal_space_inbetween():
    board = [
        [" ", " ", "X"],
        [" ", " ", " "],
        ["X", " ", " "]
    ]
    assert TicTacToeBot(max_depth=None).move(board) == (1, 1)


def test_3_x_3_last_cell():
    board = [
        ["O", "O", "X"],
        ["X", " ", "O"],
        ["X", "X", "O"]
    ]
    assert TicTacToeBot(max_depth=None).move(board) == (1, 1)


def test_3_x_3_second_move_middle_block():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", "X"]
    ]
    assert TicTacToeBot(max_depth=None).move(board) == (1, 1)


def test_block_horizontal():
    board = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "X", "X", " "],
            [" ", " ", " ", " ", " "]
        ]

    assert TicTacToeBot().move(board) == (3, 1) or (3, 4)
