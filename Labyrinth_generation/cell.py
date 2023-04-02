from enum import Enum


class Cell(Enum):
    PATH = 0
    WALL = 1
    START = 2
    END = 3
    SOLVED = 4
