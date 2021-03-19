from tkinter import Label, Button


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