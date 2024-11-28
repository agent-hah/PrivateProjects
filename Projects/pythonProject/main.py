import pygame
from PP import *

FPS = 1

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('HBD MAMA')

def main():
    run = True
    clock = pygame.time.Clock()
    canvas = Canvas(WIN)
    
    while run:
        clock.tick(FPS)
        time = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.delay(1000)
        canvas.change_all_pixel_color(DARK_SEA_GREEN)
        pygame.time.delay(1000)
        canvas.change_all_pixel_color(FIREBRICK)


if __name__ == '__main__':
    main()


