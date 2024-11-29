import pygame
import asyncio
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax, get_all_moves

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

async def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    move = 1
    ai = []

    while run:
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, float('-inf'), float('inf'), True, game)
            game.ai_move(new_board)
            ai.append([move, value])
            move += 1

        #if game.turn == RED:
            #value, new_board = minimax(game.get_board(), 4, float('-inf'), float('inf'), False, game)
            #game.ai_move(new_board)
            #ai.append([move, value])
        #move += 1


        if game.winner() != None:
            print(f'The winner is {game.winner()}!')
            print(ai)
            run = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)

    
        game.update()
        await asyncio.sleep(0)
    
    pygame.quit()
    quit()


if __name__ == '__main__':  
    asyncio.run(main())
