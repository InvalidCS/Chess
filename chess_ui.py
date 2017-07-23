import chess_logic

def play_chess() -> None:
    '''
    Plays a console-based version of Chess.
    '''
    print('Welcome to the Chess Game!')
    
    gamestate = chess_logic.GameState()
    
    while True:
        board = gamestate.get_board()
        turn = gamestate.get_turn()
        
        display_board(board, turn)
        display_turn(turn)

        start_tile = get_start_tile()
        new_tile = get_new_tile()
        row, col = find_tile(start_tile)
        new_row, new_col = find_tile(new_tile)
        try:
            gamestate.make_move(row, col, new_row, new_col)
            board = gamestate.get_board()
            
        except chess_logic.InvalidMoveError:
            print('\nInvalid move')
        except chess_logic.EmptyTileError:
            print('\nTile is empty')
        except chess_logic.WrongPieceError:
            print('\nCan\'t move opponent\'s piece')
        except chess_logic.SamePieceError:
            print('\nCan\'t move to tile with own piece')
        except chess_logic.GameOverError:
            display_winner(gamestate.get_board(), gamestate.get_winner())
            break
            
def valid_tile_format(tile: str) -> bool:
    '''
    Returns True if move consists of a  tile in the correct format with first character as a 
    letter(A-H) and second character a number(1-8). Any leading or trailing spaces are ignored.
    '''
    tile = tile.strip()
    if len(tile) != 2:
        return False
    if tile[0] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        return False
    if tile[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        return False
    return True

def get_start_tile() -> str:
    '''
    Prompts the user to enter a starting board tile in the correct format. Continues to prompt 
    the user until an appropriate tile format is entered. Returns a string (i.e. A5 or D7).
    '''
    while True:
        start_tile = input('Select a starting tile: ')
        if not valid_tile_format(start_tile):
            continue
        else:
            return start_tile.strip()

def get_new_tile() -> str:
    '''
    Prompts the user to enter an ending board tile in the correct format. Continues to prompt 
    the user until an appropriate tile format is entered. Returns a string (i.e. A5 or D7).
    '''
    while True:
        new_tile = input('Select a new tile: ')
        if not valid_tile_format(new_tile):
            continue
        else:
            return new_tile.strip()
        
def display_board(board: [[int]], turn: int) -> None:
    '''
    Prints the board in a readable format. P stands for Pawn, R stands for
    Rook, N stands for Knight, B stands for Bishop, Q stands for Queen, K stands
    for King, and a period stands for an empty tile. Uppercase letters stand for
    white pieces and lowercase letters stand for black pieces.
    '''
    piece_translation = {0: '.', -6: 'k', -5: 'q', -4: 'r', -3: 'n', -2: 'b', -1: 'p',
                         1: 'P', 2: 'B', 3: 'N', 4: 'R', 5: 'Q', 6: 'K'}
    if turn == chess_logic.WHITE_TURN:
        board_str = '\n   A  B  C  D  E  F  G  H\n'
    else:
        board_str = '\n   H  G  F  E  D  C  B  A\n'
    
    for row in range(8):
        if turn == chess_logic.WHITE_TURN:
            board_str += str(8 - row) + '  '
        else:
            board_str += str(1 + row) + '  '
        for col in range(8):
            board_str += piece_translation[board[row][col]] + '  '
        board_str += '\n'
    print(board_str)
            

def display_turn(turn: int) -> None:
    '''
    Displays the current player's turn.
    '''
    if turn == chess_logic.WHITE_TURN:
        print('WHITE\'S TURN')
    else:
        print('BLACK\'S TURN')
    
def display_winner(board: [[int]], winner: int):
    display_board(board, winner)
    if winner == 1:
        winner_str = 'WINNER: WHITE'
    elif winner == -1:
        winner_str = 'WINNER: BLACK'
    else:
        winner_str = 'DRAW'
    print(winner_str)

def find_tile(tile: str) -> (int, int):
    tile_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
                 '1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    letter = tile[0]
    number = tile[1]
    
    return (tile_dict[number], tile_dict[letter])
        

        
if __name__ == '__main__':
    play_chess()
    
    
    