from tkinteros.applications.tictactoe.bot import TicTacToeBot

def test_win_horizontal():
    board = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", "O", "O", "O", " "],
        [" ", " ", " ", " ", " "]
    ]
    move = TicTacToeBot().move(board)
    assert move == (3, 4) or move == (3, 0)

    
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
    assert TicTacToeBot().move(board) == (0, 2)


def test_3_x_3_block_diagonal():
    board = [
        [" ", " ", " "],
        [" ", "X", " "],
        ["X", " ", " "]
    ]
    assert TicTacToeBot().move(board) == (0, 2)


def test_3_x_3_block_diagonal_space_inbetween():
    board = [
        [" ", " ", "X"],
        [" ", " ", " "],
        ["X", " ", " "]
    ]
    assert TicTacToeBot().move(board) == (1, 1)


def test_3_x_3_last_cell():
    board = [
        ["O", "O", "X"],
        ["X", " ", "O"],
        ["X", "X", "O"]
    ]
    assert TicTacToeBot().move(board) == (1, 1)


def test_3_x_3_second_move_middle_block():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", "X"]
    ]
    assert TicTacToeBot().move(board) == (1, 1)


def test_block_horizontal():
    board = [
            [" ", " ", " ", " ", "O"],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "X", "X", " "],
            [" ", " ", " ", " ", " "]
        ]
    move = TicTacToeBot().move(board)
    assert move == (3, 1) or move == (3, 4) or move == (3, 0)


def test_block_beginning():
    board = [
            ["O", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "X", " ", " "],
            [" ", "X", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]
    move = TicTacToeBot().move(board)
    assert move == (1, 3) or move == (4, 0) or move == (0, 4)


def test_max_depth_not_zero():
    board = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", "X", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]
    assert TicTacToeBot().get_max_depth(board) != 0


# TODO: might add this in the future to make bot more challenging
# def test_block():
#     board = [
#             ["O", "O", " ", " ", "O"],
#             [" ", "X", " ", "X", " "],
#             [" ", " ", "X", " ", " "],
#             [" ", "X", " ", " ", " "],
#             ["O", " ", " ", " ", " "]
#         ]

#     assert TicTacToeBot(max_depth=5).move(board) != (0, 2)