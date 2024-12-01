import pygame
from .constants import *
from .pixel import Pixel

class Canvas:
    def __init__(self, win, rows = ROWS, cols = COLS):
        self.win = win
        self.canvas = []
        self.rows = rows
        self.cols = cols
        self.selected = None
        self.create_canvas()
    
    def get_pixel(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.canvas[row][col]
        else:
            raise IndexError(f"Pixel at row {row}, col {col} is out of bounds.")
    
    def draw(self):
        for row in range(len(self.canvas)):
            for col in range(len(self.canvas[0])):
                pixel = self.get_pixel(row, col)
                pygame.draw.rect(self.win, pixel.color, (pixel.x, pixel.y, SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.update()
            
        
    def change_all_pixel_color(self, color):
        for row in range(len(self.canvas)):
            for col in range(len(self.canvas[0])):
                self.canvas[row][col] = Pixel(row, col, color = color)
        self.draw()
    
    def change_pixel_color(self, color, row, col):
        pixel = self.get_pixel(row, col)
        pixel.change_color(color)
        self.draw()
        
    def create_canvas(self):
        for row in range(self.rows):
            self.canvas.append([])
            for col in range(self.cols):
                self.canvas[row].append(Pixel(row, col, color=BLACK))

    def select(self, row, col):
        if self.selected:
            result = self._change_color(row,col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.get_pixel(row, col)
        self.selected = piece
        return True
    
    def _change_color(self, row, col):
        clockwise = [MAROON, DARK_RED, BROWN, FIREBRICK, CRIMSON, RED, TOMATO, ORANGE_RED, DARK_ORANGE, ORANGE, OLIVE, YELLOW, GREEN, FOREST_GREEN, DARK_SEA_GREEN, TEAL, DARK_CYAN, AQUA, CYAN, TURQUOISE, SKY_BLUE, NAVY, BLUE, DARK_VIOLET, PURPLE, PINK, TAN, BLACK, WHITE]
        pixel = self.get_pixel(row, col)
        idx = clockwise.index(pixel.color)
        new_idx = idx + 1
        if (new_idx > len(clockwise) - 1):
           new_idx = 0 
        color = clockwise[new_idx]
        pixel.change_color(color)
        self.draw()