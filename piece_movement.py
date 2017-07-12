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
    
    def change_position(self, new_row: int, new_col: int) -> int:
        self._row = new_row
        self._col = new_col
    
    def valid_move(self, board: [[int]], new_row: int, new_col: int) -> bool:
        return (new_row, new_col) in self.all_valid_moves(board)

    def all_valid_moves(self, board: [[int]]) -> [tuple]:
        possible_moves = []
        
        if self._color == 1:
            if self._row == 6:
                if board[5][self._col] == NONE and board[4][self._col] == NONE:
                    possible_moves.append((4, self._col))
            if board[self._row-1][self._col] == NONE:
                possible_moves.append((self._row-1, self._col))
            if valid_column(self._col+1) and board[self._row-1][self._col+1] < 0:
                possible_moves.append((self._row-1, self._col+1))
            if valid_column(self._col-1) and board[self._row-1][self._col-1] < 0:
                possible_moves.append((self._row-1, self._col-1))
        else:
            if self._row == 1:
                if board[2][self._col] == NONE and board[3][self._col] == NONE:
                    possible_moves.append((3, self._col))
            if board[self._row+1][self._col] == NONE:
                possible_moves.append((self._row+1, self._col))
            if valid_column(self._col+1) and board[self._row+1][self._col+1] > 0:
                possible_moves.append((self._row+1, self._col+1))
            if valid_column(self._col-1) and board[self._row+1][self._col-1] > 0:
                possible_moves.append((self._row+1, self._col-1))        
    
        return possible_moves
    
    
    
class Knight:
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
        
    def valid_move(self, board: [[int]], new_row: int, new_col: int) -> bool:
        return (new_row, new_col) in self.all_valid_moves(board)
    
    def all_valid_moves(self, board: [[int]]) -> [tuple]:
        possible_moves = []
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
        if self._color == 1:
            for rowdelta, coldelta in directions:
                if valid_row(self._row+rowdelta) and valid_column(self._col+coldelta) and \
                board[self._row+rowdelta][self._col+coldelta] <= 0:
                    possible_moves.append((self._row+rowdelta, self._col+coldelta))
        else:
            for rowdelta, coldelta in directions:
                if valid_row(self._row+rowdelta) and valid_column(self._col+coldelta) and \
                board[self._row+rowdelta][self._col+coldelta] >= 0:
                    possible_moves.append((self._row+rowdelta, self._col+coldelta))
        return possible_moves
    
    
    
class Bishop:
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
        
    def valid_move(self, board: [[int]], new_row: int, new_col: int) -> bool:
        return (new_row, new_col) in self.all_valid_moves(board)
    
    def all_valid_moves(self, board: [[int]]) -> [tuple]:
        possible_moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        if self._color == 1:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] > 0:
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] < 0:
                        possible_moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] == NONE:
                        possible_moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
        else:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] < 0:
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] > 0:
                        possible_moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) and \
                    board[self._row+(rowdelta*i)][self._col+(coldelta*i)] == NONE:
                        possible_moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
    
        return possible_moves
    
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
        
    def valid_move(self, board: [[int]], new_row: int, new_col: int) -> bool:
        return (new_row, new_col) in self.all_valid_moves(board)
    
    def all_valid_moves(self, board: [[int]]) -> [tuple]:
        possible_moves = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        if self._color == 1:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] > 0:
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] < 0:
                        possible_moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] == NONE:
                        possible_moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
        else:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] < 0:
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] > 0:
                        possible_moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
                        break
                    elif valid_row(self._row+(rowdelta*i)) and valid_column(self._col+(coldelta*i)) \
                    and board[self._row+(rowdelta*i)][self._col+(coldelta*i)] == NONE:
                        possible_moves.append((self._row+(rowdelta*i), self._col+(coldelta*i)))
    
        return possible_moves
    



class Queen(Bishop, Rook):
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
        
    def valid_move(self, board: [[int]], new_row: int, new_col: int) -> bool:
        Bishop.__init__(self, self._row, self._col, self._color)
        Rook.__init__(self, self._row, self._col, self._color)
        return (new_row, new_col) in Bishop.all_valid_moves(self, board) or \
        Rook.all_valid_moves(self, board)


class King:
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
        
    def valid_move(self, board: [[int]], new_row: int, new_col: int) -> bool:
        return (new_row, new_col) in self.all_valid_moves(board)
    
    def all_valid_moves(self, board: [[int]]) -> [tuple]:
        possible_moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        if self._color == 1:
            for rowdelta, coldelta in directions:
                if valid_row(self._row+rowdelta) and valid_column(self._col+coldelta) and \
                board[self._row+rowdelta][self._col+coldelta] <= 0:
                    possible_moves.append((self._row+rowdelta, self._col+coldelta))
        else:
            for rowdelta, coldelta in directions:
                if valid_row(self._row+rowdelta) and valid_column(self._col+coldelta) and \
                board[self._row+rowdelta][self._col+coldelta] >= 0:
                    possible_moves.append((self._row+rowdelta, self._col+coldelta))
        return possible_moves
    
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


    

