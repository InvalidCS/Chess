from piece_movement import Pawn, Knight, Bishop, Rook, Queen, King

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
    tile_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
                 '1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    def __init__(self):
        self._turn = WHITE_TURN
        self._board = _setup_board()
        self._pieces = construct_pieces(self._board)
        self._captured_pieces = []
        self._move_history = []
        
    def get_turn(self):
        return self._turn
    
    def get_board(self):
        if self._turn == WHITE_TURN:
            return self._board
        else:
            return flip_board(self._board)
    
    def _switch_turn(self):
        self._turn = (BLACK_TURN if self._turn == WHITE_TURN else WHITE_TURN)
        
    def _find_piece(self, row: int, col: int, turn: int):
        for piece in self._pieces:
            if piece.find_tile() == (row, col) and piece.find_color() == turn:
                return piece
        raise InvalidMoveError()
    
    def _find_tile(self, tile):
        letter = tile[0]
        number = tile[1]
        return (GameState.tile_dict[number], GameState.tile_dict[letter])
    
    def make_move(self, start_tile: str, new_tile: str):
        if start_tile == new_tile:
            raise InvalidMoveError()
        row, col = self._find_tile(start_tile)
        new_row, new_col = self._find_tile(new_tile)
        
        if self._board[row][col] == NONE:
            raise InvalidMoveError()
        
        piece = self._find_piece(row, col, self._turn)
        if piece.valid_move(self._board, new_row, new_col):
            if self._board[new_row][new_col] != NONE:
                captured_piece = self._find_piece(new_row, new_col, self._turn*-1)
                self._pieces.remove(captured_piece)
                self._captured_pieces.append(captured_piece)
            self._board[new_row][new_col] = self._board[row][col]
            self._board[row][col] = NONE
            self._move_history.append((self._turn, start_tile, new_tile))
            self._switch_turn()
        else:
            raise InvalidMoveError()

    
def _create_empty_board() -> [[int]]:
    '''
    Creates an empty board with 8 rows and 8 columns.
    '''
    board = []
    for _ in range(8):
        sublist = []
        for _ in range(8):
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
    board[7][0] = 4
    board[7][1] = 3
    board[7][2] = 2
    board[7][3] = 5 
    board[7][4] = 6 
    board[7][5] = 2
    board[7][6] = 3
    board[7][7] = 4
    
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

def construct_pieces(board) -> []:
    all_pieces = []
    pieces_dict = {1: Pawn, 2: Bishop, 3: Knight, 4: Rook, 5: Queen, 6: King}
    for row in range(8):
        for col in range(8):
            tile = board[row][col]
            if tile > 0:
                all_pieces.append(pieces_dict[tile](row, col, 1))
            elif board[row][col] < 0:
                all_pieces.append(pieces_dict[abs(tile)](row, col, -1))      
    return all_pieces    