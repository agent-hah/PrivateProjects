import pygame
from .constants import *
from .pixel import Pixel
import pickle
import os
import copy

pygame.init()
font = pygame.font.Font('arial.ttf',24)

class Canvas:
    def __init__(self, win, rows = ROWS, cols = COLS):
        self.win = win
        self.canvas = []
        self.rows = rows
        self.cols = cols
        self.selected = None
        self.create_canvas()
        self.idx = 0
        self.color = BLACK
        self.background = BLACK
        self.old_canvas = None
        self.current_canvas = None
    
    def get_pixel(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.canvas[row][col]
        elif row < 0 and 0 <= col < self.cols:
            return self.canvas[0][col]
        elif row >= self.rows and 0 <= col < self.cols:
            return self.canvas[self.rows-1][col]
        elif 0 <= row < self.rows and col < 0:
            return self.canvas[row][0]
        elif 0 <= row < self.rows and col >= self.cols:
            return self.canvas[row][self.cols -1]
        elif row < 0 and col < 0:
            return self.canvas[0][0]
        elif row >= self.rows and col >= self.cols:
            return self.canvas[self.rows-1][self.cols-1]
        elif row < 0 and col >= self.cols:
            return self.canvas[0][self.cols-1]
        else: 
            row >= self.rows and col < 0
            return self.canvas[self.rows-1][0]
            

    def draw(self):
        for row in range(len(self.canvas)):
            for col in range(len(self.canvas[0])):
                pixel = self.get_pixel(row, col)
                pygame.draw.rect(self.win, pixel.color, (pixel.x, pixel.y, SQUARE_SIZE, SQUARE_SIZE))
        text = font.render("Red:1 Orange:2 Yellow:3 Green:4 Cyan:5 Blue:6 Violet:7 Black:8 White:9", True, WHITE)
        self.win.blit(text, [15,0])
        pygame.display.update()
            
        
    def change_all_pixel_color(self):
        self.idx += 1
        if (self.idx > len(CLOCKWISE) - 1):
           self.idx = 0 
        self.background = CLOCKWISE[self.idx]
        for row in range(len(self.canvas)):
            for col in range(len(self.canvas[0])):
                pixel = self.get_pixel(row, col)
                pixel.change_color(self.background)
        self.draw()
    
    def reset(self):
        self.idx = 0
        for row in range(len(self.canvas)):
            for col in range(len(self.canvas[0])):
                pixel = self.get_pixel(row, col)
                pixel.change_color(BLACK)
        self.draw()
    
    def create_canvas(self):
        for row in range(self.rows):
            self.canvas.append([])
            for col in range(self.cols):
                self.canvas[row].append(Pixel(row, col, color=BLACK))

    def select(self, row, col):
        if self.selected:
            result = self._paint(row,col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.get_pixel(row, col)
        self.selected = piece
        return True
    
    def undo(self):
        self.canvas = self.old_canvas
        self.draw()

    def redo(self):
        self.canvas = self.current_canvas
        self.draw()
        
    def get_canvas(self):
        return self.canvas
    
    def next_color(self):
        idx = CLOCKWISE.index(self.color)
        new_idx = idx + 1
        if (new_idx > len(CLOCKWISE) - 1):
           new_idx = 0 
        color = CLOCKWISE[new_idx]
        self.color = color
    
    def _paint(self, row, col):
        pixel = self.get_pixel(row, col)
        pixel.change_color(self.color)
        self.draw()
    
    def set_old_canvas(self):
        self.old_canvas = copy.deepcopy(self.canvas)
        return True
    
    def set_current_canvas(self):
        self.current_canvas = copy.deepcopy(self.canvas)
        return True
    
    def erase(self):
        self.color = self.background

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
            self.canvas = obj
            self.draw()
            
        except Exception as e:
            print(f"Error loading object: {e}")
            raise
    
    def previous_color(self):
        idx = CLOCKWISE.index(self.color)
        new_idx = idx - 1 
        if (new_idx < 0):
           new_idx = (len(CLOCKWISE) - 1)
        self.color = CLOCKWISE[new_idx]
    
    def sample(self,row,col):
        pixel = self.get_pixel(row, col)
        self.color = pixel.color
    
    def check_KEYDOWN(self, num):
        if num == 1:
            self.color = RED
            return True
        elif num == 2:
            self.color = ORANGE
            return True
        elif num == 3:
            self.color = YELLOW
            return True
        elif num == 4:
            self.color = GREEN
            return True
        elif num == 5:
            self.color = CYAN
            return True
        elif num == 6:
            self.color = BLUE
            return True
        elif num == 7:
            self.color = VIOLET
            return True
        elif num ==8:
            self.color = BLACK
            return True
        elif num == 9:
            self.color = WHITE
            return True