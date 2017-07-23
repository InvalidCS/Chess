import tkinter
from PIL.ImageTk import PhotoImage
import point
import tiles
import chess_logic

class ChessApplication:
    
    def __init__(self):
        self._root_window = tkinter.Tk()
        
        self.board = tiles.Board()
        
        self._board_canvas = tkinter.Canvas(
            master = self._root_window,
            width = 800, height = 800,
            background='white')
        
        self._board_canvas.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N+tkinter.S+tkinter.E+tkinter.W)
        
        self._board_canvas.bind('<Configure>', self._on_board_resized)
        self._board_canvas.bind('<Button-1>', self._on_board_clicked)
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        
        self._W_PAWN_image = PhotoImage(file='W_Pawn.gif')
        self._W_KNIGHT_image = PhotoImage(file='W_Knight.gif')
        self._W_BISHOP_image = PhotoImage(file='W_Bishop.gif')
        self._W_ROOK_image = PhotoImage(file='W_Rook.gif')
        self._W_QUEEN_image = PhotoImage(file='W_Queen.gif')
        self._W_KING_image = PhotoImage(file='W_King.gif')
        self._B_PAWN_image = PhotoImage(file='B_Pawn.gif')
        self._B_KNIGHT_image = PhotoImage(file='B_Knight.gif')
        self._B_BISHOP_image = PhotoImage(file='B_Bishop.gif')
        self._B_ROOK_image = PhotoImage(file='B_Rook.gif')
        self._B_QUEEN_image = PhotoImage(file='B_Queen.gif')
        self._B_KING_image = PhotoImage(file='B_King.gif')
    
    def _on_board_resized(self, event: tkinter.Event):
        self._redraw_board()
        
    def _on_board_clicked(self, event: tkinter.Event):
        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()
        
        click_point = point.from_pixel(event.x, event.y, canvas_width, canvas_height)
        
        self.board.handle_move_click(click_point)
        
        self._redraw_board()
    
    def _redraw_board(self):
        self._board_canvas.delete(tkinter.ALL)
        
        canvas_width = self._board_canvas.winfo_width()
        canvas_height = self._board_canvas.winfo_height()
        
        for tile in self.board.get_tiles():
            topleft_x, topleft_y = tile.topleft.frac()
            bottomright_x, bottomright_y = tile.bottomright.frac()
            if (tile.row + tile.col) % 2 == 0:
                self._board_canvas.create_rectangle(
                    topleft_x*canvas_width, topleft_y*canvas_height,
                    bottomright_x*canvas_width, bottomright_y*canvas_height,
                    fill='#eeeed2')
            else:
                self._board_canvas.create_rectangle(
                    topleft_x*canvas_width, topleft_y*canvas_height,
                    bottomright_x*canvas_width, bottomright_y*canvas_height,
                    fill='#769656')
            if tile.piece != chess_logic.NONE:
                if tile.piece == chess_logic.WHITE_PAWN:
                    image = self._W_PAWN_image
                elif tile.piece == chess_logic.WHITE_BISHOP:
                    image = self._W_BISHOP_image
                elif tile.piece == chess_logic.WHITE_KNIGHT:
                    image = self._W_KNIGHT_image
                elif tile.piece == chess_logic.WHITE_ROOK:
                    image = self._W_ROOK_image
                elif tile.piece == chess_logic.WHITE_QUEEN:
                    image = self._W_QUEEN_image
                elif tile.piece == chess_logic.WHITE_KING:
                    image = self._W_KING_image
                elif tile.piece == chess_logic.BLACK_PAWN:
                    image = self._B_PAWN_image
                elif tile.piece == chess_logic.BLACK_BISHOP:
                    image = self._B_BISHOP_image
                elif tile.piece == chess_logic.BLACK_KNIGHT:
                    image = self._B_KNIGHT_image
                elif tile.piece == chess_logic.BLACK_ROOK:
                    image = self._B_ROOK_image
                elif tile.piece == chess_logic.BLACK_QUEEN:
                    image =  self._B_QUEEN_image
                elif tile.piece == chess_logic.BLACK_KING:
                    image = self._B_KING_image
                
                topleft_pixel = tile.topleft.pixel(canvas_width, canvas_height)
                bottomright_pixel = tile.bottomright.pixel(canvas_width, canvas_height)
                self._board_canvas.create_image(
                    (bottomright_pixel[0]+topleft_pixel[0])/2, 
                    (bottomright_pixel[1]+topleft_pixel[1])/2,
                    image = image)
            
    
    
        
    def run(self):
        self._root_window.mainloop()
           

if __name__ == '__main__':
    ChessApplication().run()