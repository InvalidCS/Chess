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

def is_valid_row_number(row: int) -> bool:
    '''
    Returns True if the row number is between 0 and 7; False otherwise.
    '''
    return 0 <= row < 8

def is_valid_column_number(column: int) -> bool:
    '''
    Returns True if the column number is between 0 and 7; False otherwise.
    '''
    return 0 <= column < 8
        
        