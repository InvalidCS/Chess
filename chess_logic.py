from piece_movement import Pawn, Knight, Bishop, Rook, Queen, King, check_exposed_tiles

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

class EmptyTileError(Exception):
    '''
    Raise when the user tries to "move" an empty tile.
    '''
    pass

class WrongPieceError(Exception):
    '''
    Raise when the user tries to move an opposite-colored piece.
    '''
    pass

class SamePieceError(Exception):
    '''
    Raise when the user tries to move to a tile with its own piece.
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
        self._pieces = construct_pieces(self._board)
        self._captured_pieces = []
        self._move_history = []
        self._winner = NONE
        self._win_type = NONE
        self._game_over = False
        self._board_history = []
        self._piece_captured = False
        
    def get_turn(self) -> int:
        return self._turn
    
    def get_board(self) -> [[int]]:
        if self._turn == WHITE_TURN:
            return self._board
        else:
            return flip_board(self._board)
    
    def get_winner(self) -> int:
        return self._winner
    
    def get_win_type(self) -> str:
        return self._win_type
    
    def check_game_over(self) -> bool:
        return self._game_over
    
    def promote_pawn(self, row: int, col: int, new_row: int, new_col: int, piece: Pawn,
                     new_piece: str):
        print(new_piece)
        piece_to_class = {'B': Bishop, 'K': Knight, 'R': Rook, 'Q': Queen}
        piece_to_num = {('B', 1): 2, ('B', -1): -2, ('K', 1): 3, ('K', -1): -3,
                        ('R', 1): 4, ('R', -1): -4, ('Q', 1): 5, ('Q', -1): -5}
        self._board[row][col] = piece_to_num[(new_piece, self._turn)]
        self._pieces.remove(piece)
        piece_to_add = piece_to_class[new_piece](new_row, new_col, self._turn)
        self._pieces.append(piece_to_add)
    
    def castle_rook(self, new_row: int, new_col: int):
        if (new_row, new_col) == (7, 6):
            rook = self._find_piece(7, 7, 1)
            rook.change_position(7, 5)
            self._board[7][7] = NONE
            self._board[7][5] = 4
        elif (new_row, new_col) == (7, 2):
            rook = self._find_piece(7, 0, 1)
            rook.change_position(7, 3)
            self._board[7][0] = NONE
            self._board[7][3] = 4
        elif (new_row, new_col) == (0, 6):
            rook = self._find_piece(0, 7, -1)
            rook.change_position(0, 5)
            self._board[0][7] = NONE
            self._board[0][5] = -4
        else:
            rook = self._find_piece(0, 0, -1)
            rook.change_position(0, 3)
            self._board[0][0] = NONE
            self._board[0][3] = -4
        
    def _update_board(self, row: int, col: int, new_row: int, new_col: int, \
                      piece: 'Piece', new_piece: str or None):
        if type(piece) == Pawn and new_col != col and self._board[new_row][new_col] == NONE:
            self._board[row][new_col] = NONE
        elif type(piece) == Pawn and new_row in [0, 7]:
            self.promote_pawn(row, col, new_row, new_col, piece, new_piece)
        elif type(piece) == King and abs(new_col - col) > 1:
                self.castle_rook(new_row, new_col)
        
        self._remove_piece(new_row, new_col)
        self._board[new_row][new_col] = self._board[row][col]
        self._board[row][col] = NONE
        
    def _remove_piece(self, new_row: int, new_col: int):
        if self._board[new_row][new_col] != NONE:
            captured_piece = self._find_piece(new_row, new_col, self._turn*-1)
            self._pieces.remove(captured_piece)
            self._piece_captured = True
        else:
            self._piece_captured = False
        
    def _update_history(self, row: int, col:int, new_row: int, new_col: int, piece: 'Piece'):
        self._move_history.append((row, col, new_row, new_col, piece))
        if type(piece) == Pawn or self._piece_captured:
            self._board_history = [[x[:] for x in self._board]]
        else:
            self._board_history.append([x[:] for x in self._board])
            
    def _switch_turn(self):
        self._turn = (BLACK_TURN if self._turn == WHITE_TURN else WHITE_TURN)
        
    def _find_piece(self, row: int, col: int, turn: int):
        for piece in self._pieces:
            if piece.find_tile() == (row, col) and piece.find_color() == turn:
                return piece
        raise InvalidMoveError()

        
    def handle_draw(self):
        self._winner = NONE
        raise GameOverError()
    
    def check_tiles(self, row: int, col: int, new_row: int, new_col: int):
        if self._board[row][col] == NONE:
            raise EmptyTileError()
        elif self._turn == WHITE_TURN and self._board[row][col] < 0:
            raise WrongPieceError()
        elif self._turn == BLACK_TURN and self._board[row][col] > 0:
            raise WrongPieceError()
        elif self._turn == WHITE_TURN and self._board[new_row][new_col] > 0:
            raise SamePieceError()
        elif self._turn == BLACK_TURN and self._board[new_row][new_col] < 0:
            raise SamePieceError()
                                                            
               
    def _check_winner(self):
        opponent_turn = (BLACK_TURN if self._turn == WHITE_TURN else WHITE_TURN)
        opponent_pieces = [piece for piece in self._pieces if piece.find_color() == opponent_turn]
        
        if _check_threefold_repetition(self._board_history):
            self._winner = NONE
            self._win_type = 'Threefold Repetition'
            self._game_over = True
            raise GameOverError()
        
        elif _check_fifty_move_rule(self._board_history):
            self._winner = NONE
            self._win_type = 'Fifty Move Rule'
            self._game_over = True
            raise GameOverError()
        
        for piece in opponent_pieces: 
            if piece._all_valid_moves(self._board, self._pieces, self._move_history):
                return 
        king_position = [(row, col) for row in range(8) for col in range(8) if self._board[row][col] == -6*self._turn]
        if not check_exposed_tiles(self._board, king_position, self._pieces, self._turn*-1, self._move_history):
            self._winner = NONE
            self._win_type = 'Stalemate'
        else:
            self._winner = self._turn
            self._win_type = 'Checkmate'
        self._game_over = True
        raise GameOverError()
        
    
    def make_move(self, row: int, col: int, new_row: int, new_col: int, new_piece = None):
        self.check_tiles(row, col, new_row, new_col)
        
        piece = self._find_piece(row, col, self._turn)
        
        if piece.valid_move(self._board, new_row, new_col, self._pieces, self._move_history):
            self._update_board(row, col, new_row, new_col, piece, new_piece)
            self._update_history(row, col, new_row, new_col, piece)
            self._check_winner()
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

def setup_tester() -> [[int]]:
    board = _create_empty_board()
    board[0][0] = -6
    board[3][0] = 6
    board[2][2] = 5
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


def _find_king(board: [[int]], turn: int) -> (int, int):
    king = (6 if turn == WHITE_TURN else -6)
    for row in range(8):
        for col in range(8):
            if board[row][col] == king:
                return (row, col)

def _check_threefold_repetition(board_history: [[[int]]]) -> bool:
    if len(board_history) < 3:
        return False
    elif len(board_history) == 3 and board_history[0] == board_history[1] and board_history[0] == board_history[2]:
        return True
    elif board_history[-1] == board_history[-2]:
        if board_history[-1] == board_history[-3]:
            return True
        else:
            new_board_history = board_history[:]
            del new_board_history [-3]
            return _check_threefold_repetition(new_board_history)
        
    else:
        new_board_history = board_history[:]
        del new_board_history[-2]
        return _check_threefold_repetition(new_board_history)
        

def _check_fifty_move_rule(board_history: [[[int]]]) -> bool:
    return len(board_history) == 100

