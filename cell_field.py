import os
from random import shuffle
from tkinter import Button, Label, Toplevel
from win_lose import WinWindow, LoseWindow


class CellField:
    def __init__(self, window, width, height, nr_bombs, top_w):
        self.top_wind = top_w
        #  list under cells
        self.list_uc = []
        self.width = width
        self.height = height
        self.nr_bombs = nr_bombs
        global nr_cells_need_to_open
        nr_cells_need_to_open = width * height - int(width * height / 6)

        #  Create under field
        map_bombs = self.mapbombs()
        map_bombs = self.put_borders(map_bombs)
        map_bombs = self.put_numbers(map_bombs)
        self.list_uc = self.create_under_cell_field(window, map_bombs)
        self.erase_border(self.list_uc)

        #  Create cover for field
        self.list_oc = []
        self.cover_field(window)
        self.erase_border(self.list_oc)

        # all over cells will now about the list of all cells in the field and width of field
        for i in range(len(self.list_oc)):
            self.list_oc[i].get_info(list_ocf=self.list_oc, list_ucf=self.list_uc, width_f=self.width,
                                     top_w=self.top_wind)

    def mapbombs(self):
        # create a my_list of values like empty() or bomb(*)
        map1 = ["*"] * self.nr_bombs
        map2 = [' '] * int(self.width * self.height - self.nr_bombs)
        m = map1 + map2
        # shake the list map
        shuffle(m)

        return m

    def put_borders(self, my_map):
        m = my_map.copy()
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

        for i in new_m:
            print(i)

        return m

    def put_numbers(self, my_map):
        m = my_map.copy()
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
            '7': 'brown',
            '8': 'brown',
            '-': 'brown',
            '': 'brown'
        }
        ucf = []  # ucf under_cell_field the list of under_cells
        for i in range((self.width + 2) * (self.height + 2)):
            ucf.append(UnderCell(window, text=map_bombs[i], order=i, ucell_color=give_color[map_bombs[i]],
                                 ucell_bg_color='white'))

        # Arrange the under_cells in the field
        ucf_copy = ucf.copy()
        for i in range(self.height + 2):
            for j in range(self.width + 2):
                ucf_copy[0].mygrid(i + 1, j)
                ucf_copy.pop(0)

        return ucf

    def erase_border(self, l_under_cells):
        for i in range(0, (self.width + 2) * (self.height + 2), self.width + 2):
            l_under_cells[i].erase()
        for i in range(self.width + 1, (self.width + 1) * (self.height + 3), self.width + 2):
            l_under_cells[i].erase()
        for i in range(0, self.width + 1):
            l_under_cells[i].erase()
        l_under_cells.reverse()
        for i in range(0, self.width + 1):
            l_under_cells[i].erase()
        l_under_cells.reverse()

    def cover_field(self, window):
        for i in range((self.width + 2) * (self.height + 2)):
            btn = OverCell(window, text=i, order=i, ocell_bg_color='white')
            self.list_oc.append(btn)

        ocf_copy = self.list_oc.copy()
        for i in range(self.height + 2):
            for j in range(self.width + 2):
                ocf_copy[0].mygrid(i + 1, j)
                ocf_copy.pop(0)


class OverCell:
    def __init__(self, window, text=0, order=0, ocell_color='grey99', ocell_bg_color='grey95',
                 command=open):
        self.w = window
        self.top_wind = None
        self.width_field = None
        self.height_field = None
        self.list_uc = None
        self.list_oc = None
        self.is_open = False
        self.is_mark = False
        self.order = order
        self.text = text
        self.b1 = Button(window, text=text, bg=ocell_bg_color, fg=ocell_color, width=3, command=self.open)
        self.b1.bind("<Button-3>", lambda e, i=self.order: self.mark_cell(e, i))

    def get_info(self, list_ocf, list_ucf, width_f, top_w):
        self.list_uc = list_ucf
        self.list_oc = list_ocf
        self.width_field = width_f
        self.top_wind = top_w

    def erase(self):
        self.b1.grid_forget()

    def mygrid(self, row, column):
        self.b1.grid(row=row, column=column)

    def get_order(self):
        return self.order

    def open(self):
        if not self.top_wind.is_started:
            self.top_wind.is_started = True
            self.top_wind.start()

        self.is_open = True
        global nr_cells_need_to_open
        nr_cells_need_to_open -= 1
        self.b1.grid_forget()
        if nr_cells_need_to_open == 0:
            print('you win')
            top_w = Toplevel(self.w)
            win_window = WinWindow(top_w, self.restart_game, self.exit)

        if self.list_uc[self.order].text == '':
            self.open_around(self.order)
        if self.list_uc[self.order].text == '*':
            self.explode()
            print('you lose')
            top_w = Toplevel(self.w)
            lose_window = LoseWindow(top_w, self.restart_game, self.exit)

    def exit(self):
        print('exit')
        self.w.destroy()

    def restart_game(self, window):
        print('restart game')
        self.w.destroy()
        os.startfile("main.pyw")

    def open_around(self, order):
        if self.check_cell(order - self.width_field - 3):
            self.list_oc[order - self.width_field - 3].open()
        if self.check_cell(order - self.width_field - 2):
            self.list_oc[order - self.width_field - 2].open()
        if self.check_cell(order - self.width_field - 1):
            self.list_oc[order - self.width_field - 1].open()

        if self.check_cell(order - 1):
            self.list_oc[order - 1].open()
        if self.check_cell(order + 1):
            self.list_oc[order + 1].open()

        if self.check_cell(order + self.width_field + 3):
            self.list_oc[order + self.width_field + 3].open()
        if self.check_cell(order + self.width_field + 2):
            self.list_oc[order + self.width_field + 2].open()
        if self.check_cell(order + self.width_field + 1):
            self.list_oc[order + self.width_field + 1].open()

    def check_cell(self, order):
        if self.list_uc[order].text not in ('*', '-') and not self.list_oc[order].is_open:
            return True
        return False

    def explode(self):
        self.top_wind.start()
        for i in self.list_uc:
            if i.text == '*':
                self.list_oc[i.order].b1.grid_forget()
                self.list_uc[i.order].l1.config(bg='red')

    def mark_cell(self, event, order):
        if not self.list_oc[order].is_mark:
            self.list_oc[order].b1.config(text="X", fg='black')
            self.is_mark = True
            self.top_wind.minus_bomb()
        else:
            self.list_oc[order].b1.config(text=order)
            self.is_mark = False
            self.top_wind.plus_bomb()


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
