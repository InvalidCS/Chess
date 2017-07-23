import point
import chess_logic

class Tile:
    def __init__(self, row: int, col: int, topleft_point: point.Point, 
                 bottomright_point: point.Point):
        self.row = row
        self.col = col
        self.topleft = topleft_point
        self.bottomright = bottomright_point
        self.piece = 0
        self.color = 0
        self.clicked = False
    
    def adjust_color(self):
        if self.piece == 0:
            self.color = 0
        elif self.piece > 0:
            self.color = 1
        else:
            self.color = -1
    
    def contains(self, click_point: point.Point) -> bool:
        topleft_x, topleft_y = self.topleft.frac()
        bottomright_x, bottomright_y = self.bottomright.frac()
        click_point_x, click_point_y = click_point.frac()
        
        return (topleft_x < click_point_x < bottomright_x) and \
            (topleft_y < click_point_y < bottomright_y)

class Board:
    
    def __init__(self):
        self.gamestate = chess_logic.GameState()
        self.tiles = create_empty_board()
        self.start_tile_clicked = False
        self.update_tiles(flip=False)
        
    def get_tiles(self) -> [Tile]:
        return self.tiles
    
    def update_tiles(self, flip=True):
        board = self.gamestate.get_board()
        for tile in self.tiles:
            row, col = tile.row, tile.col
            tile.piece = board[row][col]
            tile.adjust_color()
                
    def handle_move_click(self, click_point: point.Point):
        turn = self.gamestate.get_turn()
        for tile in self.tiles:
            if tile.contains(click_point):
                print('Piece: ' + str(tile.piece))
                print('Row: ' + str(tile.row))
                print('Col: ' + str(tile.col))
                print()
                if not self.start_tile_clicked and turn == tile.color:
                    tile.clicked = True
                    self.last_tile_clicked = tile
                    self.start_tile_clicked = True
                    self.row_clicked = (tile.row if turn == 1 else 7 - tile.row)
                    self.column_clicked = (tile.col if turn == 1 else 7 - tile.col)
                elif self.start_tile_clicked and turn == tile.color:
                    self.last_tile_clicked.clicked = False
                    tile.clicked = True
                    self.last_tile_clicked = tile
                    self.row_clicked = (tile.row if turn == 1 else 7 - tile.row)
                    self.column_clicked = (tile.col if turn == 1 else 7 - tile.col)
                elif self.start_tile_clicked and turn != tile.color:
                    self.new_row_clicked = (tile.row if turn == 1 else 7 - tile.row)
                    self.new_column_clicked = (tile.col if turn == 1 else 7 - tile.col)
                    self.make_move(
                        self.row_clicked, self.column_clicked,
                         self.new_row_clicked, self.new_column_clicked)
                    
    def make_move(self, row: int, col: int, new_row: int, new_col: int):
        try:
            self.gamestate.make_move(row, col, new_row, new_col)
            self.update_tiles()
            self.start_tile_clicked = False
            self.last_tile_clicked.clicked = False
        except chess_logic.InvalidMoveError:
            pass
        except chess_logic.GameOverError:
            pass
                

def create_empty_board():
    all_tiles = []
    for row in range(8):
        for col in range(8):
            topleft_frac = point.from_frac(col/8, row/8)
            bottomright_frac = point.from_frac((col+1)/8, (row+1)/8)
            all_tiles.append(Tile(row, col, topleft_frac, bottomright_frac))
    return all_tiles
