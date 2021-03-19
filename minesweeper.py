from top_window import TopWindow


class UnderCellField:
    def __init__(self, window, width, height):
        pass


class UnderCell:
    def __init__(self):
        pass


class OverCellField:
    def __init__(self, window, width, height):
        pass


class OverCell:
    def __init__(self):
        pass


class FrameOfCells:
    def __init__(self, window, width, height):
        under_cells_field = UnderCellField(window, width, height)
        over_cells_field = OverCellField(window, width, height)


class Minesweeper:
    def __init__(self, window, width=15, height=12):
        self.nr_bombs = int(width * height / 6)
        self.total_cells = width * height
        self.width = width
        self.height = height

        self.top_window = TopWindow(window, self.nr_bombs)
        self.frame_of_cells = FrameOfCells(window, width, height)
