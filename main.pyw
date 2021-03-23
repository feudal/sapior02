from tkinter import Tk
from cell_field import CellField
from top_window import TopWindow


class Minesweeper:
    def __init__(self, window, width=20, height=15):  # width=15, height=12):
        self.nr_bombs = int(width * height / 6)
        self.total_cells = width * height
        self.width = width
        self.height = height

        self.top_window = TopWindow(window, self.nr_bombs)
        self.cells_field = CellField(window, width, height, self.nr_bombs, self.top_window)


window = Tk()
window.title('Sapior')
window.eval('tk::PlaceWindow . center')

m = Minesweeper(window)

window.mainloop()
