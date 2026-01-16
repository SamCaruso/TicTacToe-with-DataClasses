import random
import time
import sys
from dataclasses import dataclass
from typing import ClassVar

CROSS = "❌"
NOUGHT = "⭕"


@dataclass
class Game:
    board: ClassVar[dict] = {i: "  " for i in range(1, 10)}
    numbers_left: ClassVar[list] = list(board.keys())
    active: ClassVar[bool] = True
    rounds: ClassVar[int] = 1

    @staticmethod
    def show_board():
        print()
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(f" {Game.board[i*3+j+1]} |", end="")
            print()
        print()

    @staticmethod
    def reset():
        Game.active = True
        Game.board = {i: "  " for i in range(1, 10)}
        Game.numbers_left = list(Game.board.keys())

    @staticmethod
    def show_result(p1, p2):
        print(
            f"Rounds: {Game.rounds}. {p1.name}'s score: {p1.score}. {p2.name}'s score: {p2.score}")


@dataclass
class Player:
    name: str
    symbol: str
    score: int = 0

    def win(self):
        win_patterns = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]

        if any(all(Game.board[num] == self.symbol for num in pattern) for pattern in win_patterns):
            print(f"{self.name} wins!")
            self.score += 1
            Game.active = False


@dataclass
class Human(Player):
    def play(self):
        while Game.active:
            try:
                cell = int(input(f"{self.symbol}'s turn. Choose 1-9: "))
                if not 1 <= cell <= 9:
                    print("Invalid number")
                elif Game.board[cell] != "  ":
                    print("Cell already taken")
                else:
                    print(f"{self.symbol} chooses {cell}")
                    Game.board[cell] = self.symbol
                    Game.show_board()
                    Game.numbers_left.remove(cell)
                    self.win()
                    break

            except ValueError:
                print("Invalid entry")


@dataclass
class Computer(Player):
    def play(self):
        cell = random.choice(Game.numbers_left)
        time.sleep(1)
        print(f"{self.name}({self.symbol}) chooses {cell}")
        Game.board[cell] = self.symbol
        Game.show_board()
        Game.numbers_left.remove(cell)
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
        
        
def who_first():
    human_symbol, computer_symbol = pick_symbol()
    while True:
        print("\nWho should go first?")
        print("1. Human")
        print("2. Computer")
        first = input("Enter 1/2: ").strip()
        if first == "1":
            return Human("Human", human_symbol), Computer("Computer", computer_symbol)
        if first == "2":
            return Computer("Computer", computer_symbol), Human("Human", human_symbol)
        print("Invalid entry")


def players():
    while True:
        print("\nWho's playing?")
        print("1. Human vs Human ")
        print("2. Human vs Computer")
        print("3. Computer vs Computer")
        player = input("Enter 1/2/3: ").strip()
        if player == "1":
            return Human("Player 1", CROSS), Human("Player 2", NOUGHT)
        if player == "2":
            return who_first()
        if player == "3":
            return Computer("Computer 1", CROSS), Computer("Computer 2", NOUGHT)
        print("Invalid entry")
        print()


def play_game(p1, p2):
    initial_board = "| 1  | 2  | 3  |\n| 4  | 5  | 6  |\n| 7  | 8  | 9  |"
    print()
    print("Let's start!")
    print()
    print(f"{initial_board}\n")
    while Game.active:
        p1.play()
        if not Game.active:
            break
        if not any(v == "  " for v in Game.board.values()):
            print("It's a draw!")
            Game.active = False
            break
        p2.play()

    Game.show_result(p1, p2)


def again():
    while True:
        other = input("Play again? (y/n): ").lower().strip()
        if other == "y":
            Game.reset()
            while True:
                player = input("Same players? y/n: ").lower().strip()
                if player == "y":
                    Game.rounds += 1
                    print()
                    return True
                if player == "n":
                    Game.rounds = 1
                    return False
                print("Invalid entry")
        if other == "n":
            print("See you soon")
            sys.exit()
        print("Invalid entry")


def main():
    print("Welcome!")
    while True:
        p1, p2 = players()
        while True:
            play_game(p1, p2)
            if not again():
                break


if __name__ == "__main__":
    main()
