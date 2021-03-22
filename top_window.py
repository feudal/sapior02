import os
from datetime import datetime
from tkinter import Button, Label


class TopWindow:
    """
    Show the time, number of unfounded bombs, and restart the game
    """

    def __init__(self, window, nr_bombs):
        self.w = window
        self.temp = 0
        self.is_started = False
        self.nr_bombs = nr_bombs
        self.l1 = Label(window, text='00:00')
        self.l1.grid(row=0, column=2)
        self.b1 = Button(window, text='Restart', command=self.restart)
        self.b1.grid(row=0, column=4, columnspan=2, pady=5)
        self.l2 = Label(window, text=self.nr_bombs)
        self.l2.grid(row=0, column=7)

    def start(self):
        self.temp += 1
        stopwatch_time = datetime.utcfromtimestamp(self.temp).strftime('%M:%S')
        self.l1.config(text=stopwatch_time)
        self.l1.after(1000, self.start)

    def restart(self):
        self.w.destroy()
        os.startfile("main.pyw")

    def minus_bomb(self):
        self.nr_bombs -= 1
        self.l2.config(text=self.nr_bombs)

    def plus_bomb(self):
        self.nr_bombs += 1
        self.l2.config(text=self.nr_bombs)
