import random
import time
import sys
from dataclasses import dataclass, field

CROSS = "❌"
NOUGHT = "⭕"


@dataclass
class TicTacToe:
    board: dict = field(default_factory=lambda: {
        i: "  " for i in range(1, 10)})
    numbers_left: list = field(default_factory=list)
    active: bool = True
    rounds: int = 1

    def __post_init__(self):
        self.numbers_left = list(self.board.keys())

    def show_board(self):
        print()
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(f" {self.board[i*3+j+1]} |", end="")
            print()
        print()

    def reset(self):
        self.active = True
        self.board = {i: "  " for i in range(1, 10)}
        self.numbers_left = list(self.board.keys())

    def show_result(self, p1, p2):
        print(
            f"Rounds: {self.rounds}. {p1.name}'s score: {p1.score}. {p2.name}'s score: {p2.score}")


@dataclass
class Player:
    name: str
    symbol: str
    game: TicTacToe
    score: int = 0

    def win(self):
        win_patterns = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]

        if any(all(self.game.board[num] == self.symbol for num in pattern) for pattern in win_patterns):
            print(f"{self.name} wins!")
            self.score += 1
            self.game.active = False


@dataclass
class Human(Player):
    def play(self):
        while self.game.active:
            try:
                cell = int(input(f"{self.symbol}'s turn. Choose 1-9: "))
                if not 1 <= cell <= 9:
                    print("Invalid number")
                elif self.game.board[cell] != "  ":
                    print("Cell already taken")
                else:
                    print(f"{self.symbol} chooses {cell}")
                    self.game.board[cell] = self.symbol
                    self.game.show_board()
                    self.game.numbers_left.remove(cell)
                    self.win()
                    break

            except ValueError:
                print("Invalid entry")


@dataclass
class Computer(Player):
    def play(self):
        cell = random.choice(self.game.numbers_left)
        time.sleep(1)
        print(f"{self.name}({self.symbol}) chooses {cell}")
        self.game.board[cell] = self.symbol
        self.game.show_board()
        self.game.numbers_left.remove(cell)
        self.win()


def pick_symbol():
    while True:
        symbol = input(
            f"Which symbol do you want for Human? 1 = {CROSS}, 2 = {NOUGHT}: ").strip()
        if symbol == "1":
            return CROSS, NOUGHT
        if symbol == "2":
            return NOUGHT, CROSS
        print("Invalid entry")
        
        
def who_first(game):
    human_symbol, computer_symbol = pick_symbol()
    while True:
        print("\nWho should go first?")
        print("1. Human")
        print("2. Computer")
        first = input("Enter 1/2: ").strip()
        if first == "1":
            return Human("Human", human_symbol, game), Computer("Computer", computer_symbol, game)
        if first == "2":
            return Computer("Computer", computer_symbol, game), Human("Human", human_symbol, game)
        print("Invalid entry")


def players(game):
    while True:
        print("\nWho's playing?")
        print("1. Human vs Human ")
        print("2. Human vs Computer")
        print("3. Computer vs Computer")
        player = input("Enter 1/2/3: ").strip()
        if player == "1":
            return Human("Player 1", CROSS, game), Human("Player 2", NOUGHT, game)
        if player == "2":
            return who_first(game)
        if player == "3":
            return Computer("Computer 1", CROSS, game), Computer("Computer 2", NOUGHT, game)
        print("Invalid entry")
        print()


def play_game(p1, p2, game):
    initial_board = "| 1  | 2  | 3  |\n| 4  | 5  | 6  |\n| 7  | 8  | 9  |"
    print()
    print("Let's start!")
    print()
    print(f"{initial_board}\n")
    while game.active:
        p1.play()
        if not game.active:
            break
        if not any(v == "  " for v in game.board.values()):
            print("It's a draw!")
            game.active = False
            break
        p2.play()

    game.show_result(p1, p2)


def again(game):
    while True:
        other = input("Play again? (y/n): ").lower().strip()
        if other == "y":
            game.reset()
            while True:
                player = input("Same players? y/n: ").lower().strip()
                if player == "y":
                    game.rounds += 1
                    print()
                    return True
                if player == "n":
                    game.rounds = 1
                    return False
                print("Invalid entry")
        if other == "n":
            print("See you soon")
            sys.exit()
        print("Invalid entry")


def main():
    print("Welcome!")
    game = TicTacToe()
    while True:
        p1, p2 = players(game)
        while True:
            play_game(p1, p2, game)
            if not again(game):
                break


if __name__ == "__main__":
    main()

