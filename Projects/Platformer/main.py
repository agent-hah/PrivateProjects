import pygame

class Life():
    def __init__(self, game, mode, day):
        self.game = game
        self.mode = mode
        self.day = day
        
    def __repr__(self):
        return('i create the ships and the houses')