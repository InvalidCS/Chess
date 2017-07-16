NONE = 0
WHITE_TURN = 1
BLACK_TURN = -1

class Pawn:
    def __init__(self, row, col, color):
        self._row = row
        self._col = col
        self._color = color
        
    def find_tile(self) -> (int, int):
        return (self._row, self._col)
    
    def find_color(self) -> int:
        return self._color
    
    def valid_move(self, board: [[int]], new_row: int, new_col: int, pieces: [], history: []) -> bool:
        if (new_row, new_col) in self._all_valid_moves(board, pieces, history):
            self._row = new_row
            self._col = new_col
            return True
        else:
            return False
    
    def _all_valid_moves(self, board: [[int]], pieces: [], history: []) -> [(int, int)]:
        return _protect_king(board, self._row, self._col, pieces, self.possible_moves(board, history), self._color, history)

    def possible_moves(self, board: [[int]], history: []) -> [(int, int)]:
        moves = []
        
        if self._color == 1:
            if self._row == 6:
                if board[5][self._col] == NONE and board[4][self._col] == NONE:
                    moves.append((4, self._col))
            if board[self._row-1][self._col] == NONE:
                moves.append((self._row-1, self._col))
            if valid_column(self._col+1) and board[self._row-1][self._col+1] < 0:
                moves.append((self._row-1, self._col+1))
            if valid_column(self._col-1) and board[self._row-1][self._col-1] < 0:
                moves.append((self._row-1, self._col-1))
            if self._row == 3:
                if valid_column(self._col-1) and board[3][self._col-1] == -1:
                    last_move = history[-1]
                    if (last_move[0], last_move[1], last_move[2], last_move[3]) == \
                    (1, self._col-1, 3, self._col-1):
                        moves.append((self._row-1, self._col-1))
                if valid_column(self._col+1) and board[3][self._col+1] == -1:
                    last_move = history[-1]
                    if (last_move[0], last_move[1], last_move[2], last_move[3]) == \
                    (1, self._col+1, 3, self._col+1):
                        moves.append((self._row-1, self._col+1))
        else:
            if self._row == 1:
                if board[2][self._col] == NONE and board[3][self._col] == NONE:
                    moves.append((3, self._col))
            if board[self._row+1][self._col] == NONE:
                moves.append((self._row+1, self._col))
            if valid_column(self._col+1) and board[self._row+1][self._col+1] > 0:
                moves.append((self._row+1, self._col+1))
            if valid_column(self._col-1) and board[self._row+1][self._col-1] > 0:
                moves.append((self._row+1, self._col-1))        
            if self._row == 4:
                if valid_column(self._col-1) and board[4][self._col-1] == 1:
                    last_move = history[-1]
                    if (last_move[0], last_move[1], last_move[2], last_move[3]) == \
                    (6, self._col-1, 4, self._col-1):
                        moves.append((self._row+1, self._col-1))    
                if valid_column(self._col+1) and board[4][self._col+1] == 1:
                    last_move = history[-1]
                    if (last_move[0], last_move[1], last_move[2], last_move[3]) == \
                    (6, self._col+1, 4, self._col+1):
                        moves.append((self._row+1, self._col+1))
        return moves
    
    
    
    
class Knight:
    def __init__(self, row, col, color):
        self._row = row
        self._col = col
        self._color = color
    
    def find_tile(self) -> (int, int):
        return (self._row, self._col)
    
    def find_color(self) -> int:
        return self._color
        
    def valid_move(self, board: [[int]], new_row: int, new_col: int, pieces: [], history: []) -> bool:
        if (new_row, new_col) in self._all_valid_moves(board, pieces, history):
            self._row = new_row
            self._col = new_col
            return True
        else:
            return False
    
    def _all_valid_moves(self, board: [[int]], pieces: [], history: []) -> [(int, int)]:
        return _protect_king(board, self._row, self._col, pieces, self.possible_moves(board, history), self._color, history)
    
    def possible_moves(self, board: [[int]], history: []) -> [(int, int)]:
        moves = []
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
        if self._color == 1:
            for rowdelta, coldelta in directions:
                if valid_row(self._row+rowdelta) and valid_column(self._col+coldelta) and \
                board[self._row+rowdelta][self._col+coldelta] <= 0:
                    moves.append((self._row+rowdelta, self._col+coldelta))
        else:
            for rowdelta, coldelta in directions:
                if valid_row(self._row+rowdelta) and valid_column(self._col+coldelta) and \
                board[self._row+rowdelta][self._col+coldelta] >= 0:
                    moves.append((self._row+rowdelta, self._col+coldelta))
        return moves
    
    
    
class Bishop:
    def __init__(self, row, col, color):
        self._row = row
        self._col = col
        self._color = color
    
    def find_tile(self) -> (int, int):
        return (self._row, self._col)
    
    def find_color(self) -> int:
        return self._color
  
    def valid_move(self, board: [[int]], new_row: int, new_col: int, pieces: [], history: []) -> bool:
        if (new_row, new_col) in self._all_valid_moves(board, pieces, history):
            self._row = new_row
            self._col = new_col
            return True
        else:
            return False
    
    def _all_valid_moves(self, board: [[int]], pieces: [], history: []) -> [(int, int)]:
        return _protect_king(board, self._row, self._col, pieces, self.possible_moves(board, history), self._color, history)
    
    def possible_moves(self, board: [[int]], history: []) -> [(int, int)]:
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        if self._color == 1:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] > 0:
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] < 0:
                        moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] == NONE:
                        moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
        else:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] < 0:
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] > 0:
                        moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) and \
                    board[self._row+(rowdelta*i)][self._col+(coldelta*i)] == NONE:
                        moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
    
        return moves
    
class Rook:
    def __init__(self, row, col, color):
        self._row = row
        self._col = col
        self._color = color
    
    def find_tile(self) -> (int, int):
        return (self._row, self._col)
    
    def find_color(self) -> int:
        return self._color
    
    def change_position(self, new_row: int, new_col: int):
        self._row = new_row
        self._col = new_col
    
        
    def valid_move(self, board: [[int]], new_row: int, new_col: int, pieces: [], history: []) -> bool:
        if (new_row, new_col) in self._all_valid_moves(board, pieces, history):
            self._row = new_row
            self._col = new_col
            return True
        else:
            return False
        
    def _all_valid_moves(self, board: [[int]], pieces: [], history: []) -> [(int, int)]:
        return _protect_king(board, self._row, self._col, pieces, self.possible_moves(board, history), self._color, history)
    
    def possible_moves(self, board: [[int]], history: []) -> [(int, int)]:
        moves = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        if self._color == 1:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] > 0:
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] < 0:
                        moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] == NONE:
                        moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
        else:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] < 0:
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] > 0:
                        moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] == NONE:
                        moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
        return moves
    



class Queen(Bishop, Rook):
    def __init__(self, row, col, color):
        self._row = row
        self._col = col
        self._color = color
        
    def find_tile(self) -> (int, int):
        return (self._row, self._col)
    
    def find_color(self) -> int:
        return self._color
    
        
    def valid_move(self, board: [[int]], new_row: int, new_col: int, pieces: [], history: []) -> bool:
        
        if (new_row, new_col) in self._all_valid_moves(board, pieces, history):
            self._row = new_row
            self._col = new_col
            return True
        else:
            return False
        
    def _all_valid_moves(self, board: [[int]], pieces: [], history: []) -> [(int, int)]:
        return _protect_king(board, self._row, self._col, pieces, self.possible_moves(board, history), self._color, history)
    
    def possible_moves(self, board: [[int]], history: []):
        Bishop.__init__(self, self._row, self._col, self._color)
        Rook.__init__(self, self._row, self._col, self._color)
        return Bishop.possible_moves(self, board, history) + Rook.possible_moves(self, board, history)


class King:
    def __init__(self, row, col, color):
        self._row = row
        self._col = col
        self._color = color
    
    def find_tile(self) -> (int, int):
        return (self._row, self._col)
    
    def find_color(self) -> int:
        return self._color
    
    def valid_move(self, board: [[int]], new_row: int, new_col: int, pieces: [], history: []) -> bool:
        if (new_row, new_col) in self._all_valid_moves(board, pieces, history):
            self._row = new_row
            self._col = new_col
            return True
        else:
            return False
    
    def _all_valid_moves(self, board: [[int]], pieces: [], history: []) -> [(int, int)]:
        castling_moves = []
        if self._color == 1:
            if board[7][4] == 6 and board[7][7] == 4 and board[7][5] == NONE and board[7][6] == NONE:
                    pieces_moved = [h[4] for h in history]
                    if not _check_exposed_tiles(board, [(7, 7), (7, 5), (7, 6), (7, 4)], pieces, self._color, history) and \
                    _find_piece(7, 7, pieces) not in pieces_moved and self not in pieces_moved:
                        castling_moves.append((7, 6))
            if board[7][4] == 6 and board[7][0] == 4 and board[7][1] == NONE and board[7][2] == NONE \
            and board[7][3] == NONE:
                pieces_moved = [h[4] for h in history]
                if not _check_exposed_tiles(board, [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)], pieces, self._color, history) and \
                _find_piece(7, 0, pieces) not in pieces_moved and self not in pieces_moved:
                    castling_moves.append((7, 2))
        else:
            if board[0][4] == -6 and board[0][7] == -4 and board[0][5] == NONE and board[0][6] == NONE:
                    pieces_moved = [h[4] for h in history]
                    if not _check_exposed_tiles(board, [(0, 7), (0, 5), (0, 6), (0, 4)], pieces, self._color, history) and \
                    _find_piece(0, 7, pieces) not in pieces_moved and self not in pieces_moved:
                        castling_moves.append((0, 6))
            if board[0][4] == -6 and board[0][0] == -4 and board[0][1] == NONE and board[0][2] == NONE \
            and board[0][3] == NONE:
                pieces_moved = [h[4] for h in history]
                if not _check_exposed_tiles(board, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], pieces, self._color, history) and \
                _find_piece(0, 0, pieces) not in pieces_moved and self not in pieces_moved:
                    castling_moves.append((0, 2))
            
        return _protect_king(board, self._row, self._col, pieces, self.possible_moves(board, history), self._color, history) \
            + castling_moves
    
    def possible_moves(self, board: [[int]], history: []) -> [(int, int)]:
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        if self._color == 1:
            for rowdelta, coldelta in directions:
                if valid_row(self._row+rowdelta) and valid_column(self._col+coldelta) and \
                board[self._row+rowdelta][self._col+coldelta] <= 0:
                    moves.append((self._row+rowdelta, self._col+coldelta))
        else:
            for rowdelta, coldelta in directions:
                if valid_row(self._row+rowdelta) and valid_column(self._col+coldelta) and \
                board[self._row+rowdelta][self._col+coldelta] >= 0:
                    moves.append((self._row+rowdelta, self._col+coldelta))
        return moves
    
def valid_row(row: int) -> bool:
    '''
    Returns True if the row number is between 0 and 7; False otherwise.
    '''
    return 0 <= row < 8


def valid_column(column: int) -> bool:
    '''
    Returns True if the column number is between 0 and 7; False otherwise.
    '''
    return 0 <= column < 8

def _find_king(board: [[int]], turn: int) -> (int, int):
    king = (6 if turn == WHITE_TURN else -6)
    for row in range(8):
        for col in range(8):
            if board[row][col] == king:
                return (row, col)

def _protect_king(board: [[int]], row: int, col: int, pieces: [], possible_moves: [(int, int)],
                  turn: int, history: int) -> [(int, int)]:
    opponent_turn = turn*-1
    valid_moves = possible_moves[:]
    for new_row, new_col in possible_moves:
        possible_board = [x[:] for x in board]
        possible_board[new_row][new_col] = possible_board[row][col]
        possible_board[row][col] = NONE
        king_position = _find_king(possible_board, turn)
        opponent_pieces = [piece for piece in pieces if piece.find_color() == opponent_turn
                           and piece.find_tile() != (new_row, new_col)]
        for piece in opponent_pieces:
            if king_position in piece.possible_moves(possible_board, history):
                valid_moves.remove((new_row, new_col))
                break
    return valid_moves

def _check_exposed_tiles(board: [[int]], tiles: [(int, int)], pieces: [], turn: int, history: []) -> bool:
    opponent_turn = turn*-1
    opponent_pieces = [piece for piece in pieces if piece.find_color() == opponent_turn]
    for row, col in tiles:
        for piece in opponent_pieces:
            if (row, col) in piece.possible_moves(board, history):
                return True
    return False

def _find_piece(row: int, col: int, pieces: []) -> 'piece' or None:
    for piece in pieces: 
        if (row, col) == (piece._row, piece._col):
            return piece

    
