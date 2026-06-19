from dataclasses import dataclass


@dataclass
class PieceDirections:
    ROOK = [
        (-1, 0), # down
        (1, 0), # up
        (0, 1), # right
        (0, -1), # left
    ]
    BISHOP = [
        (-1, -1), # \ up
        (1, 1), # \ down
        (-1, 1), # / up
        (1, -1), # / down
    ]
    ALL = [
        (-1, 0), # down
        (1, 0), # up
        (0, 1), # right
        (0, -1), # left

        (-1, -1), # \ up
        (1, 1), # \ down
        (-1, 1), # / up
        (1, -1), # / down
    ]
    KNIGHT = [
        (2, 1), # down right
        (-2, -1), # up left
        (2, -1), # down left
        (-2, 1), # up right

        (1, 2), # right down
        (-1, -2), # left up
        (-1, 2), # right up
        (1, -2) # left up
    ]
