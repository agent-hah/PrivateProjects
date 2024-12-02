import pygame
from .constants import *
from .pixel import Pixel
import pickle
import os

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
        clockwise = [MAROON, DARK_RED, BROWN, FIREBRICK, CRIMSON, RED, TOMATO, ORANGE_RED, DARK_ORANGE, ORANGE, OLIVE, YELLOW, GREEN, FOREST_GREEN, DARK_SEA_GREEN, TEAL, DARK_CYAN, CYAN, TURQUOISE, SKY_BLUE, NAVY, BLUE, DARK_VIOLET, PURPLE, PINK, TAN, BLACK, WHITE]
        idx = 0
        idx += 1
        if (new_idx > len(clockwise) - 1):
           new_idx = 0 
        color = clockwise[idx]
        for row in range(len(self.canvas)):
            for col in range(len(self.canvas[0])):
                self.canvas[row][col] = Pixel(row, col, color = color)
        self.draw()
    
    def reset(self):
        for row in range(len(self.canvas)):
            for col in range(len(self.canvas[0])):
                self.canvas[row][col] = Pixel(row, col, color = BLACK)
    
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
        clockwise = [MAROON, DARK_RED, BROWN, FIREBRICK, CRIMSON, RED, TOMATO, ORANGE_RED, DARK_ORANGE, ORANGE, OLIVE, YELLOW, GREEN, FOREST_GREEN, DARK_SEA_GREEN, TEAL, DARK_CYAN, CYAN, TURQUOISE, SKY_BLUE, NAVY, BLUE, DARK_VIOLET, PURPLE, PINK, TAN, BLACK, WHITE]
        pixel = self.get_pixel(row, col)
        idx = clockwise.index(pixel.color)
        new_idx = idx + 1
        if (new_idx > len(clockwise) - 1):
           new_idx = 0 
        color = clockwise[new_idx]
        pixel.change_color(color)
        self.draw()
    

    def save_object(self, file_name=None, directory=None):
        """
        Saves a Python object to a file using pickle.
        
        Parameters:
            obj (object): The object to save.
            file_name (str, optional): The name of the file to save the object to. If not provided, a default name is used.
        
        Returns:
            str: The path to the saved file.
        """
        # Generate a default file name if one isn't provided
        if file_name is None:
            file_name = "saved_object.pkl"

        # Ensure the file has the .pkl extension
        if not file_name.endswith(".pkl"):
            file_name += ".pkl"

        # Use the provided directory or the current working directory
        if directory:
            # Create the directory if it doesn't exist
            os.makedirs(directory, exist_ok=True)
            file_path = os.path.join(directory, file_name)
        else:
            file_path = file_name

        # Save the object to the file
        try:
            with open(file_path, "wb") as file:
                pickle.dump(self.canvas, file)
            print(f"Object successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving object: {e}")
            raise

        return os.path.abspath(file_path)
    
    def load_object(self, file_path):
        """
        Loads a Python object from a pickle file.
        
        Parameters:
            file_path (str): The path to the pickle file.
        
        Returns:
            object: The deserialized Python object.
        """
        try:
            with open(file_path, "rb") as file:
                obj = pickle.load(file)
            print(f"Object successfully loaded from {file_path}")
            self.canvas = obj
            self.draw()
            
        except Exception as e:
            print(f"Error loading object: {e}")
            raise
    
    def undo(self, row, col):
        clockwise = [MAROON, DARK_RED, BROWN, FIREBRICK, CRIMSON, RED, TOMATO, ORANGE_RED, DARK_ORANGE, ORANGE, OLIVE, YELLOW, GREEN, FOREST_GREEN, DARK_SEA_GREEN, TEAL, DARK_CYAN, CYAN, TURQUOISE, SKY_BLUE, NAVY, BLUE, DARK_VIOLET, PURPLE, PINK, TAN, BLACK, WHITE]
        pixel = self.get_pixel(row, col)
        idx = clockwise.index(pixel.color)
        new_idx = idx - 1 
        if (new_idx < 0):
           new_idx = (len(clockwise) - 1)
        color = clockwise[new_idx]
        pixel.change_color(color)
        self.draw()