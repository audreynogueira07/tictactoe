# We import the necessary tkinter modules.
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # We initialize a new Tkinter window.
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # We initialize the game board as a 3x3 matrix of empty spaces.
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
        # X always goes first.
        self.current_player = 'X'
        
        # We initialize the board buttons.
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text=' ', command=lambda row=i, col=j: self.make_move(row, col), height=3, width=6)
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        # If the cell is already occupied, we do nothing.
        if self.board[row][col] != ' ':
            return

        # We put the current player's piece in the cell and update the corresponding button's text.
        self.board[row][col] = self.current_player
        self.buttons[row][col]['text'] = self.current_player
        self.buttons[row][col]['state'] = 'disabled'

        # If the current player has won the game, we display a message box and close the window.
        if self.check_win():
            messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            self.window.quit()

        # We switch the player.
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        # We check if there's a winning line anywhere on the board.
        for row in self.board:
            if row.count('X') == 3 or row.count('O') == 3:
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def run(self):
        # We start the main loop of the Tkinter window.
        self.window.mainloop()

# We create and start a new game.
game = TicTacToe()
game.run()
