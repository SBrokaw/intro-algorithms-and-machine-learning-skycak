# Skycak, J. (2021). Tic-Tac-Toe and Connect Four. In Introduction to
# Algorithms and Machine Learning: from Sorting to Strategic Agents. 
# https://justinmath.com/tic-tac-toe-and-connect-four/
from random import random as rand

class Game:
    def __init__(self, player1, player2):
        self.board = [['∙' for _ in range(7)] for _ in range(6)]
        self.move_history = [] # array of moves for this game (ex. ["XA0", "OA1", "XB1", "OB0", "XC3"])
        self.winner = "Nobody"
        player1.piece = 'X'
        player2.piece = 'O'
        self.WIN_DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    def print_board(self):
        for r_idx, row in enumerate(self.board):
            print(f"{len(self.board) - r_idx} |", end='')
            for cell in row:
                print(f"{cell} ", end='')
            print()
        print("   ‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print(f"   A B C D E F G")

    def board_col( self, c ):
        return [r[c] for r in self.board]

    def board_diag( self, r, c, m ):
        diag = [self.board[r][c]]
        dirs = [(1, m * -1), (-1, m * 1)]
        for dir_c, dir_r in dirs:
            for k in range(1, 7):
                cc = c + dir_c * k
                rr = r + dir_r * k
                if cc >= len(self.board[0]) or cc < 0 or rr >= len(self.board) or rr < 0:
                    break
                if dir_c > 0:
                    diag += [self.board[rr][cc]]
                elif dir_c < 0:
                    diag = [self.board[rr][cc]] + diag

        return diag

    def is_valid_move( self, m ):
        return True if m in self.valid_moves else False

    @property
    def valid_moves(self):
        col_ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        valid_indices = []
        for col_id, cell in zip(col_ids, self.board[0]):
            if cell == '∙': valid_indices += [f"{col_id}"]

        # print(f"  valid_moves:{valid_indices}")
        return valid_indices

    def count_consecutive(self, piece, row):
        count = 0
        num_in_a_row = 0
        for r in row:
            num_in_a_row = max(count, num_in_a_row)
            if r == piece: count += 1
            else: count = 0

        return num_in_a_row

    def check_win_from(self, r, c):
        piece = self.board[r][c]
        if piece == '∙': 
            return False
        check_row = self.board[r]
        check_col = self.board_col(c)
        check_diag1 = self.board_diag(r, c, 1)
        check_diag2 = self.board_diag(r, c, -1)
        checks = [check_row, check_col, check_diag1, check_diag2]
        # print(f"  check_win:{piece} [{r},{c}]")
        for check in checks:
            num_in_a_row = self.count_consecutive(piece, check)
            # print(f"    {check} ".ljust(50) + f"{num_in_a_row}", end='')
            if num_in_a_row == 4:
                self.winner = piece
                # print(f" WINNER! {piece}")
                return self.winner
            # print()
        
        return self.winner


    @property
    def is_playing(self):
        # check if no more valid moves
        if len(self.valid_moves) == 0: 
            self.winner = "Nobody"
            return False

        if self.winner == "Nobody":
            return True
        else:
            return False

    @property
    def is_gameover(self):
        return not self.is_playing

    def parse_move( self, move ):
        if not self.is_valid_move(move): return -1
        c = ord(move[0].lower()) - 97
        return c

    def take_turn( self, player, move, is_logging ):
        if not self.is_valid_move( move ): return -1
        c = self.parse_move( move )
        col = self.board_col(c)
        r = col.count('∙') - 1
        self.board[r][c] = player.piece

        if is_logging: 
            self.move_history += [f"{player.piece}{move}"]

        self.winner = self.check_win_from(r, c)

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



class Player:
    def __init__( self, strategy_func ):
        self.piece = ''
        self.strategy_func = strategy_func
    
    def choose_move( self, board ):
        return self.strategy_func( board, self.piece )

def print_board( board ):
    for r_idx, row in enumerate(board):
        print(f"{len(board) - r_idx} |", end='')
        for cell in row:
            print(f"{cell} ", end='')
        print()
    print("   ‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print(f"   A B C D E F G")

def possible_moves( board ):
    col_ids = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    valid_indices = []
    for col_id, cell in zip(col_ids, board[0]):
        if cell == '∙': valid_indices += [f"{col_id}"]

    # print(f"  valid_moves:{valid_indices}")
    return valid_indices

def random_moves_strat( board, piece ):
    valid_moves = possible_moves(board)
    random_idx = int(rand() * len(valid_moves))
    # print(f"  {piece} {valid_moves[random_idx]} valid_moves:{valid_moves}")
    return valid_moves[random_idx]

def manual_moves_strat( board, piece ):
    print_board(board)
    valid_moves = possible_moves(board)
    print(f"  Valid Moves: {valid_moves}")
    move = input(f"  Input Move, {piece} Player eg. \"{valid_moves[int(rand() * len(valid_moves))]}\" -->")
    # input validation
    if len(move) < 1: 
        return 0
    move = move.strip().upper()[0:1]
    print(f"  human move:{piece} {move}")
    return move

def cheater_strat( board, piece ):
    board = [['O' for _ in range(4)] for _ in range(4)]
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

def count_consecutive(piece, row):
        count = 0
        num_in_a_row = 0
        for r in row:
            num_in_a_row = max(count, num_in_a_row)
            if r == piece: count += 1
            else: count = 0

        return num_in_a_row

def count_adjacent(piece, idx, row):
    num_adjacent = 0
    # count forward
    for r in row[idx+1:]:
        if r == piece: num_adjacent += 1
        else: break
    
    # count backward
    for r in row[idx::-1]:
        if r == piece: num_adjacent += 1
        else: break

    return num_adjacent


def parse_move(move):
    return ord(move[0].lower()) - 97

def board_col( board, c ):
    return [r[c] for r in board]

def board_diag(board, r, c, m):
    return []

def rc_from_move(board, move):
    c = parse_move(move)
    col = board_col(board, c)
    r = col.count('∙') - 1

    return r, c

def rank_connectfour_move(piece, board, move):
    r, c = rc_from_move(board, move)
    check_row = board[r]
    check_col = board_col(board, c)
    # check_diag1 = board_diag(board, r, c, 1)
    # check_diag2 = board_diag(board, r, c, -1)
    checks = [[check_row, c], [check_col, r]] #, check_diag1 : 0, check_diag2 : 0}
    # print(f"  check_win:{piece} [{r},{c}]")
    num_adjacent = 0
    for check, idx in checks:
        num_adjacent += count_adjacent(piece, idx, check)
        # print(f"    {check} ".ljust(50) + f"{num_in_a_row}", end='')
        if num_adjacent == 3:
            return 99

    return num_adjacent


def custom_strat( board, piece ):
    valid_moves = {v : 0 for v in possible_moves(board)}
    # rank potential moves
    for potential_move in valid_moves:
        valid_moves[potential_move] = rank_connectfour_move(piece, board, potential_move)
    # pick highest rank move

    # else pick random squares
    valid_moves = possible_moves(board)
    if valid_moves: 
        return valid_moves[int(rand() * len(valid_moves))]

    return "Z0"

""" 
player1 = Player(random_moves_strat)
player2 = Player(random_moves_strat)
game = Game(player1, player2)
game.run(False)
game.print_board()

player1 = Player(manual_moves_strat)
player2 = Player(random_moves_strat)
game = Game(player1, player2)
game.run(False)
game.print_board()
"""

strategies = [random_moves_strat, custom_strat]
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