import tkinter
from PIL.ImageTk import PhotoImage

class PawnPromotionChoice:
    def __init__(self, piece_color):
        self._popup_window = tkinter.Toplevel()
        self._color = piece_color
        self._choice_canvas = tkinter.Canvas(
            master = self._popup_window,
            width = 200, height = 200,
            background = 'white'
            )
        self._choice_canvas.grid(
            row = 0, column = 0,
            padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._choice_canvas.bind('<Configure>', self._on_canvas_resized)
        self._choice_canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._popup_window.rowconfigure(0, weight=1)
        self._popup_window.columnconfigure(0, weight=1)
        self._clicked = False
    
        self.W_QUEEN = PhotoImage(file='W_Queen.gif')
        self.W_ROOK = PhotoImage(file='W_Rook.gif')
        self.W_BISHOP = PhotoImage(file='W_Bishop.gif')
        self.W_KNIGHT = PhotoImage(file='W_Knight.gif')
        self.B_QUEEN = PhotoImage(file='B_Queen.gif')
        self.B_ROOK = PhotoImage(file='B_Rook.gif')
        self.B_BISHOP = PhotoImage(file='B_Bishop.gif')
        self.B_KNIGHT = PhotoImage(file='B_Knight.gif')
        
    def _on_canvas_resized(self, event: tkinter.Event):
        self._redraw_canvas()
    
    def _on_canvas_clicked(self, event: tkinter.Event):
        canvas_width = self._choice_canvas.winfo_width()
        canvas_height = self._choice_canvas.winfo_height()
        
        if 0 < event.x < canvas_width * 0.5 and \
        0 < event.y < canvas_height * 0.5:
            self._clicked = True
            self.piece = 'Q'
        
        if  canvas_width * 0.5 < event.x < canvas_width and \
        0 < event.y < canvas_height * 0.5:
            self._clicked = True
            self.piece = 'R'
            
        if 0 < event.x < canvas_width * 0.5 and \
        canvas_height * 0.5 < event.y < canvas_height:
            self._clicked = True
            self.piece = 'B'
            
        if canvas_width * 0.5 < event.x < canvas_width and \
        canvas_height * 0.5 < event.y < canvas_height:
            self._clicked = True
            self.piece = 'K'
        
        if self._clicked:
            self._popup_window.destroy()
    
    def _redraw_canvas(self):
        self._choice_canvas.delete(tkinter.ALL)
        
        canvas_width = self._choice_canvas.winfo_width()
        canvas_height = self._choice_canvas.winfo_height()
        
        self._choice_canvas.create_rectangle(
            0, 0, canvas_width * 0.5, canvas_height * 0.5,
            fill = '#eeeed2', outline = 'black'
            )
        
        self._choice_canvas.create_rectangle(
            canvas_width * 0.5, 0, canvas_width, canvas_height * 0.5,
            fill = '#769656', outline = 'black'
            )
        
        self._choice_canvas.create_rectangle(
            0, canvas_height * 0.5, canvas_width * 0.5, canvas_height,
            fill = '#769656', outline = 'black'
            )
        
        self._choice_canvas.create_rectangle(
            canvas_width * 0.5, canvas_height * 0.5, canvas_width, canvas_height,
            fill = '#eeeed2', outline = 'black'
            )
        
        if self._color == 1:
            self._choice_canvas.create_image(
                canvas_width * 0.25, canvas_height * 0.25, 
                image = self.W_QUEEN)
            
            self._choice_canvas.create_image(
                canvas_width * 0.75, canvas_height * 0.25, 
                image = self.W_ROOK)
            
            self._choice_canvas.create_image(
                canvas_width * 0.25, canvas_height * 0.75, 
                image = self.W_BISHOP)
            
            self._choice_canvas.create_image(
                canvas_width * 0.75, canvas_height * 0.75, 
                image = self.W_KNIGHT)
        
        else:
            self._choice_canvas.create_image(
                canvas_width * 0.25, canvas_height * 0.25, 
                image = self.B_QUEEN)
            
            self._choice_canvas.create_image(
                canvas_width * 0.75, canvas_height * 0.25, 
                image = self.B_ROOK)
            
            self._choice_canvas.create_image(
                canvas_width * 0.25, canvas_height * 0.75, 
                image = self.B_BISHOP)
            
            self._choice_canvas.create_image(
                canvas_width * 0.75, canvas_height * 0.75, 
                image = self.B_KNIGHT)
            
        
    def get_piece(self):
        return self.piece
    
    def was_clicked(self):
        return self._clicked
    
    def show(self):
        self._popup_window.grab_set()
        self._popup_window.wait_window()
        
        