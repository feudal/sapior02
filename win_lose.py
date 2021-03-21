from tkinter import Label, Button


class WinWindow:
    def __init__(self, w, new_game, exit_game):
        w.title('You win')
        l1 = Label(w, text="You win")
        l1.grid(row=0, column=8, pady=10)
        b1 = Button(w, text="New game", width=16, command=new_game)
        b1.grid(row=1, column=0, pady=10)
        b2 = Button(w, text="Exit game", width=16, command=exit_game)
        b2.grid(row=1, column=10, pady=10)


class LoseWindow:
    def __init__(self, w, new_game, exit_game):
        w.title('You lose')
        l1 = Label(w, text="You lose")
        l1.grid(row=0, column=8, pady=10)
        b1 = Button(w, text="New game", width=16, command=new_game)
        b1.grid(row=1, column=0, pady=10)
        b2 = Button(w, text="Exit game", width=16, command=exit_game)
        b2.grid(row=1, column=10, pady=10)
