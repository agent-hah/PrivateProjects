from .constants import *

class Pixel():
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row
    
    def change_color(self, color):
        self.color = color
    
    def __repr__(self):
        return str(self.color)