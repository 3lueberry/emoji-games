import os
import time
from random import shuffle


class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.players = ["o", "x"] if __name__ == "__main__" else ["🙆‍♀️", "🙅‍♂️"]
        shuffle(self.players)
        self.moves = 9
        self.turn = 0
        self.gameover = False

    def reset(self):
        self.__init__()

    def __repr__(self):
        return self.board

    def __str__(self):
        result = " "
        for row, cols in enumerate(self.board):
            result += " | ".join(cols)
            result += "\n___________\n " if row < len(self.board) - 1 else "\n"
        return result

    def current_turn(self):
        return self.turn + 1

    def current_player(self):
        return self.players[self.turn]

    def next_turn(self):
        if not self.gameover:
            self.moves -= 1
            if self.moves > 0:
                self.turn = (self.moves + 1) % 2
                return
        raise Exception("Game Over!")

    def make_a_move(self, x, y):
        if self.board[x][y] != " ":
            raise Exception("Invalid Move!")
        self.board[x][y] = self.current_player()

    @staticmethod
    def prompt(qns):
        user = ""
        while not user.isdigit() or not (0 < int(user) < 4):
            user = input(f"Select {qns}: ")
        return int(user)

    def is_won(self):
        ([one, two, thr], [fou, fiv, six], [sev, eig, nin]) = self.board
        self.gameover = (
            True
            if one == two == thr != " "
            or fou == fiv == six != " "
            or sev == eig == nin != " "
            or one == fou == sev != " "
            or two == fiv == eig != " "
            or thr == six == nin != " "
            or one == fiv == nin != " "
            or thr == fiv == sev != " "
            else False
        )
        return self.gameover

    def play(self):
        print(f'Player "{self.current_player().upper()}": make your move.')
        while True:
            x = self.prompt("row") - 1
            y = self.prompt("col") - 1
            try:
                self.make_a_move(x, y)
            except (Exception,) as e:
                continue
            else:
                os.system("clear")
                print(self)
                break

    def end(self):
        result = (
            f"Player {self.current_player().upper()} WIN!"
            if self.is_won()
            else "It's a tie!"
        )
        print(result)
        return result

    def start(self):
        self.reset()
        os.system("clear")
        print(self)
        time.sleep(0.5)

        while True:
            self.play()
            self.is_won()
            try:
                self.next_turn()
            except (Exception,) as e:
                self.end()
                break
            else:
                time.sleep(0.5)


def main():
    again = "Y"
    game = TicTacToe()
    while again == "Y":
        again = ""
        game.start()
        time.sleep(0.5)
        while (again != "Y") and (again != "N"):
            again = input(f"Do you want to play again? (Y/N): ").capitalize()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
