class Point:
    def __init__(self, frac_x: float, frac_y: float):
        '''
        Initializes a Point object, given its fractional coordinates.
        '''
        self._frac_x = frac_x
        self._frac_y = frac_y
        
    def frac(self) -> (float, float):
        '''
        Returns an (x, y) tuple that contains the fractional coordinates
        for this object.
        '''
        return (self._frac_x, self._frac_y)
    
    def pixel(self, width: int, height: int) -> (int, int):
        '''
        Returns an (x, y) tuple that contains the pixel coordinates for this Point 
        object. The width and the height specify the total size, in pixels, of the 
        area in which the point needs to be specified.
        '''
        return (int(self._frac_x*width), int(self._frac_y*height))

def from_frac(frac_x: float, frac_y: float):
    '''
    Builds a Point given fractional x and y coordinates.
    '''
    return Point(frac_x, frac_y)

def from_pixel(pixel_x, pixel_y, width, height):
    '''
    Builds a Point given pixel x and y coordinates along with the width and height
    of the area (necessary for conversion to fractional).
    '''
    return Point(pixel_x/width, pixel_y/height)
