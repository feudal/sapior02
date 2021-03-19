from random import shuffle
from tkinter import Button, Label


class CellField:
    def __init__(self, window, width, height, nr_bombs):
        #  list under cells
        self.list_uc = []
        self.width = width
        self.height = height
        self.nr_bombs = nr_bombs

        #  Create under field
        map_bombs = self.mapbombs()
        map_bombs = self.put_borders(map_bombs)
        map_bombs = self.put_numbers(map_bombs)
        self.list_uc = self.create_under_cell_field(window, map_bombs)
        print(self.list_uc[10].order)
        self.erase_border(self.list_uc)

        #  Create cover for field
        self.list_oc = []
        self.cover_field(window)
        self.erase_border(self.list_oc)

    def mapbombs(self):
        # create a my_list of values like empty() or bomb(*)
        map1 = ["*"] * self.nr_bombs
        map2 = [' '] * int(self.width * self.height - self.nr_bombs)
        m = map1 + map2
        # shake the list map
        shuffle(m)

        return m

    def put_borders(self, map):
        m = map.copy()
        new_m = []
        for i in range(self.height):
            new_m.append(m[0:self.width])
            del m[0:self.width]

        for i in new_m:
            i.append('-')
            i.insert(0, '-')

        border = ['-'] * (self.width + 2)
        new_m.append(border)
        new_m.insert(0, border)

        for i in new_m:
            for j in i:
                m.append(j)

        return m

    def put_numbers(self, map):
        m = map.copy()
        for i in range(len(m)):
            m[i] = self.count_bombs(m, i)

        return m

    def count_bombs(self, m, i):
        if m[i] == '-':
            return '-'
        if m[i] == '*':
            return '*'

        nr_bombs = 0

        if m[i - self.width - 3] == '*':
            nr_bombs += 1
        if m[i - self.width - 2] == '*':
            nr_bombs += 1
        if m[i - self.width - 1] == '*':
            nr_bombs += 1

        if m[i + 1] == '*':
            nr_bombs += 1
        if m[i - 1] == '*':
            nr_bombs += 1

        if m[i + self.width + 1] == '*':
            nr_bombs += 1
        if m[i + self.width + 2] == '*':
            nr_bombs += 1
        if m[i + self.width + 3] == '*':
            nr_bombs += 1
        if nr_bombs != 0:
            return str(nr_bombs)
        else:
            return ''

    def create_under_cell_field(self, window, map_bombs):
        give_color = {
            "*": 'black',
            '1': 'blue',
            '2': 'green',
            '3': 'red',
            '4': 'brown',
            '5': 'brown',
            '6': 'brown',
            '-': 'brown',
            '': 'brown'
        }
        ucf = []  # ucf under_cell_field the list of under_cells
        for i in range((self.width + 2) * (self.height + 2)):
            ucf.append(UnderCell(window, text=map_bombs[i], order=i + 1, ucell_color=give_color[map_bombs[i]],
                                 ucell_bg_color='white'))

        # Arrange the under_cells in the field
        ucf_copy = ucf.copy()
        for i in range(self.height + 2):
            for j in range(self.width + 2):
                ucf_copy[0].mygrid(i + 1, j)
                ucf_copy.pop(0)

        return ucf

    def erase_border(self, l_under_cells):
        for i in range(0, (self.width+2)*(self.height+2), self.width + 2):
            l_under_cells[i].erase()
        for i in range(self.width+1, (self.width+1)*(self.height+3), self.width + 2):
            l_under_cells[i].erase()
        for i in range(0, self.width+1):
            l_under_cells[i].erase()
        l_under_cells.reverse()
        for i in range(0, self.width+1):
            l_under_cells[i].erase()

    def cover_field(self, window):
        for i in range((self.width + 2) * (self.height + 2)):
            self.list_oc.append(OverCell(window, text=i + 1, order=i + 1, ocell_color='black',
                                         ocell_bg_color='white'))

        ocf_copy = self.list_oc.copy()
        for i in range(self.height + 2):
            for j in range(self.width + 2):
                ocf_copy[0].mygrid(i + 1, j)
                ocf_copy.pop(0)


class OverCell:
    def __init__(self, window, text=0, order=0, ocell_color='grey95', ocell_bg_color='grey95',
                 command=open):
        self.order = order
        self.text = text
        self.b1 = Button(window, text=text, bg=ocell_bg_color, fg=ocell_color, width=3, command=self.open)

    def mygrid(self, row, column):
        self.b1.grid(row=row, column=column)

    def erase(self):
        self.b1.grid_forget()

    def get_order(self):
        return self.order

    def open(self):
        self.b1.grid_forget()
    #     my_list = CellField.list_uc.copy()
    #     print('mylist =', CellField.list_uc)
    #     self.b1.grid_forget()
    #     print(self.get_order())
    #
    #     if my_list[self.get_order()] == '*':
    #         print('explode')
    #         self.explode()
    #
    # def explode(self):
    #     my_list = CellField.list_uc.copy()
    #     my_list2 = OverCellField.list_oc.copy()
    #     for i in my_list:
    #         print('i =', i)
    #         if i.cget('text') == '*':
    #             my_list2[i].open()


class UnderCell:
    def __init__(self, window, text='', order=0, ucell_color='grey95', ucell_bg_color='grey95'):
        self.order = order
        self.text = text

        self.l1 = Label(window, text=text, bg=ucell_bg_color, fg=ucell_color, width=3)

    def mygrid(self, row, column):
        self.l1.grid(row=row, column=column)

    def erase(self):
        self.l1.grid_forget()

    def get_order(self):
        return self.order