import pygame
from PP import *

FPS = 1

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('HBD MAMA')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                canvas.select(row,col)

        pygame.time.delay(1000)
        canvas.change_all_pixel_color(DARK_SEA_GREEN)
        pygame.time.delay(1000)
        canvas.change_all_pixel_color(FIREBRICK)
        pygame.time.delay(1000)
        canvas.change_pixel_color(PINK, 0, 4)


if __name__ == '__main__':
    main()


