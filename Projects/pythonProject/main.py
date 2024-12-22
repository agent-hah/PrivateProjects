import pygame
from PP import *

pygame.init()
FPS = 120

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Painter')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def handle_drawing(canvas):
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    
    if keys[pygame.K_w]:
        canvas.change_all_pixel_color()
    if mouse[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_row_col_from_mouse(pos)
        canvas.select(row, col)

    if mouse[2]:
        pos = pygame.mouse.get_pos()
        row, col = get_row_col_from_mouse(pos)
        canvas.sample(row,col)

def main():
    run = True
    clock = pygame.time.Clock()
    canvas = Canvas(WIN)
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    canvas.save_object('saved_painting','/Volumes/External Storage/Users/ashmithandoo/Coding/PrivateProjects/Projects/pythonProject/saved_files')
                if event.key == pygame.K_p:
                    canvas.load_object('/Volumes/External Storage/Users/ashmithandoo/Coding/PrivateProjects/Projects/pythonProject/saved_files/saved_painting.pkl')
                if event.key == pygame.K_x:
                    canvas.previous_color()
                if event.key == pygame.K_e:
                    canvas.reset()
                if event.key == pygame.K_1:
                    canvas.check_KEYDOWN(1)
                if event.key == pygame.K_2:
                    canvas.check_KEYDOWN(2)
                if event.key == pygame.K_3:
                    canvas.check_KEYDOWN(3)
                if event.key == pygame.K_4:
                    canvas.check_KEYDOWN(4)
                if event.key == pygame.K_5:
                    canvas.check_KEYDOWN(5)
                if event.key == pygame.K_6:
                    canvas.check_KEYDOWN(6)
                if event.key == pygame.K_7:
                    canvas.check_KEYDOWN(7)
                if event.key == pygame.K_8:
                    canvas.check_KEYDOWN(8)
                if event.key == pygame.K_9:
                    canvas.check_KEYDOWN(9)
                if event.key == pygame.K_c:
                    canvas.next_color()
                if event.key == pygame.K_d:
                    canvas.erase()
                if event.key == pygame.K_z:
                    canvas.undo()
                if event.key == pygame.K_v:
                    canvas.redo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                canvas.set_old_canvas()
            if event.type == pygame.MOUSEBUTTONUP:
                canvas.set_current_canvas()
        handle_drawing(canvas)

if __name__ == '__main__':
    main()
