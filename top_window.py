from tkinter import Button, Label

from mytimer import Timer


class TopWindow:
    """
    Show the time, number of unfounded bombs, and restart the game
    """

    def __init__(self, window, nr_bombs):
        self.nr_bombs = nr_bombs
        self.t = Timer(window)
        self.t.grid(row=0, column=0)
        self.b1 = Button(window, text='Start', command=self.start)
        self.b1.grid(row=0, column=2, columnspan=2, pady=5)
        self.l2 = Label(window, text=self.nr_bombs)
        self.l2.grid(row=0, column=4)

    def start(self):
        self.t.trigger_timer()

    def minus_bomb(self):
        self.nr_bombs -= 1
        self.l2.config(text=self.nr_bombs)

    def plus_bomb(self):
        self.nr_bombs += 1
        self.l2.config(text=self.nr_bombs)
