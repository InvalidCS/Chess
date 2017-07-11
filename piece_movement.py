NONE = 0
WHITE_TURN = 1
BLACK_TURN = -1

class Pawn:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int) -> [tuple]:
        valid_moves = []
        
        if board[row][col] > 0 and turn == WHITE_TURN:
            if row == 6:
                if board[5][col] == NONE and board[4][col] == NONE:
                    valid_moves.append((4, col))
            if board[row-1][col] == NONE:
                valid_moves.append((row-1, col))
            if valid_column(col+1) and board[row-1][col+1] < 0:
                valid_moves.append((row-1, col+1))
            if valid_column(col-1) and board[row-1][col-1] < 0:
                valid_moves.append((row-1, col-1))
        elif board[row][col] < 0 and turn == BLACK_TURN:
            if row == 1:
                if board[2][col] == NONE and board[3][col] == NONE:
                    valid_moves.append((3, col))
            if board[row+1][col] == NONE:
                valid_moves.append((row+1, col))
            if valid_column(col+1) and board[row+1][col+1] > 0:
                valid_moves.append((row+1, col+1))
            if valid_column(col-1) and board[row+1][col-1] > 0:
                valid_moves.append((row+1, col-1))        
    
        return valid_moves
    
    
    
class Knight:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        valid_moves = []
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
        if board[row][col] > 0 and turn == WHITE_TURN:
            for rowdelta, coldelta in directions:
                if valid_row(row+rowdelta) and valid_column(col+coldelta) and \
                board[row+rowdelta][col+coldelta] <= 0:
                    valid_moves.append((row+rowdelta, col+coldelta))
        elif board[row][col] < 0 and turn == BLACK_TURN:
            for rowdelta, coldelta in directions:
                if valid_row(row+rowdelta) and valid_column(col+coldelta) and \
                board[row+rowdelta][col+coldelta] >= 0:
                    valid_moves.append((row+rowdelta, col+coldelta))
        return valid_moves
    
    
    
class Bishop:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        valid_moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        if board[row][col] > 0 and turn == WHITE_TURN:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] > 0:
                        break
                    elif valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] < 0:
                        valid_moves.append((row+(rowdelta*i), col+(coldelta*i)))
                        break
                    elif valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] == NONE:
                        valid_moves.append((row+(rowdelta*i), col+(coldelta*i)))
        elif board[row][col] < 0 and turn == BLACK_TURN:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] < 0:
                        break
                    elif valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] > 0:
                        valid_moves.append((row+(rowdelta*i), col+(coldelta*i)))
                        break
                    elif valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] == NONE:
                        valid_moves.append((row+(rowdelta*i), col+(coldelta*i)))
    
        return valid_moves
    
class Rook:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        valid_moves = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        if board[row][col] > 0 and turn == WHITE_TURN:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] > 0:
                        break
                    elif valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] < 0:
                        valid_moves.append((row+(rowdelta*i), col+(coldelta*i)))
                        break
                    elif valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] == NONE:
                        valid_moves.append((row+(rowdelta*i), col+(coldelta*i)))
        elif board[row][col] < 0 and turn == BLACK_TURN:
            for rowdelta, coldelta in directions:
                for i in range(1, 8):
                    if valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] < 0:
                        break
                    elif valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] > 0:
                        valid_moves.append((row+(rowdelta*i), col+(coldelta*i)))
                        break
                    elif valid_row(row+(rowdelta*i)) and valid_column(col+(coldelta*i)) and \
                    board[row+(rowdelta*i)][col+(coldelta*i)] == NONE:
                        valid_moves.append((row+(rowdelta*i), col+(coldelta*i)))
    
        return valid_moves
    



class Queen(Bishop, Rook):
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return Bishop.valid_move(self, board, row, col, new_row, new_col, turn) or \
            Rook.valid_move(self, board, row, col, new_row, new_col, turn)


class King:
    def valid_move(self, board: [[int]], row: int, col: int, new_row: int, new_col: int,
                   turn: int) -> bool:
        return (new_row, new_col) in self._all_valid_moves(board, row, col, turn)
    
    def _all_valid_moves(self, board: [[int]], row: int, col: int, turn: int ) -> [tuple]:
        valid_moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        if board[row][col] > 0 and turn == WHITE_TURN:
            for rowdelta, coldelta in directions:
                if valid_row(row+rowdelta) and valid_column(col+coldelta) and \
                board[row+rowdelta][col+coldelta] <= 0:
                    valid_moves.append((row+rowdelta, col+coldelta))
        elif board[row][col] < 0 and turn == BLACK_TURN:
            for rowdelta, coldelta in directions:
                if valid_row(row+rowdelta) and valid_column(col+coldelta) and \
                board[row+rowdelta][col+coldelta] >= 0:
                    valid_moves.append((row+rowdelta, col+coldelta))
        return valid_moves
    
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
