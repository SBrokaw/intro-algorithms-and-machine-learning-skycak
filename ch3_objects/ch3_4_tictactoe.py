# Skycak, J. (2021). Tic-Tac-Toe and Connect Four. In Introduction to
# Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/tic-tac-toe-and-connect-four/
from random import random as rand

class Game:
    def __init__(self, player1, player2):
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

        # self.print_board()

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
                # print(f"  win! {line} a:{a} b:{b} c:{c}")
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

        # print(f"  history:", self.move_history, move, r, c)
        # self.print_board()
        return 0

    def run( self, is_logging ):
        while self.is_playing:
            board_copy = [row[:] for row in self.board]
            self.take_turn(player1, player1.choose_move(board_copy), is_logging)
            if self.is_gameover: break
            board_copy = [row[:] for row in self.board]
            self.take_turn(player2, player2.choose_move(board_copy), is_logging)
            if self.is_gameover: break

        if is_logging:
            self.print_board()
            print(f" Game Over —— {self.winner} Wins! ".center(40, '—'))
            print(f"".center(40, '‾'))

        return self.winner


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


class Player:
    def __init__( self, strategy_func ):
        self.piece = ''
        self.strategy_func = strategy_func
    
    def choose_move( self, board ):
        return self.strategy_func( board, self.piece )

def print_board( board ):
    print(f"3  {board[0][0]} | {board[0][1]} | {board[0][2]}") 
    print("  ———+———+———")
    print(f"2  {board[1][0]} | {board[1][1]} | {board[1][2]}")  
    print("  ———+———+———")
    print(f"1  {board[2][0]} | {board[2][1]} | {board[2][2]}")  
    print("   A   B   C")

def possible_moves( board ):
    col_ids = ['A', 'B', 'C']
    row_ids = ['3', '2', '1']
    valid_indices = []
    for row_id, row in zip(row_ids, board):
        for col_id, cell in zip(col_ids, row):
            if cell == ' ': valid_indices += [f"{col_id}{row_id}"]

    # print(f"  valid_moves:{valid_indices}")
    return valid_indices

def random_moves_strat( board, piece ):
    valid_moves = possible_moves(board)
    random_idx = int(rand() * len(valid_moves))
    # print(f"  valid_moves[{random_idx}] {valid_moves}")
    return valid_moves[random_idx]

def manual_moves_strat( board, piece ):
    print_board(board)
    valid_moves = possible_moves(board)
    print(f"  Valid Moves: {valid_moves}")
    move = input(f"  Input Move eg. \"{valid_moves[int(rand() * len(valid_moves))]}\" -->")
    # input validation
    if len(move) < 2: 
        return 0
    move = move.strip().upper()[0:2]
    print(f"  human move:{move}")
    return move

def cheater_strat( board, piece ):
    board = [['O' for _ in range(3)] for _ in range(3)]
    return "A1"

def possible_corners( board ):
    corners = ["A1", "A3", "C1", "C3"]
    return [corner for corner in possible_moves(board) if corner in corners]

def parse_indices( indices ):
    r = int(indices[0])
    c = int(indices[1])
    col_ids = ['A', 'B', 'C']
    row_ids = ['3', '2', '1']
    return f"{col_ids[c]}{row_ids[r]}"

def custom_strat( board, piece ):
    win_lines = [   [(0,0), (0,1), (0,2)],
                    [(1,0), (1,1), (1,2)],
                    [(2,0), (2,1), (2,2)],
                    [(0,0), (1,0), (2,0)],
                    [(0,1), (1,1), (2,1)],
                    [(0,2), (1,2), (2,2)],
                    [(0,0), (1,1), (2,2)],
                    [(0,2), (1,1), (2,0)]]
    # check win lines for two-in-a-rows
    for line in win_lines:
        a, b, c = (board[r][c] for r, c in line)
        vals = [a, b, c]
        if vals.count(piece) == 2 and vals.count(' ') == 1:
            # winner found! return the empty cell
            move = [[r, c] for r, c, in line if board[r][c] == ' ']
            grid_location = parse_indices(move[0])
            return grid_location
    # fill corners
    valid_moves = possible_corners(board)
    if valid_moves: 
        return valid_moves[int(rand() * len(valid_moves))]

    # then pick random squares
    valid_moves = possible_moves(board)
    if valid_moves: 
        return valid_moves[int(rand() * len(valid_moves))]

    return "Z0"

def custom_strat2( board, piece ):
    win_lines = [   [(0,0), (0,1), (0,2)],
                    [(1,0), (1,1), (1,2)],
                    [(2,0), (2,1), (2,2)],
                    [(0,0), (1,0), (2,0)],
                    [(0,1), (1,1), (2,1)],
                    [(0,2), (1,2), (2,2)],
                    [(0,0), (1,1), (2,2)],
                    [(0,2), (1,1), (2,0)]]
    # check win lines for two-in-a-rows
    for line in win_lines:
        a, b, c = (board[r][c] for r, c in line)
        vals = [a, b, c]
        if vals.count(piece) == 2 and vals.count(' ') == 1:
            # winner found! return the empty cell
            move = [[r, c] for r, c, in line if board[r][c] == ' ']
            grid_location = parse_indices(move[0])
            return grid_location

    # then pick random squares
    valid_moves = possible_moves(board)
    if valid_moves: 
        return valid_moves[int(rand() * len(valid_moves))]

    return "Z0"

strategies = [random_moves_strat, custom_strat, custom_strat2]
strat_combos = [[p1, p2] for p1 in strategies for p2 in strategies]

table_width = 80
col_width = int(table_width / 8)
strat_width = 20
print(f"X wins".center(col_width) + 
      f"O wins".center(col_width) + 
      f"Total Wins".center(col_width) + 
      f"X wr".center(col_width) + 
      f"O wr".center(col_width) + 
      f"N".center(col_width) + 
      f"X strat".ljust(strat_width) + 
      f"O strat")
print("".center(table_width + strat_width, '‾'))
stats = []

for combo in strat_combos:
    N = 100
    x_wins = 0
    o_wins = 0
    for n in range(N):
        player1 = Player(combo[0])
        player2 = Player(combo[1])
        game = Game(player1, player2)
        winner = game.run(False)
        if winner == 'X':
            x_wins += 1
        elif winner == 'O':
            o_wins += 1

    total_wins = x_wins + o_wins
    stats += [f"{x_wins}".center(col_width) +
              f"{o_wins}".center(col_width) + 
              f"{total_wins}".center(col_width) + 
              f"{x_wins/(total_wins):.3f}".center(col_width) +
              f"{o_wins/(total_wins):.3f}".center(col_width) + 
              f"{N}".center(col_width) +
              f"{combo[0].__name__}".ljust(strat_width) + 
              f"{combo[1].__name__}"]

for s in stats: print(s)
