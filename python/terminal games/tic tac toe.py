from os import system
from time import sleep
from random import choice

empty_board = [" " for i in range(0, 9)]

def title_screen(msg, time, space=10):
    system('cls')
    print("_" * 35)
    print("\n" * 7)
    print(" " * space + msg)
    print("\n" * 6)
    print("_" * 35)
    sleep(time)

class Player:
    def __init__(self, name):
        self.name = name
        self.letter = "None"

class Game:
    def __init__(self):
        self.board = list(empty_board)
        self.p1 = Player("P1")
        self.p2 = Player("P2")

        self.active_player = None
        self.game_on = False

    def start(self):
        title_screen("Tic-Tac-Toe", 5)
        self.game_on = True
        self.new_game()

    def draw_game_window(self):
        system('cls')
        print("_" * 35)
        print(f"Turn: {self.active_player.name}")
        print("\n" * 4)
        print(" " * 10 + f" {self.board[6]} | {self.board[7]} | {self.board[8]} " + " " * 10)
        print(" " * 10 + "---+---+---" + " " * 10)
        print(" " * 10 + f" {self.board[3]} | {self.board[4]} | {self.board[5]} " + " " * 10)
        print(" " * 10 + "---+---+---" + " " * 10)
        print(" " * 10 + f" {self.board[0]} | {self.board[1]} | {self.board[2]} " + " " * 10)
        print("\n" * 2)
        print(f"PlayerOne: {self.p1.letter}         PlayerTwo: {self.p2.letter}")
        print(f"    0                    0       ")
        print("_" * 35)
 
    def new_game(self):
        self.board = list(empty_board)
        letters = ["X", "O"]
        self.p1.letter = choice(letters)
        letters.remove(self.p1.letter)
        self.p2.letter = letters[0]

        self.active_player = self.p1
        self.game_on = True

        self.draw_game_window()

        while self.game_on:

            move = self.make_move(self.active_player)
            self.board[move - 1] = self.active_player.letter
            self.draw_game_window()
            win = self.check_win(self.active_player)

            if win is not None:
                self.game_on = False
                title_screen(win, 1)
                self.new_game()
            
            self.switch_player()
            self.draw_game_window()

    def make_move(self, player):
        while True:
            move = input(f"{player.name} Move: \n")
            try:
                move = int(move)

                if move > 9 or move < 0:
                    print("Illegal Move, Out of bounds \n")
                    sleep(1.5)
                    self.draw_game_window()
                    continue

                if self.check_availability(move):
                    return move
                else:
                    print("Illegal Move, position occupied")
                    sleep(1.5)
                    self.draw_game_window()
                    continue
            except:
                print("Illegal Move, Not an integer")
                sleep(1.5)
                self.draw_game_window()
                continue

    def check_availability(self, move):
        return self.board[move - 1] == " "

    def check_win(self, player):
        letter = player.letter

        if " " not in self.board:
            return "Draw"

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[j + 3*i] != letter:
                    break
                if j == 2:
                    return f"{player.name} Wins"

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i + 3*j] != letter:
                    break
                if j == 2:
                    return f"{player.name} Wins"

        for i in range(0, 4, 8):
            if self.board[i] != letter:
                break
            if i == 8:
                return f"{player.name} Wins"

        for i in range(2, 4, 6):
            if self.board[i] != letter:
                break
            if i == 6:
                return f"{player.name} Wins"

        return None

    def switch_player(self):
        if self.active_player == self.p1:
            self.active_player = self.p2
        else:
            self.active_player = self.p1

if __name__ == "__main__":
    game = Game()
    game.start()