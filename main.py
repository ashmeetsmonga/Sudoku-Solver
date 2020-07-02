import pygame
pygame.font.init()
from Grid import Grid


def redraw(win, board):
    win.fill((255, 255, 255))
    fnt = pygame.font.SysFont("comicsans", 30)
    start_label = fnt.render("Press Space Bar to start", True, (0, 0, 0))
    win.blit(start_label, (270 - start_label.get_width() / 2, 560))
    #Draw Board
    board.draw()


def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Solver")
    board = Grid(9, 9, 540, 540, win)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.solve_gui()

        redraw(win, board)
        pygame.display.update()

main()