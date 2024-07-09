from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from games.tic_tac_toe import TicTacToe


class TicTacToeBoard:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback

        self.window = ttk.Frame(root, padding=0)
        self.window.grid(column=0, row=0, sticky=NSEW)
        self.root.title("Tic Tac Toe")
        # self.window = Toplevel(root)
        # self.window.title("Tic Tac Toe")
        self.menu = ttk.Frame(self.window, padding=12)
        self.menu.grid(column=0, row=0, sticky=NSEW)
        self.display = ttk.Frame(self.window, padding=12)
        self.display.grid(column=0, row=1, sticky=NSEW)
        self.board = ttk.Frame(self.window, padding=12)
        self.board.grid(column=0, row=2, sticky=NSEW)
        self.game = TicTacToe()
        self.player = StringVar()
        self.message = StringVar()
        self.layout()
        self.reset()

        self.window.update()
        mw = self.window.winfo_reqwidth()
        mh = self.window.winfo_reqheight()
        vw = root.winfo_screenwidth()
        vh = root.winfo_screenheight()
        x = (vw / 2) - (mw / 2)
        y = (vh / 2) - (mh / 2) - 50
        geometry = f"{int(mw)}x{int(mh)}+{int(x)}+{int(y)}"
        root.geometry(geometry)

    def layout(self):
        ttk.Button(
            self.menu, text="Quit", command=self.end_game, default="active"
        ).grid(column=0, row=0, sticky=W)
        ttk.Button(self.menu, text="Restart", command=self.reset).grid(
            column=1, row=0, sticky=W
        )
        ttk.Label(
            self.board,
            textvariable=self.player,
            font=Font(size=18),
        ).grid(column=0, row=0, columnspan=2, padx=12, pady=10, sticky=W)
        ttk.Label(
            self.board,
            textvariable=self.message,
            font=Font(size=18),
            foreground="red",
        ).grid(column=2, row=0, ipadx=12, pady=10, sticky=E)

    def move(self, x, y, btn):
        def temp():
            try:
                self.game.make_a_move(x, y)
            except (Exception,) as e:
                self.message.set(str(e))
            else:
                btn.config(text=self.game.current_player())
                btn.configure(state="disabled")
                self.game.is_won()
                try:
                    self.game.next_turn()
                except (Exception,) as e:
                    [
                        b.configure(state="disabled")
                        for b in self.board.winfo_children()
                        if isinstance(b, Button)
                    ]
                    self.message.set(str(e))
                    self.player.set(self.game.end())

        return temp

    def reset(self):
        self.game.reset()
        self.player.set(f"Player {self.game.current_player()}'s turn")
        self.message.set("")

        for row, rows in enumerate(self.game.board):
            for col, cols in enumerate(rows):
                btn = Button(
                    self.board,
                    text=" ",
                    font=Font(size=64),
                    width=2,
                    height=1,
                    borderwidth=0,
                    relief="raised",
                    anchor=CENTER,
                    padx=10,
                    pady=10,
                    activebackground="blue",
                    default="normal",
                )
                btn.config(command=self.move(col, row, btn))
                btn.grid(
                    column=col, row=(row + 2), padx=0, pady=0, ipady=10, sticky=NSEW
                )

    def end_game(self):
        self.callback()
        self.window.destroy()
