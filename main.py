from tkinter import *
from tkinter import ttk

from boards.tic_tac_toe import TicTacToeBoard

root = Tk()
root.resizable(FALSE, FALSE)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

menus = ttk.Frame(root)

style = ttk.Style()
style.configure("disabled.TButton", foreground="grey")


def show_menus():
    root.title("Emoji Games")
    menus.grid(column=0, row=0, padx=75, pady=50, sticky=NSEW)
    menus.update()
    mw = menus.winfo_reqwidth() + 150
    mh = menus.winfo_reqheight() + 100
    vw = root.winfo_screenwidth()
    vh = root.winfo_screenheight()
    x = (vw / 2) - (mw / 2)
    y = (vh / 2) - (mh / 2) - 50
    geometry = f"{int(mw)}x{int(mh)}+{int(x)}+{int(y)}"
    root.geometry(geometry)


def tic_tac_toe():
    # menus.grid_remove()
    TicTacToeBoard(root, show_menus)


ttk.Button(menus, text="Tic Tac Toe", command=tic_tac_toe).grid(
    column=0, row=0, sticky=EW
)
ttk.Button(menus, text="Four-in-a-Row", state=DISABLED, style="disabled.TButton").grid(
    column=0, row=1, sticky=EW
)
ttk.Button(menus, text="Exit", command=root.quit, default="active").grid(
    column=0, row=2, sticky=EW
)

# for child in main_menu.winfo_children():
#     child.grid_configure(padx=5, pady=5)


if __name__ == "__main__":
    try:
        show_menus()
        root.mainloop()
    except KeyboardInterrupt:
        pass
