# Skycak, J. (2021). Tic-Tac-Toe and Connect Four. In Introduction to
# Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/tic-tac-toe-and-connect-four/
from random import random as rand

class Game:
    def __init__(self, player1, player2):
        print(" Tic-Tac-Toe! ".center(40, '='))
        self.board = [[' '] * 3] * 3
        self.move_history = [] # array of moves for this game (ex. ["X0A", "O1A", "X1B", "O0B", "X3C"])
        player1.piece = 'X'
        player2.piece = 'O'

        self.is_playing = True
        self.print_board()

    def print_board(self):
        print("   A   B   C")
        print(f"1  {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}  Move History:{self.move_history}") 
        print("  ———+———+———")
        print(f"2  {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}")  
        print("  ———+———+———")
        print(f"3  {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")  

    def is_valid_move( self, m ):
        return True if m in self.valid_moves else False

    @property
    def valid_moves(self):
        col_ids = ['A', 'B', 'C']
        row_ids = ['1', '2', '3']
        valid_indices = []
        for i, r in zip(row_ids, self.board):
            for j, cell in zip(col_ids, r):
                if cell == ' ': valid_indices += [f"{i}{j}"]

        return valid_indices




class RandomPlayer:
    def __init__( self ):
        self.piece = ''

    def choose_move( self, game ):
        valid_moves = game.valid_moves
        return valid_moves[int(rand() * len(valid_moves))]

    
player1 = RandomPlayer()
player2 = RandomPlayer()
game = Game(player1, player2)
print( game.valid_moves )

while game.is_playing:
    print(player1.choose_move( game))

    game.is_playing = False