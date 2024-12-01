import pygame
from .constants import *
from .pixel import Pixel

class Canvas:
    def __init__(self, win, rows = ROWS, cols = COLS):
        self.win = win
        self.canvas = []
        self.rows = rows
        self.cols = cols
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
        self.draw
        
    def create_canvas(self):
        for row in range(self.rows):
            self.canvas.append([])
            for col in range(self.cols):
                self.canvas[row].append(Pixel(row, col, color=BLACK))
