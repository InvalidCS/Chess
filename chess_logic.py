NONE = 0

WHITE_PAWN = 1
WHITE_KNIGHT = 3
WHITE_BISHOP = 2
WHITE_ROOK = 4
WHITE_QUEEN = 5
WHITE_KING = 6
WHITE_TURN = 1

BLACK_PAWN = -1
BLACK_KNIGHT = -3
BLACK_BISHOP = -2
BLACK_ROOK = -4
BLACK_QUEEN = -5
BLACK_KING = -6
BLACK_TURN = -1

class InvalidMoveError(Exception):
    '''
    Raise when the user makes an invalid move.
    '''
    pass

class GameOverError(Exception):
    '''
    Raised when the user wants to make a move from an empty tile.
    '''
    pass


class GameState:
    def __init__(self):
        self._turn = WHITE_TURN
        self._board = _setup_board()
        
    def get_turn(self):
        return self._turn
    
    def get_board(self):
        return self._board
    
    def _switch_turn(self):
        self._turn = (BLACK_TURN if self._turn == WHITE_TURN else WHITE_TURN)
        
    def _find_piece(self, row: int, col: int):
        num_to_piece = {1: Pawn(), 2: Knight(), 3: Bishop(), 4: Rook(),
                             5: Queen(), 6: King()}
        return num_to_piece[abs(self._board[row][col])]
    
    def make_move(self, row: int, col: int, new_row: int, new_col: int):
        row -= 1
        col -= 1
        new_row -= 1
        new_col -= 1
        
        if self._board[row][col] == NONE:
            raise InvalidMoveError()
        
        piece = self.find_piece(row, col)
        if piece.valid_move(self._board, row, col, new_row, new_col, self._turn):
            self._board[new_row][new_col] = self._board[row][col]
            self._board[row][col] = NONE
            self._switch_turn()
        else:
            raise InvalidMoveError()

class Pawn:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        pass

class Knight:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        pass
    
class Bishop:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        pass
    
class Rook:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        pass
    
class Queen:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        pass
    
class King:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        pass
    
def _create_empty_board() -> [[int]]:
    '''
    Creates an empty board with 8 rows and 8 columns.
    '''
    board = []
    for row in range(8):
        sublist = []
        for col in range(8):
            sublist.append(NONE)
        board.append(sublist)
    return board

def _setup_board() -> [[int]]:
    '''
    Sets up initial arrangement of pieces on the board from White player's perspective.
    '''
    board = _create_empty_board()
    for col in range(8):
        board[1][col] = -1
        board[6][col] = 1
        
    board[0][0] = -4
    board[0][1] = -3
    board[0][2] = -2
    board[0][3] = -5
    board[0][4] = -6
    board[0][5] = -2
    board[0][6] = -3
    board[0][7] = -4
    board[1][0] = 4
    board[1][1] = 3
    board[1][2] = 2
    board[1][3] = 5 
    board[1][4] = 6 
    board[1][5] = 2
    board[1][6] = 3
    board[1][7] = 4
    
    return board

def flip_board(board: [[int]]) -> [[int]]:
    '''
    Flips the board to the opposite player's perspective.
    '''
    flipped_board = _create_empty_board()
    for row in range(8):
        for col in range(8):
            flipped_board[row][col] = board[7-row][7-col]
    return flipped_board

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
        
        