# chess_logic.py

NONE = 0

WHITE_PAWN = 1
WHITE_KNIGHT = 2
WHITE_BISHOP = 3
WHITE_ROOK = 4
WHITE_QUEEN = 5
WHITE_KING = 6
W_TURN = 1

BLACK_PAWN = -1
BLACK_KNIGHT = -2
BLACK_BISHOP = -3
BLACK_ROOK = -4
BLACK_QUEEN = -5
BLACK_KING = -6
B_TURN = -1

def is_number(s) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_char(s) -> bool:
    try:
        ord(s)
        if(is_number(s)):
            return False
        else:
            return True
    except ValueError:
        return False

class GameState:

    def __init__(self,board,turn):
        self._board = board
        self._turn = turn
        print("When it is your turn, please only enter the starting and ending squares.\nDon't specify the piece's type or whether a piece is captured.")

    def _handle_turn(self):
        valid=False
        if(self._turn==W_TURN):
            pl = "White"
        else:
            pl = "Black"
        print(pl+"'s move")
        while(not valid):
            start = input("Select starting square: ")
            if(not self._valid_format(start)):
                print("Error: the format of the entered square is invalid.")
                continue
            [row,col] = self._get_rowcol(start)
            if(not Board.on_board(row,col)):
                print("Error: row or column is out of bounds.")
                continue
            piece = self._get_piece(row,col)
            if(piece == 0):
                print("Error: the square selected doesn't have a "+pl.lower()+" piece.")
                continue
            end = input("Select ending square: ")
            if(not self._valid_format(end)):
                print("Error: the format of the entered square is invalid.")
                continue
            [nrow,ncol] = self._get_rowcol(end)
            if(row==nrow and col == ncol):
                print("Error: starting square and ending square are the same.")
                continue
            if(not Board.on_board(nrow,ncol)):
                print("Error: row or column is out of bounds.")
                continue
            if((not board._occupied_ally(self._turn,nrow,ncol)) and self._is_valid(piece,row,col,nrow,ncol)):
                break
            else:
                print("Error: invalid move.")
        self._make_move(piece,row,col,nrow,ncol)

    def _valid_format(self,str) -> bool:
        if(not len(str) == 2):
            return False
        elif(not(is_char(str[0]) and is_number(str[1]))):
            return False
        else:
            return True
            

    def _get_rowcol(self,sq) -> [int,int]:
        sq = sq.lower()
        if(self._turn == W_TURN):
            col = ord(sq[0])-97
            row = 8-int(sq[1]) #Was 7-(int(sq[1])-1)
        else:
            col = 104-ord(sq[0]) #Was 7-(ord(sq[0])-97)
            row = int(sq[1])-1
        return [row,int(col)]

    def _get_piece(self,row,col) -> int:
        piece = board._board[row][col]
        if((self._turn>0) == (piece>0)):
            return piece #A check to see if the piece's value is 0 is not necessary since it will trigger an error in the function that called this anyway.
        else:
            return 0

    def _is_valid(self,piece,row,col,nrow,ncol) -> bool:
        mag = abs(piece)
        if(mag==WHITE_PAWN):
            if(Pawn.isValid(row,col,nrow,ncol,self._turn,self._board)):
                return True
        elif(mag==WHITE_KNIGHT):
            if(Knight.isValid(row,col,nrow,ncol)):
                return True
        elif(mag==WHITE_BISHOP):
            if(Bishop.isValid(row,col,nrow,ncol,self._board)):
                return True
        elif(mag==WHITE_ROOK):
            if(Rook.isValid(row,col,nrow,ncol,self._board)):
                return True
        elif(mag==WHITE_QUEEN):
            if(Queen.isValid(row,col,nrow,ncol,self._board)):
                return True
        elif(mag==WHITE_KING):
            if(King.isValid(row,col,nrow,ncol)):
                return True
        return False

    def _make_move(self,piece,row,col,nrow,ncol):
        board._adjust_board(piece,row,col,nrow,ncol)
        self._switch_turn()

    def _switch_turn(self):
        self._turn = -self._turn
        self._board._flip_board()




class Board:
    def __init__(self):
        self._board = create_empty_board()

    @staticmethod
    def on_board(row,col) -> bool:
        if(not (row in range(8) and col in range(8))):
            return False
        else:
            return True

    def _setup_board(self) -> None:
        '''
        Sets up initial arrangement of pieces on the board from White player's
        perspective.
        '''
        for row in range(8):
            if row == 1: # fills second row from top with black pawns
                for col in range(8):
                    self._board[row][col] = -1
            elif row == 6: # fills second row from bottom with white pawns
                for col in range(8):
                    self._board[row][col] = 1
            elif row == 0: # fills top-most row with white pieces
                self._board[row][0] = -4
                self._board[row][1] = -2
                self._board[row][2] = -3 
                self._board[row][3] = -5
                self._board[row][4] = -6
                self._board[row][5] = -3
                self._board[row][6] = -2
                self._board[row][7] = -4
            elif row == 7: # fills bottom-most row with black pieces
                self._board[row][0] = 4
                self._board[row][1] = 2
                self._board[row][2] = 3
                self._board[row][3] = 5
                self._board[row][4] = 6
                self._board[row][5] = 3
                self._board[row][6] = 2
                self._board[row][7] = 4

    def _flip_board(self) -> None:
        '''
        Flips the board to the other player's perspective.
        '''
        new_board = create_empty_board()
        for row in range(8):
            for col in range(8):
                new_board[row][col] = self._board[7 - row][7 - col]
                
        self._board = new_board

    def _adjust_board(self,piece,row,col,nrow,ncol):
        self._board[row][col] = 0
        self._board[nrow][ncol] = piece

    def _impeded(self,row,col,nrow,ncol) -> bool:
        rdiff = nrow-row
        if(not rdiff==0):
            rowcopy=row
            colcopy=col
            if(ncol-col==0):
                dcol=0
            elif(ncol>col):
                dcol=1
            else:
                dcol=-1
            if(nrow>row):
                drow=1
            else:
                drow=-1
            while(not(rowcopy+drow == nrow)):
                if(not(self._board[rowcopy+drow][colcopy+dcol] == 0)):
                    return True
                rowcopy+=drow
                colcopy+=dcol
        else:
            colcopy=col
            if(ncol-col==0):
                dcol=0
            elif(ncol>col):
                dcol=1
            else:
                dcol=-1
            while(not(colcopy+dcol == ncol)):
                if(not(self._board[row][colcopy+dcol] == 0)):
                    return True
                colcopy+=dcol
        return False

    def _occupied_ally(self,turn,nrow,ncol):
        if(not(self._occupied(nrow,ncol))):
            return False
        if((self._board[nrow][ncol] > 0) == (turn > 0)):
            return True
        else:
            return False

    def _occupied_enemy(self,turn,nrow,ncol):
        if(not(self._occupied(nrow,ncol))):
            return False
        if((-self._board[nrow][ncol] > 0) == (turn > 0)):
            return True
        else:
            return False

    def _occupied(self,nrow,ncol):
        if(self._board[nrow][ncol] == 0):
            return False
        else:
            return True

    def _disp_board_text(self) -> None:
        for row in range(8):
            line = ""
            for col in range(8):
                cp = ""
                if(self._board[row][col] == 0):
                    cp=" -- "
                    line+=cp
                    continue
                elif(self._board[row][col] > 0):
                    cp+=" W"
                else:
                    cp+=(" B")
                mag = abs(self._board[row][col])
                if(mag==WHITE_PAWN):
                    cp+=("P ")
                elif(mag==WHITE_KNIGHT):
                    cp+=("N ")
                elif(mag==WHITE_BISHOP):
                    cp+=("B ")
                elif(mag==WHITE_ROOK):
                    cp+=("R ")
                elif(mag==WHITE_QUEEN):
                    cp+=("Q ")
                else:
                    cp+=("K ")
                line+=cp
            print(line)

    
class Pawn(object):
    @staticmethod
    def isValid(row,col,nrow,ncol,turn,board) -> bool:
        dcol=ncol-col
        drow=nrow-row
        if(drow>=0 or dcol >1):
            return False
        elif(drow==-1):
            if(dcol == 0):
                return True
            else:
                if(board._occupied_enemy(turn,nrow,ncol)):
                    return True
                else:
                    return False
        elif(drow==-2 and dcol==0):
            if(row==6 and not board._impeded(row,col,nrow,ncol)):
                return True
            else:
                return False
        else:
            return False

class Knight(object):
    @staticmethod
    def isValid(row,col,nrow,ncol) -> bool:
        if((abs(row-nrow) == 2 and abs(col-ncol) == 1) or (abs(row-nrow) == 1 and abs(col-ncol) == 2)):
            return True
        else:
            return False

class Bishop(object):
    @staticmethod
    def isValid(row,col,nrow,ncol,board) -> bool:
        drow = abs(nrow-row)
        dcol = abs(ncol-col)
        if(drow==dcol):
            if(not board._impeded(row,col,nrow,ncol)):
               return True
        else:
            return False

class Rook(object):
    @staticmethod
    def isValid(row,col,nrow,ncol,board) -> bool:
        drow = abs(nrow-row)
        dcol = abs(ncol-col)
        if(drow==0 or dcol == 0):
            if(not board._impeded(row,col,nrow,ncol)):
               return True
        else:
            return False

class Queen(object):
    @staticmethod
    def isValid(row,col,nrow,ncol,board) -> bool:
        drow = abs(nrow-row)
        dcol = abs(ncol-col)
        if(drow==0 or dcol == 0 or drow == dcol):
            if(not board._impeded(row,col,nrow,ncol)):
               return True
        else:
            return False

class King(object):
    @staticmethod
    def isValid(row,col,nrow,ncol) -> bool:
        drow = abs(nrow-row)
        dcol = abs(ncol-col)
        if(drow <= 1 and dcol <= 1):
            return True
        else:
            return False


def create_empty_board() -> [[int]]:
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


def gameloop(gs):
    while True:
        gs._board._disp_board_text()
        gs._handle_turn()

if __name__ == '__main__':
    board = Board()
    board._setup_board()
    gs = GameState(board,W_TURN)
    gameloop(gs)
    