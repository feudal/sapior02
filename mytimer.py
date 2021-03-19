import datetime
from tkinter import Label


class Timer:
    """
    Timer is a class that have label where is displayed a timer. You can start and stop them.
    """

    def __init__(self, window):
        self.temp = 0
        self.is_triggered = False
        self.is_running = False

        self.l1 = Label(window, text="00:00")

    def grid(self, row, column):
        self.l1.grid(row=row, column=column, columnspan=2)

    def trigger_timer(self):
        # is_triggered instance is used right switching between function start_timer and stop_timer
        # is_running instance is used to know if is running the timer or not
        # we don't trigger the timer if it is running and function start_timer is called
        # we don't trigger the timer if it isn't running and function stop_timer is called
        if not self.is_running:
            if not self.is_triggered:
                self.is_triggered = not self.is_triggered
                self.is_running = True
                self.star_timer()
        else:
            self.stop_timer()
            self.is_triggered = not self.is_triggered

    def star_timer(self):
        if self.is_running:
            self.temp += 1
            stopwatch_time = datetime.datetime.utcfromtimestamp(self.temp).strftime('%M:%S')
            self.l1.config(text=stopwatch_time)
            self.l1.after(1000, self.star_timer)

    def stop_timer(self):
        self.temp = 0
        self.l1.config(text='00:00')
        self.is_running = False
