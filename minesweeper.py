from top_window import TopWindow
from under_cell import *


class FrameOfCells:
    def __init__(self, window, width, height, nr_bombs):
        under_cells_field = CellField(window, width, height, nr_bombs)


class Minesweeper:
    def __init__(self, window, width=10, height=10):  # width=15, height=12):
        self.nr_bombs = int(width * height / 6)
        self.total_cells = width * height
        self.width = width
        self.height = height

        self.top_window = TopWindow(window, self.nr_bombs)
        self.frame_of_cells = FrameOfCells(window, width, height, self.nr_bombs)
