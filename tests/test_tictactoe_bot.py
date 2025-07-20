from tkinteros.applications.tictactoe.tictactoe_bot import TicTacToeBot

def test_win_horizontal():
    board_list = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', 'O', 'O', 'O', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]

    assert TicTacToeBot().move(board_list) == (3, 4) or (4, 3)

    
def test_win_vertical():
    board_list = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'X'],
        ['O', ' ', ' ', ' ', 'X'],
        ['O', ' ', 'X', 'X', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]

    assert TicTacToeBot().move(board_list) == (1, 0)

# TODO
# def test_block_horizontal():
#     board_list = [
#             [' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' '],
#             [' ', 'X', 'X', 'X', ' '],
#             [' ', ' ', ' ', ' ', ' ']
#         ]

#     assert TicTacToeBot().move(board_list) == (3, 4)
