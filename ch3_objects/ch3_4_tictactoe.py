# Skycak, J. (2021). Tic-Tac-Toe and Connect Four. In Introduction to
# Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/tic-tac-toe-and-connect-four/
from random import random as rand

class Game:
    def __init__(self, player1, player2):
        print(" Tic-Tac-Toe! ".center(40, '='))
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.move_history = [] # array of moves for this game (ex. ["XA0", "OA1", "XB1", "OB0", "XC3"])
        self.winner = "No player"
        player1.piece = 'X'
        player2.piece = 'O'
        self.WIN_LINES = [  [(0,0), (0,1), (0,2)],
                            [(1,0), (1,1), (1,2)],
                            [(2,0), (2,1), (2,2)],
                            [(0,0), (1,0), (2,0)],
                            [(0,1), (1,1), (2,1)],
                            [(0,2), (1,2), (2,2)],
                            [(0,0), (1,1), (2,2)],
                            [(0,2), (1,1), (2,0)]]

        self.print_board()

    def print_board(self):
        print(f"3  {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}  Move History:{self.move_history}") 
        print("  ———+———+———")
        print(f"2  {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}")  
        print("  ———+———+———")
        print(f"1  {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")  
        print("   A   B   C")

    def is_valid_move( self, m ):
        return True if m in self.valid_moves else False

    @property
    def valid_moves(self):
        col_ids = ['A', 'B', 'C']
        row_ids = ['3', '2', '1']
        valid_indices = []
        for row_id, row in zip(row_ids, self.board):
            for col_id, cell in zip(col_ids, row):
                if cell == ' ': valid_indices += [f"{col_id}{row_id}"]

        # print(f"  valid_moves:{valid_indices}")
        return valid_indices

    @property
    def is_playing(self):
        # check if no more valid moves
        if len(self.valid_moves) == 0: 
            self.winner = "Nobody"
            return False

        # check all 8 combinations to see if there is any 3-in-a-row
        for line in self.WIN_LINES:
            a, b, c = (self.board[r][c] for r, c in line)
            if (a == b == c) and a != ' ': 
                print(f"  win! {line} a:{a} b:{b} c:{c}")
                self.winner = a
                return False # win line found!

        return True # no match. return True

    @property
    def is_gameover(self):
        return not self.is_playing

    def parse_move( self, move ):
        if not self.is_valid_move(move): return -1, -1
        c = ord(move[0].lower()) - 97
        r = -1 * int(move[1]) + 3
        return r, c

    def take_turn( self, player, move, is_logging ):
        if not self.is_valid_move( move ): return -1
        r, c = self.parse_move( move )
        self.board[r][c] = player.piece

        if is_logging: self.move_history += [f"{player.piece}{move}"]

        print(f"  history:", self.move_history, move, r, c)
        # self.print_board()
        return 0

    def run( self, is_logging ):
        while self.is_playing:
            self.take_turn(player1, player1.choose_move(self), is_logging)
            if self.is_gameover: break
            self.take_turn(player2, player2.choose_move(self), is_logging)
            if self.is_gameover: break

        self.print_board()
        print(f" Game Over —— {self.winner} Wins! ".center(40, '—'))
        return 0


class RandomPlayer:
    def __init__( self ):
        self.piece = ''

    def choose_move( self, game ):
        valid_moves = game.valid_moves
        random_idx = int(rand() * len(valid_moves))
        # print(f"  valid_moves[{random_idx}] {valid_moves}")
        return valid_moves[random_idx]


class ManualPlayer:
    def __init__( self ):
        self.piece = ''

    def choose_move( self, game ):
        game.print_board()
        valid_moves = game.valid_moves
        print(f"  Valid Moves: {valid_moves}")
        move = input(f"  Input Move eg. \"{valid_moves[int(rand() * len(valid_moves))]}\" -->")
        # input validation
        if len(move) < 2: 
            return 0
        move = move.strip().upper()[0:2]
        print(f"  human move:{move}")
        return move

    
# NPC vs. NPC
player1 = RandomPlayer()
player2 = RandomPlayer()
game = Game(player1, player2)
game.run(True)

# Player1 Human vs. NPC
player1 = ManualPlayer()
player2 = RandomPlayer()
game = Game(player1, player2)
game.run(True)

# NPC vs. Player2 Human
player1 = RandomPlayer()
player2 = ManualPlayer()
game = Game(player1, player2)
game.run(True)
